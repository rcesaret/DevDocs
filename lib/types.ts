export interface DiscoveredPage {
  url: string
  title?: string
  status: 'pending' | 'fetching' | 'scraping' | 'complete' | 'crawled' | 'error'
}

export interface CrawlStats {
  subdomainsParsed: number
  pagesCrawled: number
  dataExtracted: string
  errorsEncountered: number
}

export interface CrawlResult {
  markdown: string
  links: {
    internal: Array<{
      href: string
      text: string
    }>
    external: Array<{
      href: string
      text: string
    }>
  }
  error?: string
}
