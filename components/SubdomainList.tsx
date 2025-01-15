import { Button, ScrollArea } from "@/components/ui"
import { DiscoveredPage } from "@/lib/types"
import { Globe, Loader2, CheckCircle2, AlertCircle, Link as LinkIcon } from 'lucide-react'

interface SubdomainListProps {
  subdomains: DiscoveredPage[]
  onCrawlAll: () => void
  isProcessing: boolean
}

export default function SubdomainList({ subdomains, onCrawlAll, isProcessing }: SubdomainListProps) {
  const getStatusIcon = (status: string, isProcessing: boolean) => {
    switch (status) {
      case 'complete':
        return <CheckCircle2 className="w-4 h-4 text-green-400" />
      case 'error':
        return <AlertCircle className="w-4 h-4 text-red-400" />
      case 'fetching':
        return <Loader2 className={`w-4 h-4 text-yellow-400 ${isProcessing ? 'animate-spin' : ''}`} />
      case 'scraping':
        return <Loader2 className={`w-4 h-4 text-purple-400 ${isProcessing ? 'animate-spin' : ''}`} />
      case 'crawled':
        return <CheckCircle2 className="w-4 h-4 text-green-400" />
      case 'pending':
        return <Loader2 className="w-4 h-4 text-blue-400" />
      default:
        return <Loader2 className="w-4 h-4 text-blue-400" />
    }
  }

  const getStatusStyle = (status: string, isProcessing: boolean) => {
    switch (status) {
      case 'complete':
        return 'bg-green-500/10 text-green-400 border-green-500/20'
      case 'error':
        return 'bg-red-500/10 text-red-400 border-red-500/20'
      case 'fetching':
        return `bg-yellow-500/10 text-yellow-400 border-yellow-500/20 transition-all duration-300 ${isProcessing ? 'opacity-100' : 'opacity-75'}`
      case 'scraping':
        return `bg-purple-500/10 text-purple-400 border-purple-500/20 transition-all duration-300 ${isProcessing ? 'opacity-100' : 'opacity-75'}`
      case 'crawled':
        return 'bg-green-500/10 text-green-400 border-green-500/20'
      case 'pending':
        return 'bg-blue-500/10 text-blue-400 border-blue-500/20'
      default:
        return 'bg-blue-500/10 text-blue-400 border-blue-500/20'
    }
  }

  return (
    <div className="space-y-4 animate-in fade-in duration-500">
      {/* Header */}
      <div className="flex justify-between items-center bg-gray-800/50 backdrop-blur-sm rounded-xl p-4 border border-gray-700">
        <div className="flex items-center gap-3">
          <Globe className="w-5 h-5 text-purple-400" />
          <h2 className="text-xl font-semibold text-purple-400">Discovered Pages</h2>
          <span className="px-2 py-1 rounded-lg bg-purple-500/10 text-purple-400 text-sm">
            {subdomains.length} pages
          </span>
        </div>
        <Button
          onClick={onCrawlAll}
          disabled={isProcessing || subdomains.length === 0}
          className={`
            flex items-center gap-2 transition-all duration-300
            ${isProcessing ? 'bg-purple-500/50' : 'bg-purple-500 hover:bg-purple-600'}
          `}
        >
          {isProcessing ? (
            <>
              <Loader2 className="w-4 h-4 animate-spin" />
              <span>Processing...</span>
            </>
          ) : (
            <>
              <Globe className="w-4 h-4" />
              <span>Crawl All Pages</span>
            </>
          )}
        </Button>
      </div>
      
      {/* Table Container */}
      <div className="rounded-xl border border-gray-700 overflow-hidden bg-gray-900/50 backdrop-blur-sm">
        <ScrollArea className="h-[400px]">
          <table className="w-full">
            <thead className="bg-gray-800/50 sticky top-0">
              <tr>
                <th className="px-4 py-3 text-left text-gray-400 font-medium">URL</th>
                <th className="px-4 py-3 text-left text-gray-400 font-medium">Title</th>
                <th className="px-4 py-3 text-left text-gray-400 font-medium">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-700/50">
              {subdomains.length === 0 ? (
                <tr>
                  <td colSpan={3} className="px-4 py-8 text-center text-gray-400">
                    <div className="flex flex-col items-center gap-2">
                      <Globe className="w-8 h-8 text-gray-500" />
                      <p>No pages discovered yet. Enter a URL to start.</p>
                    </div>
                  </td>
                </tr>
              ) : (
                subdomains.map((page, index) => (
                  <tr
                    key={page.url}
                    className="transition-colors hover:bg-gray-800/30"
                  >
                    <td className="px-4 py-3">
                      <div className="flex items-center gap-2">
                        <LinkIcon className="w-4 h-4 text-gray-500" />
                        <span className="font-mono text-sm text-gray-300 truncate max-w-[300px]">
                          {page.url}
                        </span>
                      </div>
                    </td>
                    <td className="px-4 py-3 text-gray-300">
                      {page.title || 'Untitled'}
                    </td>
                    <td className="px-4 py-3">
                      <div className={`
                        inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium
                        border transition-all duration-300 ${getStatusStyle(page.status, isProcessing)}
                      `}>
                        {getStatusIcon(page.status, isProcessing)}
                        <span className="capitalize">{page.status}</span>
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </ScrollArea>
      </div>
    </div>
  )
}
