# DevDocs 🚀

A powerful documentation crawler and extractor that helps you discover, crawl, and convert web documentation into clean markdown format. Built with Next.js, FastAPI, and Crawl4AI.

The idea of DevDocs is to ensure that software engineers and (LLM) software devs dont have to go through copious amount of tech documentation just to implement the tech. 

Traditionally: You would use cline or equivalent to query what you want to build and it will build it for you using claude or deepseek, but the knowledge cut off date hinders the ability for Cline to provide you the best code for the technology. So you burn through tokens and go through the documentation of that technology and send it to cline or upload to an MCP server. Problem is that the docs are huuuge and you cant copy paste everything. Wouldnt it be easier if a complete markdown file is built for you to upload to your MCP server of choice? 

<<<<<<< Updated upstream
New way: Using Devdocs (Free on Github) you get to just upload the primary URL and crawl every page related to that URL and download the contents in 1 concise markdown. Boom now you have complete knowledge of that tech ready for Cline to work through. This came from a personal frustration of mine when using the documentation of LlamaIndex and Langchain. I will be making improvements to the features so use it and star the repo so you are updated. 
=======
**Solution:** I built a unique platform called DevDocs which spiders through all the child pages of the primary URL, scans if the webpages are live or dead, parses every page (FREE of cost) and converts it into markdown for easy LLM digestion. You can take the markdown and embed into your vector database or use an MCP server like obsidian and load it into Cline for software development. 

**Goal:** I wanted to use state of the art technology but wanted the speed of an up to date LLM, cant do that without an hashtag#MCP(model context protocol) server. So now if I wanted to implement a vector database into my code, I just copy the URL, paste it in DevDocs and the tool grabs all the data from its child websites and spits it into markdown which is then uploaded into my MCP server for Claude to use. This cuts down weeks of research into just a bunch of questions. 

## Roadmap:
- [X] ~~Build a Minimum Viable Product with accurate functionality~~
- [ ] Handle Complex websites documentation like AWS, MS, langchain.
- [ ] Build and add MCP server so all md data is also available in the server. 
- [ ] Turnkey Vector Database so all chunking, embedding is done behind the scenes while you sip your joe
- [ ] Agents which will be pros in particular documentation and can code, architect or reason for you with the accurate information as ground truth.
- [ ] Option to switch to LLM based crawling for specific usecase.
- [ ] UI Improvements, cuz we flashy. 
>>>>>>> Stashed changes

This is V1 of DevDocs, eventually I will be adding MCP servers, Shareable Vector Database, Agents which will be pros in particular documentation and can code for you. 
Stay tuned. 


![image](https://github.com/user-attachments/assets/40f9e0b0-b662-46bf-821a-4dab23c54649)

## ✨ Features

- 🔍 **Smart Discovery**: Automatically finds and maps all related documentation pages
- 📝 **Markdown Conversion**: Converts web content into clean, readable markdown
- 🌐 **Deep Crawling**: Intelligently navigates through complex documentation structures
- 🎯 **Precision Extraction**: Focuses on meaningful content while filtering out noise
- 🚄 **Real-time Progress**: Live updates on crawling progress and statistics
- 💫 **Modern UI**: Sleek, responsive interface with real-time feedback

## 🏗️ Architecture

### Frontend (Next.js + TypeScript)
- Modern React components with TypeScript
- Real-time state management with React hooks
- Tailwind CSS for styling
- Shadcn UI components for consistent design

### Backend (FastAPI + Python)
- FastAPI for high-performance async API
- Crawl4AI for intelligent web crawling
- Advanced error handling and recovery
- Session management for reliable crawling

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.12+
- npm or yarn
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/cyberagiinc/DevDocs.git
cd DevDocs
```

2. Install frontend dependencies:
```bash
npm install
# or
yarn install
```

3. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

### Running the Application

1. Start the backend server:
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 24125 --reload
```

2. Start the frontend development server:
```bash
# In another terminal
npm run dev
# or
yarn dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser

## 💡 How to Use

1. Enter a documentation URL (e.g., https://docs.example.com)
2. Click "Discover" to find all related pages
3. Review the discovered pages in the list
4. Click "Crawl All Pages" to extract content
5. Download or copy the generated markdown

## 🧩 Key Components

### Frontend Components
- `UrlInput`: URL validation and submission
- `SubdomainList`: Displays discovered pages
- `ProcessingBlock`: Shows crawling progress
- `MarkdownOutput`: Displays extracted content

### Backend Services
- `/api/discover`: Finds related documentation pages
- `/api/crawl`: Extracts and converts content to markdown
- Error handling and recovery
- Session management


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

Apache-2.0 license


Built with ❤️ by CyberAGI Inc. | Report Issues like you would do for any Github repo, if you know how to fix it, provide a fix using the Contribution method. 
