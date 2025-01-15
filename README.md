# DevDocs Explorer: Your Documentation Discovery Engine 🚀

Transform scattered documentation into organized knowledge with DevDocs Explorer. This powerful web crawler specializes in discovering and extracting documentation from any website, making it your perfect companion for technical research and documentation management.

## ✨ Key Features

- 🔍 **Smart Discovery**: Automatically finds and maps all related documentation pages
- 📝 **Markdown Magic**: Converts web content into clean, readable markdown
- 🌐 **Deep Crawling**: Intelligently navigates through complex documentation structures
- 🎯 **Precision Extraction**: Focuses on meaningful content while filtering out noise
- 🚄 **Lightning Fast**: Optimized performance with parallel processing
- 📱 **Modern UI**: Sleek, responsive interface with real-time progress tracking

## 🎯 Perfect Use Cases

DevDocs Explorer is ideal for:
- Archiving documentation for offline access
- Converting web docs to markdown for your knowledge base
- Extracting and organizing technical content
- Creating documentation backups

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/devdocs-explorer.git
cd devdocs-explorer
```

2. Install dependencies:
```bash
npm install        # Frontend dependencies
cd backend
pip install -r requirements.txt  # Backend dependencies
```

3. Start the development servers:
```bash
# Terminal 1: Frontend
npm run dev

# Terminal 2: Backend
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 24125 --reload
```

4. Open http://localhost:3000 in your browser

## 💡 How to Use

1. Enter a documentation URL in the input field
2. Click "Discover" to find all related pages
3. Review the discovered pages in the list
4. Click "Crawl All Pages" to extract content
5. Get your documentation in clean markdown format!

## 🛠️ Tech Stack

- **Frontend**: Next.js, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python
- **Crawler**: Crawl4AI, Playwright
- **UI Components**: Shadcn UI

## 📝 License

MIT License - feel free to use it in your own projects!

---

Built with ❤️ by CyberAGI Inc. | [Documentation](https://docs.example.com) | [Report Issues](https://github.com/yourusername/devdocs-explorer/issues)
