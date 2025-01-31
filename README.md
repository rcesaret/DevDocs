# DevDocs 🚀

A powerful documentation crawler and extractor that helps you discover, crawl, and convert web documentation into clean markdown format. Built with Next.js, FastAPI, and Crawl4AI.

The idea of DevDocs is to ensure that software engineers and (LLM) software devs dont have to go through copious amount of tech documentation just to implement the tech. 

Traditionally: You would use cline or equivalent to query what you want to build and it will build it for you using claude or deepseek, but the knowledge cut off date hinders the ability for Cline to provide you the best code for the technology. So you burn through tokens and go through the documentation of that technology and send it to cline or upload to an MCP server. Problem is that the docs are huuuge and you cant copy paste everything. Wouldnt it be easier if a complete markdown file is built for you to upload to your MCP server of choice? 

New way: Using Devdocs (Free on Github) you get to just upload the primary URL and crawl every page related to that URL and download the contents in 1 concise markdown. Boom now you have complete knowledge of that tech ready for Cline to work through. This came from a personal frustration of mine when using the documentation of LlamaIndex and Langchain. I will be making improvements to the features so use it and star the repo so you are updated. 

**Solution:** I built a unique platform called DevDocs which spiders through all the child pages of the primary URL, scans if the webpages are live or dead, parses every page (FREE of cost) and converts it into markdown for easy LLM digestion. You can take the markdown and embed into your vector database or use an MCP server like obsidian and load it into Cline for software development. 

**Goal:** I wanted to use state of the art technology but wanted the speed of an up to date LLM, cant do that without an hashtag#MCP(model context protocol) server. So now if I wanted to implement a vector database into my code, I just copy the URL, paste it in DevDocs and the tool grabs all the data from its child websites and spits it into markdown which is then uploaded into my MCP server for Claude to use. This cuts down weeks of research into just a bunch of questions. 

## Roadmap:
- [X] ~~Build a Minimum Viable Product with accurate functionality~~
- [ ] Handle Complex websites documentation like AWS, MS, langchain :D 
- [X] ~~Adding MCP servers options to choose.~~
- [ ] Turnkey Vector Database so all chunking, embedding is done behind the scenes while you sip your joe :) 
- [ ] Agents which will be pros in particular documentation and can code, architect or reason for you with the accurate information as ground truth.
- [ ] Option to switch to LLM based crawling for specific usecase.
- [ ] UI Improvements, cuz we flashy. 


![image](https://github.com/user-attachments/assets/8bdc3dfe-1fb9-4ace-8259-e6155f44ebcd)


## ✨ Features

- 🔍 **Smart Discovery**: Automatically finds and maps all related documentation pages
- 📝 **Markdown Conversion**: Converts web content into clean, readable markdown
- 🌐 **Deep Crawling**: Intelligently navigates through complex documentation structures
- 🎯 **Precision Extraction**: Focuses on meaningful content while filtering out noise
- 🚄 **Real-time Progress**: Live updates on crawling progress and statistics
- 💫 **Modern UI**: Sleek, responsive interface with real-time feedback
- 🔥 **Inbuilt MCP Server**: No need to copy paste into your MCP server, DevDocs already has an inbuild MCP server, already connect to your claude desktop app upon installation(restart needed) and gives you the commands you need to add to your cline MCP server configs. How cool is that? 

## 🚀 Getting Started

```bash
# 1. Clone and install everything
git clone https://github.com/cyberagiinc/DevDocs.git && cd DevDocs && ./fast-markdown-mcp/setup.sh

# 2. Start all services
./start.sh
```

That's it! The system will:
- Install all dependencies (npm, Python backend, MCP server)
- Configure Claude Desktop integration
- Start all services automatically
- Open the application in your browser (http://localhost:3001)

## 💡 How to Use

1. Enter a documentation URL (e.g., https://docs.example.com)
2. Click "Discover" to find all related pages
3. Review the discovered pages in the list
4. Click "Crawl All Pages" to extract content. Go get some coffee, because it takes a while. 
5. Download the generated markdown/json or use it with an inbuilt MCP server with Cline/Claude

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


Built with ❤️ by CyberAGI Inc. & Shubham Khichi
