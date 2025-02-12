from typing import List, Optional, Set
import logging
import sys
from datetime import datetime
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from urllib.parse import urljoin, urlparse

# Configure logging
logger = logging.getLogger(__name__)

# Increase recursion limit for complex pages
sys.setrecursionlimit(10000)

class InternalLink(BaseModel):
    href: str
    text: str
    status: str = 'pending'  # Default status for internal links

class DiscoveredPage(BaseModel):
    url: str
    title: Optional[str] = None
    status: str = "pending"  # Default status for parent pages
    internalLinks: Optional[List[InternalLink]] = None

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
        viewport_width=1920,
        viewport_height=1080,
        verbose=True,
        text_mode=True,
        light_mode=True,
        extra_args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu"
        ]
    )

def get_crawler_config(session_id: str = None) -> CrawlerRunConfig:
    """Get crawler configuration for content extraction"""
    markdown_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(
            threshold=0.2,
            threshold_type="dynamic",
            min_word_threshold=5
        ),
        options={
            "body_width": 80,
            "ignore_images": True,
            "escape_html": True
        }
    )
    
    return CrawlerRunConfig(
        word_count_threshold=5,
        markdown_generator=markdown_generator,
        cache_mode=CacheMode.ENABLED,
        verbose=True,
        wait_until='domcontentloaded',
        wait_for_images=True,
        scan_full_page=True,
        scroll_delay=0.5,
        page_timeout=120000,
        screenshot=False,
        pdf=False,
        magic=True
    )

def normalize_url(url: str) -> str:
    """Normalize URL by removing trailing slashes and fragments"""
    parsed = urlparse(url)
    path = parsed.path.rstrip('/')
    if not path:
        path = '/'
    return f"{parsed.scheme}://{parsed.netloc}{path}"

async def discover_pages(
    url: str,
    max_depth: int = 3,
    current_depth: int = 1,
    seen_urls: Set[str] = None,
    parent_urls: Set[str] = None,
    all_internal_links: Set[str] = None
) -> List[DiscoveredPage]:
    if seen_urls is None:
        seen_urls = set()
    if parent_urls is None:
        parent_urls = set()
    if all_internal_links is None:
        all_internal_links = set()
    
    url = normalize_url(url)
    discovered_pages = []
    logger.info(f"Starting discovery for URL: {url} at depth {current_depth}/{max_depth}")
    
    if url in seen_urls or current_depth > max_depth:
        logger.info(f"Skipping URL: {url} (seen: {url in seen_urls}, depth: {current_depth})")
        return discovered_pages
        
    seen_urls.add(url)
    parent_urls.add(url)
    
    try:
        browser_config = get_browser_config()
        crawler_config = get_crawler_config()
        
        async with AsyncWebCrawler(config=browser_config) as crawler:
            try:
                result = await crawler.arun(url=url, config=crawler_config)
                
                title = "Untitled Page"
                if result.markdown_v2 and result.markdown_v2.fit_markdown:
                    content_lines = result.markdown_v2.fit_markdown.split('\n')
                    if content_lines:
                        potential_title = content_lines[0].strip('# ').strip()
                        if potential_title:
                            title = potential_title

                internal_links = []
                if hasattr(result, 'links') and isinstance(result.links, dict):
                    seen_internal_links = set()
                    
                    for link in result.links.get("internal", []):
                        href = link.get("href", "")
                        if not href:
                            continue
                            
                        if not href.startswith(('http://', 'https://')):
                            href = urljoin(url, href)
                        href = normalize_url(href)
                            
                        if (href in parent_urls or 
                            href in all_internal_links or 
                            href in seen_internal_links):
                            continue
                            
                        if any(excluded in href.lower() for excluded in [
                            "login", "signup", "register", "logout",
                            "account", "profile", "admin"
                        ]):
                            continue
                            
                        base_domain = urlparse(url).netloc
                        link_domain = urlparse(href).netloc
                        if base_domain != link_domain:
                            continue
                            
                        seen_internal_links.add(href)
                        all_internal_links.add(href)
                        
                        internal_links.append(InternalLink(
                            href=href,
                            text=link.get("text", "").strip()
                        ))
                    
                    logger.info(f"Found {len(internal_links)} unique internal links at depth {current_depth}")

                primary_page = DiscoveredPage(
                    url=url,
                    title=title,
                    internalLinks=internal_links
                )
                discovered_pages.append(primary_page)

                if current_depth < max_depth:
                    for link in internal_links:
                        sub_pages = await discover_pages(
                            url=link.href,
                            max_depth=max_depth,
                            current_depth=current_depth + 1,
                            seen_urls=seen_urls,
                            parent_urls=parent_urls,
                            all_internal_links=all_internal_links
                        )
                        discovered_pages.extend(sub_pages)

            except Exception as e:
                logger.error(f"Error crawling {url}: {str(e)}")
                discovered_pages.append(
                    DiscoveredPage(
                        url=url,
                        title="Error Page",
                        status="error"
                    )
                )

            return discovered_pages

    except Exception as e:
        logger.error(f"Error discovering pages: {str(e)}")
        return [DiscoveredPage(url=url, title="Main Page", status="error")]

async def crawl_pages(pages: List[DiscoveredPage]) -> CrawlResult:
    """
    Crawl multiple pages and combine their content into a single markdown document.
    """
    all_markdown = []
    total_size = 0
    errors = 0
    crawled_urls = set()
    
    try:
        browser_config = get_browser_config()
        crawler_config = get_crawler_config()
        logger.info("Initializing crawler with browser config: %s", browser_config)
        logger.info("Using crawler config: %s", crawler_config)
        
        async with AsyncWebCrawler(config=browser_config) as crawler:
            for page in pages:
                if page.url in crawled_urls:
                    continue
                    
                try:
                    logger.info(f"Crawling page: {page.url}")
                    result = await crawler.arun(url=page.url, config=crawler_config)
                    
                    if result and hasattr(result, 'markdown_v2') and result.markdown_v2:
                        page_markdown = f"# {page.title or 'Untitled Page'}\n"
                        page_markdown += f"URL: {page.url}\n\n"
                        
                        content = None
                        if hasattr(result.markdown_v2, 'fit_markdown') and result.markdown_v2.fit_markdown:
                            content = result.markdown_v2.fit_markdown
                            logger.info(f"Using fit_markdown for {page.url}")
                        elif hasattr(result.markdown_v2, 'raw_markdown') and result.markdown_v2.raw_markdown:
                            content = result.markdown_v2.raw_markdown
                            logger.info(f"Falling back to raw_markdown for {page.url}")
                        
                        if content:
                            filtered_lines = []
                            skip_next = False
                            for line in content.split('\n'):
                                if skip_next:
                                    skip_next = False
                                    continue
                                    
                                if 'To navigate the symbols, press' in line:
                                    skip_next = True
                                    continue
                                    
                                if any(x in line for x in [
                                    'Skip Navigation',
                                    'Search...',
                                    '⌘K',
                                    'symbols inside <root>'
                                ]):
                                    continue
                                    
                                filtered_lines.append(line)
                            
                            filtered_content = '\n'.join(filtered_lines).strip()
                            if filtered_content:
                                page_markdown += filtered_content
                                page_markdown += "\n\n---\n\n"
                                all_markdown.append(page_markdown)
                                total_size += len(page_markdown.encode('utf-8'))
                                logger.info(f"Successfully extracted content from {page.url}")
                                
                                # Mark URL as crawled
                                crawled_urls.add(page.url)
                                page.status = "crawled"
                            else:
                                logger.warning(f"Skipping {page.url} - filtered content was empty")
                                errors += 1
                                page.status = "error"
                        else:
                            logger.warning(f"Skipping {page.url} - no markdown content available")
                            errors += 1
                            page.status = "error"
                    else:
                        logger.warning(f"Skipping {page.url} - no valid result")
                        errors += 1
                        page.status = "error"
                        
                except Exception as e:
                    logger.error(f"Error crawling page {page.url}: {str(e)}")
                    errors += 1
                    page.status = "error"

            combined_markdown = "".join(all_markdown)
            
            size_str = f"{total_size} B"
            if total_size > 1024:
                size_str = f"{total_size/1024:.2f} KB"
            if total_size > 1024*1024:
                size_str = f"{total_size/(1024*1024):.2f} MB"
            
            stats = CrawlStats(
                subdomains_parsed=len(pages),
                pages_crawled=len(crawled_urls),
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