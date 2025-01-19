import { NextResponse } from 'next/server'
import fs from 'fs/promises'
import path from 'path'

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url)
    const filePath = searchParams.get('path')

    if (!filePath) {
      return NextResponse.json(
        { success: false, error: 'No file path provided' },
        { status: 400 }
      )
    }

    // Security check to ensure the path is within the storage directory
    const storagePath = path.join(process.cwd(), 'storage/markdown')
    const normalizedPath = path.normalize(filePath)
    if (!normalizedPath.startsWith(storagePath)) {
      return NextResponse.json(
        { success: false, error: 'Invalid file path' },
        { status: 403 }
      )
    }

    // Check if file exists
    try {
      await fs.access(normalizedPath)
    } catch {
      return NextResponse.json(
        { success: false, error: 'File not found' },
        { status: 404 }
      )
    }

    // Read the file
    const content = await fs.readFile(normalizedPath, 'utf-8')

    // If it's a JSON file, verify it's valid JSON
    if (path.extname(filePath) === '.json') {
      try {
        JSON.parse(content)
      } catch {
        return NextResponse.json(
          { success: false, error: 'Invalid JSON file' },
          { status: 500 }
        )
      }
    }
    
    // Determine content type based on file extension
    const contentType = path.extname(filePath) === '.json' 
      ? 'application/json' 
      : 'text/markdown'

    // Create response with appropriate headers for download
    return new NextResponse(content, {
      headers: {
        'Content-Type': contentType,
        'Content-Disposition': `attachment; filename="${path.basename(filePath)}"`,
      },
    })
  } catch (error) {
    console.error('Error downloading file:', error)
    return NextResponse.json(
      { 
        success: false, 
        error: error instanceof Error ? error.message : 'Failed to download file' 
      },
      { status: 500 }
    )
  }
}