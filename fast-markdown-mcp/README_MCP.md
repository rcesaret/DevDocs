# Fast Markdown MCP Server

A high-performance MCP server for markdown content management with automatic file monitoring, integrated with DevDocs.

## Quick Start

```bash
# 1. Clone and install everything
git clone https://github.com/cyberagi/DevDocs.git && cd DevDocs && ./fast-markdown-mcp/setup.sh

# 2. Start all services
./start.sh
```

That's it! The system will:
- Install all dependencies (npm, Python backend, MCP server)
- Configure Claude Desktop integration
- Start all services automatically
- Open the application in your browser (http://localhost:3001)

## Features

- 📝 Automatic markdown file monitoring
- 🔍 Full-text search across all markdown files
- 🏷️ Tag-based search
- 📊 File statistics and analytics
- 🔄 Real-time file synchronization

## Prerequisites

- Node.js and npm
- Python 3.10 or higher
- Claude Desktop app

## Available MCP Tools

- `list_files` - List all markdown files
- `read_file` - Read content and metadata of a file
- `search_files` - Search content across all files
- `search_by_tag` - Search files by metadata tags
- `get_stats` - Get statistics about all files
- `sync_file` - Force sync a specific file
- `get_status` - Get server status

## Project Structure

```
DevDocs/
├── storage/markdown/    # Markdown files and metadata
├── backend/            # Python backend
├── fast-markdown-mcp/  # MCP server
├── logs/              # Service logs
└── start.sh           # Service launcher
```

## Troubleshooting

1. Check service logs:
```bash
cat logs/frontend.log   # Frontend logs
cat logs/backend.log    # Backend logs
cat logs/mcp.log       # MCP server logs
```

2. Restart services:
```bash
# Stop all services with Ctrl+C
# Then restart:
./start.sh
```

3. Verify services:
- Frontend: http://localhost:3001
- Backend: http://localhost:24125
- Check Claude Desktop logs: `~/Library/Logs/Claude/mcp.log`