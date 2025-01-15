from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
import uvicorn
import logging
import asyncio
import json
from .crawler import discover_pages, crawl_pages, DiscoveredPage, CrawlResult

# Create an event queue for status updates
status_updates = asyncio.Queue()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Crawl4AI Backend")

# Configure CORS to allow requests from our frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DiscoverRequest(BaseModel):
    url: str

class CrawlRequest(BaseModel):
    pages: List[DiscoveredPage]

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/api/discover")
async def discover_endpoint(request: DiscoverRequest):
    """Discover pages related to the provided URL"""
    try:
        logger.info(f"Received discover request for URL: {request.url}")
        pages = await discover_pages(request.url)
        
        # Log the results
        if pages:
            logger.info(f"Successfully discovered {len(pages)} pages")
            for page in pages:
                logger.debug(f"Discovered page: {page.url} ({page.status})")
        else:
            logger.warning("No pages discovered")
            
        # Always return a valid response, even if no pages were found
        return {
            "pages": pages or [],  # Ensure we always return an array
            "message": f"Found {len(pages)} pages" if pages else "No pages discovered",
            "success": True
        }
    except Exception as e:
        logger.error(f"Error discovering pages: {str(e)}", exc_info=True)
        # Return a structured error response
        return {
            "pages": [],
            "message": f"Error discovering pages: {str(e)}",
            "success": False,
            "error": str(e)
        }

@app.post("/api/crawl")
async def crawl_endpoint(request: CrawlRequest, background_tasks: BackgroundTasks):
    """Crawl the provided pages and generate markdown content"""
    try:
        logger.info(f"Received crawl request for {len(request.pages)} pages")
        
        # Start crawling in a background task
        background_tasks.add_task(crawl_and_update_status, request.pages)
        
        return {
            "message": "Crawling started",
            "success": True
        }
    except Exception as e:
        logger.error(f"Error starting crawl: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/crawl/status")
async def status_endpoint():
    """Stream status updates for the crawling process"""
    async def event_generator():
        while True:
            try:
                # Get the next status update
                update = await status_updates.get()
                
                # Format as SSE
                yield f"data: {json.dumps(update)}\n\n"
                
                # If this is the final update, break
                if update.get("complete", False):
                    break
            except asyncio.CancelledError:
                break
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

async def crawl_and_update_status(pages: List[DiscoveredPage]):
    """Background task to crawl pages and send status updates"""
    try:
        # Initialize status queue
        status_queue = asyncio.Queue()
        
        # Start crawling in a separate task to handle status updates
        crawl_task = asyncio.create_task(crawl_pages(pages, status_queue))
        
        # Forward status updates to the SSE queue
        while True:
            try:
                status = await asyncio.wait_for(status_queue.get(), timeout=1.0)
                await status_updates.put(status)
                
                # If this was the final update, break
                if status.get("complete", False):
                    break
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                logger.error(f"Error processing status update: {str(e)}")
                break
        
        # Wait for crawl to complete and get result
        result = await crawl_task
        
        # Send final update if not already sent
        if result:
            await status_updates.put({
                "complete": True,
                "markdown": result.markdown,
                "stats": result.stats.dict(),
                "success": True
            })
            
    except Exception as e:
        logger.error(f"Error in background crawl: {str(e)}")
        await status_updates.put({
            "complete": True,
            "error": str(e),
            "success": False
        })

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=24125,
        reload=True,
        log_level="info"
    )
