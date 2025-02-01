# DevDocs Containerization Strategy

## Overview

This document outlines the strategy for containerizing the DevDocs application while keeping the MCP server local. The architecture will consist of:

1. Frontend Container (Next.js 15.1.4)
2. Backend Container (FastAPI 0.104.0+ with Crawl4AI 0.4.2+)
3. Local MCP Server (fast-markdown-mcp, remains non-containerized)

## Container Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Frontend       │────▶│    Backend      │────▶│   MCP Server   │
│  (Next.js)      │     │   (Crawl4AI)    │     │    (Local)     │
│  Port: 3001     │     │  Port: 24125    │     │   (stdio)      │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                               Storage: ./storage/markdown
```

## Environment-Specific Configurations

### Development Environment

Create `docker-compose.dev.yml`:
```yaml
version: '3.8'

services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
      target: development
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=development
      - NEXT_PUBLIC_BACKEND_URL=http://backend:24125
    volumes:
      - ./:/app
      - /app/node_modules
      - ./logs:/app/logs:rw
    networks:
      - devdocs-network
    depends_on:
      backend:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "wget", "--spider", "http://localhost:3001"]
      interval: 10s
      timeout: 5s
      retries: 3

  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
      target: development
    ports:
      - "24125:24125"
    environment:
      - PYTHONPATH=/app
      - CHROME_BIN=/usr/bin/chromium
      - CHROMEDRIVER_PATH=/usr/bin/chromedriver
      - CRAWLER_CACHE_ENABLED=true
      - CRAWLER_TIMEOUT=120000
      - CRAWLER_WORD_THRESHOLD=5
      - MCP_SERVER_HOST=host.docker.internal
      - MCP_SERVER_PORT=50051
    volumes:
      - ./backend:/app/backend
      - ./logs:/app/logs:rw
      - ./storage:/app/storage:rw
    networks:
      - devdocs-network
    extra_hosts:
      - "host.docker.internal:host-gateway"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:24125/health"]
      interval: 10s
      timeout: 5s
      retries: 3
    command: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "24125", "--reload"]

networks:
  devdocs-network:
    driver: bridge
```

### Production Environment

Create `docker-compose.prod.yml`:
```yaml
version: '3.8'

services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
      target: production
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=production
      - NEXT_PUBLIC_BACKEND_URL=http://backend:24125
    networks:
      - devdocs-network
    depends_on:
      backend:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "wget", "--spider", "http://localhost:3001"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped

  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
      target: production
    ports:
      - "24125:24125"
    environment:
      - PYTHONPATH=/app
      - CHROME_BIN=/usr/bin/chromium
      - CHROMEDRIVER_PATH=/usr/bin/chromedriver
      - CRAWLER_CACHE_ENABLED=true
      - CRAWLER_TIMEOUT=120000
      - CRAWLER_WORD_THRESHOLD=5
      - MCP_SERVER_HOST=host.docker.internal
      - MCP_SERVER_PORT=50051
    volumes:
      - storage_volume:/app/storage
      - log_volume:/app/logs
    networks:
      - devdocs-network
    extra_hosts:
      - "host.docker.internal:host-gateway"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:24125/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    command: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "24125", "--workers", "4"]
    restart: unless-stopped

networks:
  devdocs-network:
    driver: bridge

volumes:
  storage_volume:
  log_volume:
```

## Multi-Stage Dockerfiles

### Frontend Dockerfile

Create `Dockerfile.frontend`:
```dockerfile
# Base stage for shared dependencies
FROM node:20-alpine AS base
WORKDIR /app
ENV NODE_ENV=production

# Development stage
FROM base AS development
ENV NODE_ENV=development
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]

# Builder stage
FROM base AS builder
COPY package*.json ./
RUN npm install --production
COPY . .
RUN npm run build

# Production stage
FROM base AS production
COPY --from=builder /app/next.config.mjs ./
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./

# Set runtime configuration
ENV PORT=3001
ENV NODE_OPTIONS="--max-old-space-size=4096"
EXPOSE 3001

CMD ["npm", "start"]
```

### Backend Dockerfile

Create `Dockerfile.backend`:
```dockerfile
# Base stage for shared dependencies
FROM python:3.11-slim AS base
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    chromium \
    chromium-driver \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Development stage
FROM base AS development
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .

# Production stage
FROM base AS production
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY backend/ .

# Create non-root user
RUN useradd -m -U -s /bin/bash appuser && \
    chown -R appuser:appuser /app /opt/venv

USER appuser

# Set runtime configuration
ENV PYTHONUNBUFFERED=1
EXPOSE 24125
```

## Security Considerations

### Container Security
1. Minimal Base Images:
   - Use Alpine-based images for frontend
   - Use slim Python images for backend
   - Remove unnecessary tools after installation

2. Least Privilege:
   - Run containers as non-root users
   - Minimize container capabilities
   - Use read-only file systems where possible

3. Network Security:
   - Internal Docker network for container communication
   - Expose only necessary ports
   - Use service discovery instead of hardcoded localhost

### Volume Security
1. Production Volumes:
   - Use named volumes instead of bind mounts
   - Implement proper backup strategies
   - Set appropriate file permissions

2. Development Volumes:
   - Use bind mounts for hot reloading
   - Maintain consistent ownership between host and container
   - Implement proper file watching

## Monitoring and Logging

### Health Checks
1. Frontend Health Check:
   - HTTP check on main page
   - Resource availability check
   - Build status verification

2. Backend Health Check:
   - API endpoint check
   - Database connection check
   - MCP server connection check

### Logging Strategy
1. Development:
   - Direct log file mounting
   - Console output for debugging
   - Hot reloading logs

2. Production:
   - Centralized logging system
   - Log rotation and archival
   - Error aggregation

## Scaling Considerations

### Horizontal Scaling
1. Frontend:
   - Stateless design
   - Shared nothing architecture
   - Load balancer ready

2. Backend:
   - Multiple workers
   - Connection pooling
   - Cache sharing

### State Management
1. Session Handling:
   - Distributed session storage
   - Sticky sessions if needed
   - Session persistence

2. Cache Management:
   - Distributed caching
   - Cache invalidation strategy
   - Cache warming

## Development Workflow

1. Start Development Environment:
```bash
# Start MCP Server
./start.sh

# Start Development Containers
docker-compose -f docker-compose.dev.yml up --build
```

2. Start Production Environment:
```bash
# Start MCP Server
./start.sh

# Start Production Containers
docker-compose -f docker-compose.prod.yml up --build
```

## Next Steps

1. Implementation:
   - Create multi-stage Dockerfiles
   - Set up development and production compose files
   - Implement health checks
   - Configure logging

2. Testing:
   - Create integration tests
   - Test scaling scenarios
   - Verify security measures
   - Validate monitoring

3. Documentation:
   - Update deployment guides
   - Document scaling procedures
   - Create troubleshooting guides
   - Maintain configuration references