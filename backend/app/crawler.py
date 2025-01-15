from typing import List, Optional
import logging
import asyncio
from datetime import datetime
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

# Configure logging
logger = logging.getLogger(__name__)

class DiscoveredPage(BaseModel):
    url: str
    title: Optional[str] = None
    status: str = "pending"

class CrawlStats(BaseModel):
    subdomains_parsed: int = 0
    pages_crawled: int = 0
    data_extracted: str = "0 KB"
    errors_encountered: int = 0

class CrawlResult(BaseModel):
    markdown: str
    stats: CrawlStats

def get_browser_config() -> BrowserConfig:
    """Get browser configuration that launches a local instance"""
    return BrowserConfig(
        browser_type="chromium",
        headless=True,
        viewport_width=1280,  # Reduced viewport size for stability
        viewport_height=800,
        verbose=True,
        text_mode=True,
        light_mode=True,
        extra_args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-extensions",
            "--disable-background-networking",
            "--disable-background-timer-throttling",
            "--disable-backgrounding-occluded-windows",
            "--disable-breakpad",
            "--disable-component-extensions-with-background-pages",
            "--disable-features=TranslateUI,BlinkGenPropertyTrees",
            "--disable-ipc-flooding-protection",
            "--disable-renderer-backgrounding",
            "--enable-features=NetworkService,NetworkServiceInProcess",
            "--force-color-profile=srgb",
            "--metrics-recording-only",
            "--mute-audio"
        ]
    )

def get_crawler_config(session_id: str = None) -> CrawlerRunConfig:
    """Get crawler configuration for content extraction"""
    return CrawlerRunConfig(
        word_count_threshold=10,  # Lower threshold for more content
        cache_mode=CacheMode.ENABLED,
        verbose=True,
        wait_until='networkidle',  # Wait for network to be idle
        screenshot=False,
        pdf=False,
        magic=True,  # Enable magic mode for better bot detection avoidance
        scan_full_page=True,
        page_timeout=30000,  # 30 second timeout for page operations
        delay_before_return_html=0.5,  # Wait for dynamic content
        mean_delay=1.0,  # Average delay between requests
        max_range=0.5,  # Variation in delay
        semaphore_count=2  # Limit concurrent operations
    )

async def discover_pages(url: str) -> List[DiscoveredPage]:
    """
    Discover all related pages under a given URL using Crawl4AI's link analysis.
    """
    discovered_pages = []
    logger.info(f"Starting discovery for URL: {url}")
    
    try:
        browser_config = get_browser_config()
        crawler_config = get_crawler_config()
        crawler = None
        logger.info("Initializing crawler with browser config: %s", browser_config)
        logger.info("Using crawler config: %s", crawler_config)
        
        try:
            max_retries = 3
            retry_count = 0
            while retry_count < max_retries:
                try:
                    crawler = AsyncWebCrawler(config=browser_config)
                    await crawler.start()
                    break
                except Exception as e:
                    retry_count += 1
                    logger.error(f"Failed to start crawler (attempt {retry_count}/{max_retries}): {str(e)}")
                    if crawler:
                        try:
                            await crawler.stop()
                        except:
                            pass
                    if retry_count == max_retries:
                        raise
                    await asyncio.sleep(1)  # Wait before retry
            # Add delay before initial crawl
            await asyncio.sleep(0.5)
            
            result = await crawler.arun(url=url, config=crawler_config)
            logger.info(f"Crawl completed for {url}. Success: {result.success}")
            
            # Wait for any dynamic content
            await asyncio.sleep(0.5)
            
            # Extract title from content
            title = "Untitled Page"
            if result.markdown_v2 and result.markdown_v2.fit_markdown:
                content_lines = result.markdown_v2.fit_markdown.split('\n')
                if content_lines:
                    potential_title = content_lines[0].strip('# ').strip()
                    if potential_title:
                        title = potential_title

            # Add the main page
            discovered_pages.append(
                DiscoveredPage(
                    url=url,
                    title=title,
                    status="crawled" if result.success else "pending"
                )
            )

            # Process internal links
            if not hasattr(result, 'links'):
                logger.warning("No links attribute in result")
                return discovered_pages
                
            if not isinstance(result.links, dict):
                logger.warning(f"Unexpected links type: {type(result.links)}")
                return discovered_pages
                
            internal_links = result.links.get("internal", [])
            external_links = result.links.get("external", [])
            
            if not isinstance(internal_links, list) or not isinstance(external_links, list):
                logger.warning(f"Unexpected link list types: internal={type(internal_links)}, external={type(external_links)}")
                return discovered_pages
                
            logger.info(f"Found {len(internal_links)} internal and {len(external_links)} external links")
                
            # Debug log all links
            for link in internal_links:
                logger.debug(f"Internal link found: {link.get('href', '')} ({link.get('text', '')})")
            for link in external_links:
                logger.debug(f"External link found: {link.get('href', '')} ({link.get('text', '')})")
            
            # Debug result structure
            logger.debug(f"Result attributes: {dir(result)}")
            logger.debug(f"Links structure: {result.links}")
            
            # Process each internal link
            for link in internal_links:
                try:
                    href = link.get("href", "")
                    if not href:
                        logger.debug(f"Skipping empty URL")
                        continue
                    
                    # Handle relative paths
                    if not href.startswith(('http://', 'https://')):
                        # Check if it's a root-relative path
                        if href.startswith('/'):
                            from urllib.parse import urlparse
                            base = urlparse(url)
                            href = f"{base.scheme}://{base.netloc}{href}"
                        else:
                            # Regular relative path
                            from urllib.parse import urljoin
                            href = urljoin(url, href)
                        logger.debug(f"Converted relative URL: {href}")
                    
                    # Remove URL fragments and query parameters
                    if '#' in href:
                        href = href.split('#')[0]
                    if '?' in href:
                        href = href.split('?')[0]

                    # Parse URL
                    from urllib.parse import urlparse
                    parsed_url = urlparse(href)
                    base_url = urlparse(url)

                    # Debug URL parsing
                    logger.debug(f"URL parsing - Base: {base_url.netloc}, Current: {parsed_url.netloc}")

                    # Get base domains for comparison
                    base_domain = '.'.join(base_url.netloc.split('.')[-2:])  # e.g., crawl4ai.com
                    current_domain = '.'.join(parsed_url.netloc.split('.')[-2:]) if parsed_url.netloc else base_domain
                    
                    # Allow links within the same root domain
                    if current_domain != base_domain:
                        logger.debug(f"Skipping external URL: {href} (domain mismatch: {current_domain} != {base_domain})")
                        continue
                    
                    logger.debug(f"Accepting URL from domain: {parsed_url.netloc} (root domain: {current_domain})")

                    # Skip common restricted paths
                    if any(excluded in href.lower() for excluded in [
                        "login", "signup", "register", "logout",
                        "account", "profile", "admin"
                    ]):
                        logger.debug(f"Skipping restricted URL: {href}")
                        continue
                        
                    # Normalize URL by removing trailing slash
                    href = href.rstrip('/')
                    
                    # Skip if we already have this URL (normalized comparison)
                    if any(page.url.rstrip('/') == href for page in discovered_pages):
                        logger.debug(f"Skipping duplicate URL: {href}")
                        continue

                    # Log the accepted URL
                    logger.info(f"Found valid internal link: {href}")

                    link_title = link.get("text", "").strip() or "Untitled Page"
                    logger.info(f"Adding discovered page: {href} ({link_title})")
                    discovered_pages.append(
                        DiscoveredPage(
                            url=href,
                            title=link_title,
                            status="pending"
                        )
                    )
                except Exception as e:
                    logger.error(f"Error processing link {link}: {str(e)}")
                    continue

            logger.info(f"Discovered {len(discovered_pages)} valid pages from {url}")
            return discovered_pages

        except Exception as e:
            logger.error(f"Error discovering pages: {str(e)}")
            return [DiscoveredPage(url=url, title="Main Page", status="pending")]
        finally:
            if crawler:
                try:
                    if hasattr(crawler, 'stop'):
                        await crawler.stop()
                    elif hasattr(crawler, 'close'):
                        await crawler.close()
                except Exception as e:
                    logger.error(f"Error stopping crawler: {str(e)}")

    except Exception as e:
        logger.error(f"Error setting up crawler: {str(e)}")
        return [DiscoveredPage(url=url, title="Main Page", status="pending")]

async def crawl_pages(pages: List[DiscoveredPage], status_queue: asyncio.Queue = None) -> CrawlResult:
    """
    Crawl multiple pages and combine their content into a single markdown document.
    """
    all_markdown = []
    total_size = 0
    errors = 0
    crawler = None
    
    try:
        browser_config = get_browser_config()
        crawler_config = get_crawler_config()
        logger.info("Initializing crawler with browser config: %s", browser_config)
        logger.info("Using crawler config: %s", crawler_config)
        
        try:
            max_retries = 3
            retry_count = 0
            while retry_count < max_retries:
                try:
                    crawler = AsyncWebCrawler(config=browser_config)
                    await crawler.start()
                    break
                except Exception as e:
                    retry_count += 1
                    logger.error(f"Failed to start crawler (attempt {retry_count}/{max_retries}): {str(e)}")
                    if crawler:
                        try:
                            await crawler.stop()
                        except:
                            pass
                    if retry_count == max_retries:
                        raise
                    await asyncio.sleep(1)  # Wait before retry
            for page in pages:
                try:
                    # Update status to fetching
                    logger.info(f"[FETCH]... ↓ {page.url}")
                    page.status = "fetching"
                    if status_queue:
                        await status_queue.put({
                            "pages": [{"url": p.url, "status": p.status, "title": p.title} for p in pages]
                        })
                    
                    result = await crawler.arun(url=page.url, config=crawler_config)
                    
                    # Update status to scraping
                    logger.info(f"[SCRAPE]... ⚡ {page.url}")
                    page.status = "scraping"
                    if status_queue:
                        await status_queue.put({
                            "pages": [{"url": p.url, "status": p.status, "title": p.title} for p in pages]
                        })
                    
                    await asyncio.sleep(1)  # Add 1 second delay between pages
                    
                    if result and hasattr(result, 'markdown_v2') and result.markdown_v2:
                        logger.info(f"[COMPLETE] ● {page.url}")
                        page.status = "complete"
                        if status_queue:
                            await status_queue.put({
                                "pages": [{"url": p.url, "status": p.status, "title": p.title} for p in pages]
                            })
                        # Add page title and URL as header
                        page_markdown = f"# {page.title or 'Untitled Page'}\n"
                        page_markdown += f"URL: {page.url}\n\n"
                        
                        # Add markdown content
                        if hasattr(result.markdown_v2, 'fit_markdown') and result.markdown_v2.fit_markdown:
                            page_markdown += result.markdown_v2.fit_markdown
                            logger.info(f"Successfully extracted content from {page.url}")
                        else:
                            page_markdown += result.markdown_v2.raw_markdown
                            logger.warning(f"Using raw markdown for {page.url}")
                            
                        page_markdown += "\n\n---\n\n"
                        
                        all_markdown.append(page_markdown)
                        total_size += len(page_markdown.encode('utf-8'))
                    else:
                        logger.warning(f"[WARNING] ⚠ No valid result for {page.url}")
                        page.status = "error"
                        if status_queue:
                            await status_queue.put({
                                "pages": [{"url": p.url, "status": p.status, "title": p.title} for p in pages]
                            })
                        errors += 1
                        
                except Exception as e:
                    logger.error(f"[ERROR] × {page.url}: {str(e)}")
                    page.status = "error"
                    if status_queue:
                        await status_queue.put({
                            "pages": [{"url": p.url, "status": p.status, "title": p.title} for p in pages]
                        })
                    errors += 1

            combined_markdown = "".join(all_markdown)
            
            # Calculate human-readable size
            size_str = f"{total_size} B"
            if total_size > 1024:
                size_str = f"{total_size/1024:.2f} KB"
            if total_size > 1024*1024:
                size_str = f"{total_size/(1024*1024):.2f} MB"
            
            stats = CrawlStats(
                subdomains_parsed=len(pages),
                pages_crawled=len(pages) - errors,
                data_extracted=size_str,
                errors_encountered=errors
            )
            
            logger.info(f"Completed crawling with stats: {stats}")
            return CrawlResult(
                markdown=combined_markdown,
                stats=stats
            )

        except Exception as e:
            logger.error(f"Error in crawl_pages: {str(e)}")
            return CrawlResult(
                markdown="",
                stats=CrawlStats(
                    subdomains_parsed=len(pages),
                    pages_crawled=0,
                    data_extracted="0 KB",
                    errors_encountered=1
                )
            )
        finally:
            if crawler:
                try:
                    if hasattr(crawler, 'stop'):
                        await crawler.stop()
                    elif hasattr(crawler, 'close'):
                        await crawler.close()
                except Exception as e:
                    logger.error(f"Error stopping crawler: {str(e)}")
                    
    except Exception as e:
        logger.error(f"Error setting up crawler: {str(e)}")
        return CrawlResult(
            markdown="",
            stats=CrawlStats(
                subdomains_parsed=len(pages),
                pages_crawled=0,
                data_extracted="0 KB",
                errors_encountered=1
            )
        )
