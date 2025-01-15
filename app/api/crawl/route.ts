import { NextResponse } from 'next/server'
import { DiscoveredPage } from '@/lib/types'

export async function POST(request: Request) {
  try {
    const { pages } = await request.json()

    if (!Array.isArray(pages)) {
      return NextResponse.json(
        { error: 'Pages array is required' },
        { status: 400 }
      )
    }

    // Start the crawl process
    const response = await fetch('http://localhost:24125/api/crawl', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ pages }),
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.message || 'Failed to start crawl')
    }

    // Set up SSE connection
    const stream = new ReadableStream({
      async start(controller) {
        const eventSource = new EventSource('http://localhost:24125/api/crawl/status')
        
        eventSource.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data)
            controller.enqueue(JSON.stringify(data) + '\n')
            
            // Close the connection when complete
            if (data.complete) {
              eventSource.close()
              controller.close()
            }
          } catch (e) {
            console.error('Error parsing SSE message:', e)
          }
        }

        eventSource.onerror = (error) => {
          console.error('SSE error:', error)
          eventSource.close()
          controller.error(error)
        }
      }
    })

    return new Response(stream, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
      },
    })
  } catch (error) {
    console.error('Error in crawl route:', error)
    return NextResponse.json(
      { error: 'Failed to crawl pages' },
      { status: 500 }
    )
  }
}
