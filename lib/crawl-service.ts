import { DiscoveredPage, CrawlResult } from './types'

const BACKEND_URL = 'http://localhost:24125'

export async function discoverSubdomains(primaryUrl: string): Promise<DiscoveredPage[]> {
  try {
    console.log('Making request to backend:', `${BACKEND_URL}/api/discover`)
    console.log('Request payload:', { url: primaryUrl })

    const response = await fetch(`${BACKEND_URL}/api/discover`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: primaryUrl }),
    })

    console.log('Response status:', response.status)
    const data = await response.json()
    console.log('Response data:', data)

    if (!response.ok) {
      console.error('Error response:', data)
      throw new Error(data.detail || 'Failed to discover subdomains')
    }

    // If we get a successful response but no pages, log it
    if (!data.pages || !Array.isArray(data.pages)) {
      console.warn('No pages array in response:', data)
      return []
    }

    // Log each discovered page
    console.log('Discovered pages:', data.pages.length)
    data.pages.forEach((page: DiscoveredPage) => {
      console.log('Page:', {
        url: page.url,
        title: page.title,
        status: page.status
      })
    })

    return data.pages
  } catch (error) {
    console.error('Error discovering subdomains:', error)
    // Re-throw the error to be handled by the UI
    throw error
  }
}

export async function crawlPages(
  pages: DiscoveredPage[],
  onStatusUpdate?: (updatedPages: DiscoveredPage[]) => void
): Promise<CrawlResult> {
  try {
    console.log('Making request to backend for crawling:', pages.length, 'pages')
    
    const response = await fetch(`${BACKEND_URL}/api/crawl`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ pages }),
    })

    if (!response.ok) {
      throw new Error(await response.text() || 'Failed to crawl pages')
    }

    // Set up SSE for status updates
    const eventSource = new EventSource(`${BACKEND_URL}/api/crawl/status`)
    
    eventSource.onmessage = (event) => {
      try {
        const update = JSON.parse(event.data)
        if (update.pages && onStatusUpdate) {
          onStatusUpdate(update.pages)
        }
      } catch (e) {
        console.error('Error parsing status update:', e)
      }
    }

    eventSource.onerror = () => {
      eventSource.close()
    }

    // Wait for the final response
    const data = await response.json()
    eventSource.close()

    return {
      markdown: data.markdown || '',
      links: {
        internal: data.links?.internal || [],
        external: data.links?.external || []
      },
      error: data.error
    }
  } catch (error) {
    console.error('Error crawling pages:', error)
    return {
      markdown: '',
      links: {
        internal: [],
        external: []
      },
      error: error instanceof Error ? error.message : 'Unknown error occurred'
    }
  }
}

export function validateUrl(url: string): boolean {
  try {
    new URL(url)
    return true
  } catch {
    return false
  }
}

export function formatBytes(bytes: number): string {
  if (bytes === 0) return '0 KB'
  const k = 1024
  const sizes = ['B', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(2))} ${sizes[i]}`
}
