# Consolidated Documentation for https://mcp-framework.com/docs/introduction

This file contains content from multiple pages related to https://mcp-framework.com/docs/introduction.
Each section represents a different page that was crawled.

---


## Untitled Page
URL: https://mcp-framework.com/docs/introduction

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](#)

  * [Examples](#)

  * [Prompts](#)

  * [Resources](#)

  * [Tools](#)

  * [Transports](#)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Introduction



On this page

# Introduction to MCP Framework

This framework makes it easy to create and manage MCP (modelcontextprotocol) servers that can be used with MCP Clients like the Claude Desktop app.

It is simple and intuitive to use.

MCP-Framework gives you architecture out of the box, with automatic directory-based discovery for tools, resources, and prompts. Use our powerful MCP abstractions to define tools, resources, or prompts in an elegant way. Our cli makes getting started with your own MCP server a breeze

Quick Setup

You can build a MCP server with mcp-framework in under 5 minutes! [Follow the quickstart guide](/docs/quickstart) to get started.

[Quickstart Guide](/docs/quickstart)

## Key Features[​](#key-features "Direct link to Key Features")

  * **Tool Support** : Create custom tools that extend AI model capabilities
  * **Resource Management** : Handle external data sources and APIs
  * **Prompt Templates** : Define reusable prompt templates
  * **Multiple Transports** : Support for both STDIO and SSE (Server-Sent Events) communication
  * **Authentication** : Built-in JWT and API Key authentication for SSE transport
  * **Use the power of Typescript** : Full TypeScript support with type safety
  * **CLI Tool** : Easy project scaffolding and component creation
  * **Fast Development** : Elegant and fast development cycles



## How It Works[​](#how-it-works "Direct link to How It Works")

MCP Framework provides four main components:

### 1. Tools[​](#1-tools "Direct link to 1. Tools")

Functions that AI models can invoke to:

  * Fetch data from APIs
  * Transform data
  * Perform computations
  * Interact with external services



### 2. Resources[​](#2-resources "Direct link to 2. Resources")

Data sources that can be:

  * Read by the AI model
  * Subscribed to for updates
  * Used to provide context



### 3. Prompts[​](#3-prompts "Direct link to 3. Prompts")

Template systems that:

  * Define reusable conversation flows
  * Provide structured context
  * Guide model interactions



### 4. Transports[​](#4-transports "Direct link to 4. Transports")

Communication layers that:

  * Handle client-server communication
  * Support different use cases: 
    * **STDIO** : Perfect for CLI tools and local integrations
    * **SSE** : Ideal for web applications with optional authentication



The framework handles all communication between your server and AI models, following the Model Context Protocol specification.

## When to Use MCP Framework[​](#when-to-use-mcp-framework "Direct link to When to Use MCP Framework")

  * Building custom tools for AI models
  * Creating data integration services
  * Developing specialized AI assistants
  * Extending AI capabilities with external services
  * Building enterprise AI solutions
  * Creating web-based AI tools (using SSE transport)
  * Developing secure AI services with authentication



Ready to get started? Head to the [Installation](/docs/installation) guide to begin building your first MCP server, or learn more about our [transport options](/docs/Transports/transports-overview).

[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/introduction.md)

[NextInstallation](/docs/installation)

  * [Key Features](#key-features)
  * [How It Works](#how-it-works)
    * [1. Tools](#1-tools)
    * [2. Resources](#2-resources)
    * [3. Prompts](#3-prompts)
    * [4. Transports](#4-transports)
  * [When to Use MCP Framework](#when-to-use-mcp-framework)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

# MCP Framework

Build Model Context Protocol Servers in TypeScript

[Get Started →](/docs/introduction)[5-Min Tutorial ⚡](/docs/quickstart)

# MCP Framework

Build powerful Model Context Protocol servers in TypeScript

⚡

### Lightning Fast Setup

Create your MCP server in under 5 minutes with our CLI. One command is all it takes to start building.

🛠️

### Powerful Tools

Build type-safe tools that extend AI capabilities. From API integrations to data processing, the possibilities are endless.

🔄

### Auto-Discovery

Focus on building features. Our framework automatically discovers and loads your tools, resources, and prompts.

Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/installation

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Installation



On this page

# Installation

Setting up the MCP Framework is straightforward. You can either create a new project using our CLI or add it to an existing project.

## Using the CLI (Recommended)[​](#using-the-cli-recommended "Direct link to Using the CLI \(Recommended\)")

The easiest way to get started is using our CLI to create a new project:

```
`# Install the CLI globally with npmnpm install -g mcp-framework# The mcp CLI is now globally available# Create your new project with the mcp CLImcp create my-mcp-server# Navigate to your projectcd my-mcp-server# Install dependenciesnpm install`
```

This will create a new project with the following structure:

```
`my-mcp-server/├── src/│ ├── tools/ # MCP Tools directory│ │ └── ExampleTool.ts│ └── index.ts # Server entry point├── package.json└── tsconfig.json`
```

To open this project in vscode, use:

```
`code .`
```

## Manual Installation[​](#manual-installation "Direct link to Manual Installation")

If you prefer to add MCP Framework to an existing project:

```
`npm install mcp-framework`
```

Then create a minimal server in `src/index.ts`:

```
`import{MCPServer}from"mcp-framework";const server =newMCPServer();server.start().catch((error)=>{console.error("Server error:", error); process.exit(1);});`
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

After installation, you can:

  1. Follow the [Quickstart](/docs/quickstart) guide to create your first tool
  2. Learn about [Tools](/docs/Tools/tools-overview)
  3. Explore [Resources](/docs/Resources/resources-overview)
  4. Check out [Prompts](/docs/Prompts/prompts-overview)



## Requirements[​](#requirements "Direct link to Requirements")

  * Node.js 18 or later
  * TypeScript 5.0 or later
  * npm or yarn package manager



## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Common Issues[​](#common-issues "Direct link to Common Issues")

  1. **TypeScript Errors** :

```
`error TS2304: Cannot find name 'z'`
```

Solution: Install zod - `npm install zod`

  2. **Module Resolution Issues** :

```
`Error: Cannot find module '@modelcontextprotocol/sdk'`
```

Solution: Install peer dependencies - `npm install @modelcontextprotocol/sdk`




For more help, check our [GitHub Issues](https://github.com/QuantGeekDev/mcp-framework/issues) or join our [Discord community](https://discord.gg/RMCFtcEuYd).

[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/installation.md)

[PreviousIntroduction](/docs/introduction)[NextQuickstart](/docs/quickstart)

  * [Using the CLI (Recommended)](#using-the-cli-recommended)
  * [Manual Installation](#manual-installation)
  * [Next Steps](#next-steps)
  * [Requirements](#requirements)
  * [Troubleshooting](#troubleshooting)
    * [Common Issues](#common-issues)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Authentication/overview

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

    * [Authentication](/docs/Authentication/overview)
  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Authentication
  * Authentication



On this page

# Authentication

The MCP Framework provides built-in authentication support through various authentication providers. This allows you to secure your MCP server endpoints and ensure only authorized clients can access your tools and resources.

## Available Authentication Providers[​](#available-authentication-providers "Direct link to Available Authentication Providers")

### API Key Authentication[​](#api-key-authentication "Direct link to API Key Authentication")

The API Key authentication provider allows you to secure your endpoints using API keys. This is useful for simple authentication scenarios where you want to control access using predefined keys.

```
`import{APIKeyAuthProvider}from"@modelcontextprotocol/mcp-framework";const authProvider =newAPIKeyAuthProvider({ keys:["your-api-key-1","your-api-key-2"], headerName:"X-API-Key"// Optional, defaults to "X-API-Key"});`
```

Clients must include the API key in the specified header:

```
`X-API-Key: your-api-key-1`
```

### JWT Authentication[​](#jwt-authentication "Direct link to JWT Authentication")

The JWT authentication provider enables token-based authentication using JSON Web Tokens. This is suitable for more complex authentication scenarios where you need to include user information or other claims in the token.

```
`import{JWTAuthProvider}from"@modelcontextprotocol/mcp-framework";const authProvider =newJWTAuthProvider({ secret:"your-jwt-secret", algorithms:["HS256"],// Optional, defaults to ["HS256"] headerName:"Authorization",// Optional, defaults to "Authorization" requireBearer:true// Optional, defaults to true});`
```

Clients must include the JWT token in the Authorization header:

```
`Authorization: Bearer eyJhbGciOiJIUzI1NiIs...`
```

## Configuring Authentication[​](#configuring-authentication "Direct link to Configuring Authentication")

You can configure authentication when setting up your SSE transport:

```
`import{MCPServer,APIKeyAuthProvider}from"@modelcontextprotocol/mcp-framework";const server =newMCPServer({ transport:{ type:"sse", options:{ auth:{ provider:newAPIKeyAuthProvider({ keys:["your-api-key"]}), endpoints:{ sse:true,// Require auth for SSE connections messages:true// Require auth for messages}}}}});`
```

### Endpoint Configuration[​](#endpoint-configuration "Direct link to Endpoint Configuration")

The `endpoints` configuration allows you to specify which endpoints require authentication:

  * `sse`: Controls authentication for the SSE connection endpoint 
    * Default: `false`
  * `messages`: Controls authentication for the message endpoint 
    * Default: `true`



## Error Handling[​](#error-handling "Direct link to Error Handling")

Authentication providers include built-in error handling that returns appropriate HTTP status codes and error messages:

```
`// Example error response for invalid API key{"error":"Invalid API key","status":401,"type":"authentication_error"}// Example error response for invalid JWT{"error":"Invalid or expired JWT token","status":401,"type":"authentication_error"}`
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

  1. **API Key Security** :

     * Use long, random strings for API keys
     * Rotate keys periodically
     * Store keys securely
     * Use HTTPS in production
  2. **JWT Security** :

     * Use a strong secret key
     * Set appropriate token expiration
     * Include only necessary claims
     * Use secure algorithms (HS256, RS256, etc.)
  3. **General Security** :

     * Enable authentication for both SSE and message endpoints in production
     * Use environment variables for secrets
     * Implement rate limiting
     * Monitor failed authentication attempts



[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Authentication/overview.md)

[PreviousDebugging](/docs/debugging)[NextUS Treasury Fiscal Data Example](/docs/Examples/fiscal-data)

  * [Available Authentication Providers](#available-authentication-providers)
    * [API Key Authentication](#api-key-authentication)
    * [JWT Authentication](#jwt-authentication)
  * [Configuring Authentication](#configuring-authentication)
    * [Endpoint Configuration](#endpoint-configuration)
  * [Error Handling](#error-handling)
  * [Best Practices](#best-practices)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Examples/fiscal-data

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

    * [US Treasury Fiscal Data Example](/docs/Examples/fiscal-data)
  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Examples
  * US Treasury Fiscal Data Example



On this page

# US Treasury Fiscal Data Example

Live Example

See MCP Framework in action with this US Treasury data server that provides real-time access to treasury statements and operating cash balances!

## Overview[​](#overview "Direct link to Overview")

The [Fiscal Data MCP Server](https://github.com/QuantGeekDev/fiscal-data-mcp) demonstrates a practical implementation of an MCP server that connects to the US Treasury's Fiscal Data API. It showcases:

  * Tools for fetching specific treasury statements
  * Resources for historical data access
  * Prompts for generating formatted reports
  * Smart caching for API efficiency



## Features[​](#features "Direct link to Features")

### 1. Daily Treasury Statements[​](#1-daily-treasury-statements "Direct link to 1. Daily Treasury Statements")

Fetch treasury data for specific dates using the `get_daily_treasury_statement` tool:

Example usage:

```
`User:Get the treasury statement for2024-03-01`
```

### 2. Historical Data Resource[​](#2-historical-data-resource "Direct link to 2. Historical Data Resource")

Access 30 days of historical treasury data through the resource system:

  * Automatically cached for 1 hour
  * Updates on demand
  * Provides formatted JSON data



### 3. Report Generation[​](#3-report-generation "Direct link to 3. Report Generation")

Generate formatted treasury reports using the `daily_treasury_report` prompt:

```
`User:Generate a treasury report for2024-03-01`
```

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Install and Use with Claude Desktop[​](#1-install-and-use-with-claude-desktop "Direct link to 1. Install and Use with Claude Desktop")

Add this configuration to your Claude Desktop config file:

**MacOS** : `~/Library/Application Support/Claude/claude_desktop_config.json` **Windows** : `%APPDATA%/Claude/claude_desktop_config.json`

```
`{"mcpServers":{"fiscal-data":{"command":"npx","args":["fiscal-data-mcp"]}}}`
```

### 2. Example Interactions[​](#2-example-interactions "Direct link to 2. Example Interactions")

Once configured, you can interact with the server through Claude:

```
`User: Can you get the treasury statement for the 20th of September 2023?`
```

[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Examples/us-treasury-data.md)

[PreviousAuthentication](/docs/Authentication/overview)[NextPrompts Overview](/docs/Prompts/prompts-overview)

  * [Overview](#overview)
  * [Features](#features)
    * [1. Daily Treasury Statements](#1-daily-treasury-statements)
    * [2. Historical Data Resource](#2-historical-data-resource)
    * [3. Report Generation](#3-report-generation)
  * [Quick Start](#quick-start)
    * [1. Install and Use with Claude Desktop](#1-install-and-use-with-claude-desktop)
    * [2. Example Interactions](#2-example-interactions)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Prompts/prompts-overview

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

    * [Prompts Overview](/docs/Prompts/prompts-overview)
  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Prompts
  * Prompts Overview



On this page

# Working with Prompts

Power of Prompts

Prompts let you create reusable templates for AI interactions, making your MCP server more consistent and powerful!

## What are Prompts?[​](#what-are-prompts "Direct link to What are Prompts?")

Prompts are reusable templates that:

  * Define conversation flows
  * Provide structured context
  * Use dynamic data
  * Ensure consistent AI responses



Here's a simple example:

```
`import{MCPPrompt}from"mcp-framework";import{ z }from"zod";interfaceGreetingPromptInput{ userName:string; timeOfDay:string;}classGreetingPromptextendsMCPPrompt<GreetingPromptInput>{ name ="greeting"; description ="Generates a personalized greeting"; schema ={ userName:{ type: z.string(), description:"User's name", required:true,}, timeOfDay:{ type: z.enum(["morning","afternoon","evening"]), description:"Time of day", required:true,},};asyncgenerateMessages({ userName, timeOfDay }){return[{ role:"user", content:{ type:"text", text:`Good ${timeOfDay}${userName}! How can I assist you today?`,},},];}}`
```

## Creating Prompts[​](#creating-prompts "Direct link to Creating Prompts")

### Using the CLI[​](#using-the-cli "Direct link to Using the CLI")

```
`mcp add prompt my-prompt`
```

This creates a new prompt in `src/prompts/MyPrompt.ts`.

### Prompt Structure[​](#prompt-structure "Direct link to Prompt Structure")

Every prompt has:

  1. **Metadata**



```
`name ="data-analysis";description ="Analyzes data with specific parameters";`
```

  1. **Input Schema**



```
`schema ={ dataset:{ type: z.string(), description:"Dataset to analyze", required:true,}, metrics:{ type: z.array(z.string()), description:"Metrics to calculate", required:true,},};`
```

  1. **Message Generation**



```
`asyncgenerateMessages(input){return[{ role:"user", content:{ type:"text", text:`Analyze ${input.dataset} for ${input.metrics.join(", ")}`}}];}`
```

## Advanced Features[​](#advanced-features "Direct link to Advanced Features")

### Using Resources in Prompts[​](#using-resources-in-prompts "Direct link to Using Resources in Prompts")

```
`classDataAnalysisPromptextendsMCPPrompt{asyncgenerateMessages({ datasetId }){const dataResource =newDatasetResource(datasetId);const[data]=await dataResource.read();return[{ role:"user", content:{ type:"text", text:"Please analyze this dataset:", resource:{ uri: data.uri, text: data.text, mimeType: data.mimeType,},},},];}}`
```

### Multi-step Prompts[​](#multi-step-prompts "Direct link to Multi-step Prompts")

```
`classReportPromptextendsMCPPrompt{asyncgenerateMessages({ reportType }){return[{ role:"system", content:{ type:"text", text:"You are a professional report writer.",},},{ role:"user", content:{ type:"text", text:`Create a ${reportType} report using the following data:`,},},];}}`
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

Pro Tips

Follow these practices for better prompt design!

  1. **Clear Naming**



```
`name ="financial-analysis";// Goodname ="fa";// Bad`
```

  1. **Detailed Descriptions**



```
`description ="Analyzes financial data and provides insights with specific metrics";`
```

  1. **Input Validation**



```
`schema ={ email:{ type: z.string().email(), description:"Valid email address", required:true,},};`
```

  1. **Structured Messages**



```
`asyncgenerateMessages(input){return[{ role:"system", content:{ type:"text", text:"Context setting message"}},{ role:"user", content:{ type:"text", text:"Main instruction"}}];}`
```

## Examples[​](#examples "Direct link to Examples")

### Report Generator[​](#report-generator "Direct link to Report Generator")

```
`classReportGeneratorPromptextendsMCPPrompt{ name ="report-generator"; description ="Generates formatted reports from data"; schema ={ data:{ type: z.object({ title: z.string(), sections: z.array(z.string()),}), description:"Report data structure",}, format:{ type: z.enum(["short","detailed"]), description:"Report format",},};asyncgenerateMessages({ data, format }){return[{ role:"user", content:{ type:"text", text:`Generate a ${format} report titled "${ data.title}" with the following sections: ${data.sections.join(", ")}`,},},];}}`
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

  * Learn about [Tools](/docs/Tools/tools-overview)
  * Learn about [Resources](/docs/Resources/resources-overview)
  * [Get Started](/docs/quickstart)



[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Prompts/overview.md)

[PreviousUS Treasury Fiscal Data Example](/docs/Examples/fiscal-data)[NextResources Overview](/docs/Resources/resources-overview)

  * [What are Prompts?](#what-are-prompts)
  * [Creating Prompts](#creating-prompts)
    * [Using the CLI](#using-the-cli)
    * [Prompt Structure](#prompt-structure)
  * [Advanced Features](#advanced-features)
    * [Using Resources in Prompts](#using-resources-in-prompts)
    * [Multi-step Prompts](#multi-step-prompts)
  * [Best Practices](#best-practices)
  * [Examples](#examples)
    * [Report Generator](#report-generator)
  * [Next Steps](#next-steps)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Resources/resources-overview

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](#)

  * [Examples](#)

  * [Prompts](#)

  * [Resources](#)

    * [Resources Overview](/docs/Resources/resources-overview)
  * [Tools](#)

  * [Transports](#)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Resources
  * Resources Overview



On this page

# Resources

What are Resources?

Resources are data sources that AI models can read or subscribe to. Think of them as a way to provide context, data, or state to your AI interactions!

## Understanding Resources[​](#understanding-resources "Direct link to Understanding Resources")

Resources can be:

  * Files
  * API endpoints
  * Database queries
  * Real-time data streams
  * Configuration data



Here's a simple example:

```
`import{MCPResource}from"mcp-framework";classConfigResourceextendsMCPResource{ uri ="resource://config"; name ="Configuration"; description ="System configuration settings"; mimeType ="application/json";asyncread(){return[{ uri:this.uri, mimeType:this.mimeType, text:JSON.stringify({ version:"1.0.0", environment:"production", features:["analytics","reporting"],}),},];}}`
```

## Creating Resources[​](#creating-resources "Direct link to Creating Resources")

### Using the CLI[​](#using-the-cli "Direct link to Using the CLI")

```
`mcp add resource my-resource`
```

This creates a new resource in `src/resources/MyResource.ts`.

### Resource Structure[​](#resource-structure "Direct link to Resource Structure")

Every resource has:

  1. **Metadata**



```
`uri ="resource://my-data";name ="My Data Resource";description ="Provides access to my data";mimeType ="application/json";`
```

  1. **Read Method**



```
`asyncread():Promise<ResourceContent[]>{// Fetch or generate your datareturn[{ uri:this.uri, mimeType:this.mimeType, text:JSON.stringify(data)}];}`
```

## Resource Types[​](#resource-types "Direct link to Resource Types")

### Static Resources[​](#static-resources "Direct link to Static Resources")

```
`classDocumentationResourceextendsMCPResource{ uri ="resource://docs"; name ="Documentation"; mimeType ="text/markdown";asyncread(){return[{ uri:this.uri, mimeType:this.mimeType, text:"# API Documentation\n\nWelcome to our API...",},];}}`
```

### Dynamic Resources[​](#dynamic-resources "Direct link to Dynamic Resources")

```
`classMarketDataResourceextendsMCPResource{ uri ="resource://market-data"; name ="Market Data"; mimeType ="application/json";asyncread(){const data =awaitthis.fetch("https://api.market.com/latest");return[{ uri:this.uri, mimeType:this.mimeType, text:JSON.stringify(data),},];}}`
```

### Real-time Resources[​](#real-time-resources "Direct link to Real-time Resources")

Real-time Updates

Use subscription methods to handle real-time data streams!

```
`classStockTickerResourceextendsMCPResource{ uri ="resource://stock-ticker"; name ="Stock Ticker"; mimeType ="application/json";private ws:WebSocket|null=null;asyncsubscribe(){this.ws=newWebSocket("wss://stocks.example.com");this.ws.on("message",this.handleUpdate);}asyncunsubscribe(){if(this.ws){this.ws.close();this.ws=null;}}asyncread(){const latestData =awaitthis.getLatestStockData();return[{ uri:this.uri, mimeType:this.mimeType, text:JSON.stringify(latestData),},];}}`
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

  1. **URI Naming**



```
`uri ="resource://domain/type/identifier";// Example: "resource://finance/stocks/AAPL"`
```

  1. **Error Handling**



```
`asyncread(){try{const data =awaitthis.fetchData();return[{ uri:this.uri, mimeType:this.mimeType, text:JSON.stringify(data)}];}catch(error){thrownewError(`Failed to read resource: ${error.message}`);}}`
```

  1. **Caching**



```
`classCachedResourceextendsMCPResource{private cache:any=null;private lastFetch:number=0;privateTTL=60000;// 1 minuteasyncread(){if(this.cache&&Date.now()-this.lastFetch<this.TTL){returnthis.cache;}const data =awaitthis.fetchFreshData();this.cache= data;this.lastFetch=Date.now();return data;}}`
```

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Combining with Tools[​](#combining-with-tools "Direct link to Combining with Tools")

```
`classDataResourceextendsMCPResource{ uri ="resource://data"; name ="Data Store";asyncread(){return[{ uri:this.uri, mimeType:"application/json", text:JSON.stringify(awaitthis.getData()),},];}}classDataProcessorextendsMCPTool{asyncexecute(input){const resource =newDataResource();const[data]=await resource.read();returnthis.processData(JSON.parse(data.text));}}`
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

  * Learn about [Tools](/docs/Tools/tools-overview)
  * Learn about [Prompts](/docs/Prompts/prompts-overview)
  * [Get Started](/docs/quickstart)



[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Resources/overview.md)

[PreviousPrompts Overview](/docs/Prompts/prompts-overview)[NextTools Overview](/docs/Tools/tools-overview)

  * [Understanding Resources](#understanding-resources)
  * [Creating Resources](#creating-resources)
    * [Using the CLI](#using-the-cli)
    * [Resource Structure](#resource-structure)
  * [Resource Types](#resource-types)
    * [Static Resources](#static-resources)
    * [Dynamic Resources](#dynamic-resources)
    * [Real-time Resources](#real-time-resources)
  * [Best Practices](#best-practices)
  * [Advanced Usage](#advanced-usage)
    * [Combining with Tools](#combining-with-tools)
  * [Next Steps](#next-steps)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Tools/tools-overview

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

    * [Tools Overview](/docs/Tools/tools-overview)
    * [API Integration](/docs/Tools/api-integration)
  * [Transports](/docs/Transports/transports-overview)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Tools
  * Tools Overview



On this page

# Building Tools with MCP Framework

Power of Tools

Tools are the powerhouse of your MCP server - they let AI models interact with external services, process data, and perform complex operations with type safety!

## What is a Tool?[​](#what-is-a-tool "Direct link to What is a Tool?")

A tool is a MCP class that defines:

  * What inputs it accepts
  * What it does with those inputs
  * What it returns to the AI model



Here's a simple example:

```
`import{MCPTool}from"mcp-framework";import{ z }from"zod";interfaceGreetingInput{ name:string; language:string;}classGreetingToolextendsMCPTool<GreetingInput>{ name ="greeting"; description ="Generate a greeting in different languages"; schema ={ name:{ type: z.string(), description:"Name to greet",}, language:{ type: z.enum(["en","es","fr"]), description:"Language code (en, es, fr)",},};asyncexecute({ name, language }){const greetings ={ en:`Hello ${name}!`, es:`¡Hola ${name}!`, fr:`Bonjour ${name}!`,};return greetings[language];}}`
```

## Creating Tools[​](#creating-tools "Direct link to Creating Tools")

### Using the CLI[​](#using-the-cli "Direct link to Using the CLI")

The fastest way to create a new tool:

```
`mcp add tool my-tool`
```

This generates a tool template in `src/tools/MyTool.ts`.

### Manual Creation[​](#manual-creation "Direct link to Manual Creation")

  1. Create a new TypeScript file in `src/tools/`
  2. Extend the `MCPTool` class
  3. Define your interface and implementation



## Tool Architecture[​](#tool-architecture "Direct link to Tool Architecture")

Every tool has three main parts:

### 1. Input Schema[​](#1-input-schema "Direct link to 1. Input Schema")

```
`schema ={ email:{ type: z.string().email(), description:"User's email address",}, count:{ type: z.number().min(1), description:"Number of items to process",},};`
```

### 2. Metadata[​](#2-metadata "Direct link to 2. Metadata")

```
`name ="email-sender";description ="Sends emails to specified addresses";`
```

### 3. Execution Logic[​](#3-execution-logic "Direct link to 3. Execution Logic")

```
`asyncexecute(input:MyInput){// Your tool's core functionalityreturn result;}`
```

## Type Safety[​](#type-safety "Direct link to Type Safety")

Type Safety First

MCP Framework leverages TypeScript and Zod to provide end-to-end type safety!

```
`interfaceDataInput{ userId:number; fields:string[];}classDataToolextendsMCPTool<DataInput>{ schema ={ userId:{ type: z.number(), description:"User ID to fetch data for",}, fields:{ type: z.array(z.string()), description:"Fields to include in response",},};}`
```

## Error Handling[​](#error-handling "Direct link to Error Handling")

Tools should handle errors gracefully:

```
`asyncexecute(input:MyInput){try{const result =awaitthis.processData(input);return result;}catch(error){if(error.code==='NETWORK_ERROR'){thrownewError('Unable to reach external service');}thrownewError(`Operation failed: ${error.message}`);}}`
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

Pro Tips

Following these practices will make your tools more reliable and maintainable!

  1. **Clear Names**

```
`name ="fetch-user-data";// Goodname ="fud";// Bad`
```

  2. **Detailed Descriptions**

Descriptions are also read by the LLMs - so make sure to make them detailed

```
`description ="Fetches user data including profile, preferences, and settings";`
```

  3. **Descriptive Input Validation**

```
`schema ={ age:{ type: z.number().min(0).max(150), description:"User's age (0-150)",},};`
```




## Next Steps[​](#next-steps "Direct link to Next Steps")

  * Learn about [API Integration](/docs/Tools/api-integration)
  * Learn about [Prompts](/docs/Prompts/prompts-overview)
  * Learn about [Resources](/docs/Resources/resources-overview)



[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Tools/overview.md)

[PreviousResources Overview](/docs/Resources/resources-overview)[NextAPI Integration](/docs/Tools/api-integration)

  * [What is a Tool?](#what-is-a-tool)
  * [Creating Tools](#creating-tools)
    * [Using the CLI](#using-the-cli)
    * [Manual Creation](#manual-creation)
  * [Tool Architecture](#tool-architecture)
    * [1. Input Schema](#1-input-schema)
    * [2. Metadata](#2-metadata)
    * [3. Execution Logic](#3-execution-logic)
  * [Type Safety](#type-safety)
  * [Error Handling](#error-handling)
  * [Best Practices](#best-practices)
  * [Next Steps](#next-steps)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/quickstart

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Quickstart



On this page

# Quickstart

Let's create a simple MCP server with a basic tool. This guide will walk you through creating a weather information tool.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Make sure you have `mcp-framework` installed globally with npm:

```
`npm i -g mcp-framework`
```

## Create a New Project[​](#create-a-new-project "Direct link to Create a New Project")

First, create a new MCP server project:

```
`mcp create weather-mcp-servercd weather-mcp-server`
```

## Add a Weather Tool[​](#add-a-weather-tool "Direct link to Add a Weather Tool")

Use the CLI to create a new tool:

```
`mcp add tool weather`
```

This creates `src/tools/WeatherTool.ts` Let's modify it to handle weather requests:

```
`import{MCPTool}from"mcp-framework";import{ z }from"zod";interfaceWeatherInput{ city:string;}classWeatherToolextendsMCPTool<WeatherInput>{ name ="weather"; description ="Get weather information for a city"; schema ={ city:{ type: z.string(), description:"City name to get weather for",},};asyncexecute({ city }:WeatherInput){// In a real scenario, this would call a weather API// For now, we return this sample datareturn{ city, temperature:22, condition:"Sunny", humidity:45,};}}exportdefaultWeatherTool;`
```

## Build your project[​](#build-your-project "Direct link to Build your project")

```
`# Build the projectnpm run build`
```

## Choose a Transport[​](#choose-a-transport "Direct link to Choose a Transport")

MCP Framework supports two types of transports:

  1. **STDIO Transport** (Default): Perfect for CLI tools and local integrations. This is what we'll use with Claude Desktop.
  2. **SSE Transport** : Ideal for web applications and distributed systems.



For this quickstart, we'll use the default STDIO transport. To learn more about transports, check out:

  * [Transport Overview](/docs/Transports/transports-overview)
  * [STDIO Transport](/docs/Transports/stdio-transport)
  * [SSE Transport](/docs/Transports/sse)



## Use the Tool[​](#use-the-tool "Direct link to Use the Tool")

You can test your tool using the Claude Desktop client. Add this to your Claude Desktop config:

**MacOS** : `~/Library/Application Support/Claude/claude_desktop_config.json` **Windows** : `%APPDATA%/Claude/claude_desktop_config.json`

```
`{"mcpServers":{"weather-mcp-server":{"command":"node","args":["/absolute/path/to/weather-mcp-server/dist/index.js"]}}}`
```

Now you can ask Claude to use your weather tool:

```
`Could you check the weather in London using the weather tool?`
```

## What's Next?[​](#whats-next "Direct link to What's Next?")

The example above shows a basic tool implementation. In practice, you might want to:

  1. Add real API integration
  2. Include error handling
  3. Add more weather-related tools
  4. Create resources for caching
  5. Define prompts for common queries
  6. Consider using SSE transport for web integration



Check out our [US Treasury Data Example](https://github.com/QuantGeekDev/fiscal-data-mcp) for a more complete implementation.

### Next Steps[​](#next-steps "Direct link to Next Steps")

  * Learn more about [Tools](/docs/Tools/tools-overview)
  * Learn about [Resources](/docs/Resources/resources-overview)
  * Understand [Prompts](/docs/Prompts/prompts-overview)
  * Explore [Transports](/docs/Transports/transports-overview)
  * Set up [Debugging](/docs/debugging)



[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/quickstart.md)

[PreviousInstallation](/docs/installation)[NextDebugging](/docs/debugging)

  * [Prerequisites](#prerequisites)
  * [Create a New Project](#create-a-new-project)
  * [Add a Weather Tool](#add-a-weather-tool)
  * [Build your project](#build-your-project)
  * [Choose a Transport](#choose-a-transport)
  * [Use the Tool](#use-the-tool)
  * [What's Next?](#whats-next)
    * [Next Steps](#next-steps)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Transports/stdio-transport

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

    * [Transport Overview](/docs/Transports/transports-overview)
    * [STDIO Transport](/docs/Transports/stdio-transport)
    * [SSE Transport](/docs/Transports/sse)
  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Transports
  * STDIO Transport



On this page

# STDIO Transport

The STDIO transport is the default transport mechanism in MCP Framework. It uses standard input/output streams for communication between the client and server.

## Overview[​](#overview "Direct link to Overview")

STDIO transport is ideal for:

  * CLI tools and applications
  * Local process communication
  * Simple integrations without network requirements
  * Development and testing scenarios



## How It Works[​](#how-it-works "Direct link to How It Works")

The STDIO transport:

  1. Uses standard input (stdin) to receive messages from the client
  2. Uses standard output (stdout) to send messages to the client
  3. Implements JSON-RPC 2.0 protocol for message formatting
  4. Maintains a direct, synchronous communication channel



## Features[​](#features "Direct link to Features")

  * **Simplicity** : No network configuration required
  * **Performance** : Direct process communication with minimal overhead
  * **Reliability** : Guaranteed message delivery within the same process
  * **Security** : Inherent security through process isolation
  * **Debugging** : Easy to debug with direct console output



## Implementation[​](#implementation "Direct link to Implementation")

```
`import{MCPServer}from"mcp-framework";// STDIO is the default transportconst server =newMCPServer();// Or explicitly specify STDIO transportconst server =newMCPServer({ transport:{ type:"stdio"}});await server.start();`
```

## Use Cases[​](#use-cases "Direct link to Use Cases")

### CLI Tools[​](#cli-tools "Direct link to CLI Tools")

STDIO transport is perfect for CLI tools where the MCP server runs as part of the command-line application:

```
`#!/usr/bin/env nodeimport{MCPServer}from"mcp-framework";asyncfunctionmain(){const server =newMCPServer();await server.start();}main().catch(console.error);`
```

### Local Development[​](#local-development "Direct link to Local Development")

During development, STDIO transport provides a simple way to test and debug your MCP tools:

```
`import{MCPServer}from"mcp-framework";const server =newMCPServer({ name:"dev-server", version:"1.0.0"});await server.start();`
```

## Limitations[​](#limitations "Direct link to Limitations")

While STDIO transport is simple and efficient, it has some limitations:

  * Single client connection only
  * No network accessibility
  * No authentication mechanism
  * Process-bound lifecycle



For scenarios requiring multiple clients, network access, or authentication, consider using [SSE Transport](/docs/Transports/sse) instead.

## Best Practices[​](#best-practices "Direct link to Best Practices")

  1. **Error Handling**

     * Implement proper error handling for process termination
     * Handle SIGINT and SIGTERM signals appropriately
  2. **Logging**

     * Use stderr for logging to avoid interfering with transport messages
     * Consider implementing a proper logging strategy
  3. **Process Management**

     * Properly close the server on process exit
     * Handle cleanup operations in shutdown hooks



## Example Implementation[​](#example-implementation "Direct link to Example Implementation")

Here's a complete example showing best practices:

```
`import{MCPServer}from"mcp-framework";classMyMCPServer{private server:MCPServer;constructor(){this.server=newMCPServer({ name:"my-mcp-server", version:"1.0.0", transport:{ type:"stdio"}});// Handle process signals process.on('SIGINT',()=>this.shutdown()); process.on('SIGTERM',()=>this.shutdown());}asyncstart(){try{awaitthis.server.start();console.error('Server started successfully');// Use stderr for logging}catch(error){console.error('Failed to start server:', error); process.exit(1);}}privateasyncshutdown(){console.error('Shutting down...');try{awaitthis.server.stop(); process.exit(0);}catch(error){console.error('Error during shutdown:', error); process.exit(1);}}}// Start the servernewMyMCPServer().start().catch(console.error);`
```

[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Transports/stdio.md)

[PreviousTransport Overview](/docs/Transports/transports-overview)[NextSSE Transport](/docs/Transports/sse)

  * [Overview](#overview)
  * [How It Works](#how-it-works)
  * [Features](#features)
  * [Implementation](#implementation)
  * [Use Cases](#use-cases)
    * [CLI Tools](#cli-tools)
    * [Local Development](#local-development)
  * [Limitations](#limitations)
  * [Best Practices](#best-practices)
  * [Example Implementation](#example-implementation)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Transports/sse

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

    * [Transport Overview](/docs/Transports/transports-overview)
    * [STDIO Transport](/docs/Transports/stdio-transport)
    * [SSE Transport](/docs/Transports/sse)
  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Transports
  * SSE Transport



On this page

# SSE Transport

The Server-Sent Events (SSE) transport enables HTTP-based communication between the MCP server and clients. It uses SSE for server-to-client messages and HTTP POST for client-to-server messages.

## Configuration[​](#configuration "Direct link to Configuration")

The SSE transport supports various configuration options to customize its behavior:

```
`import{MCPServer}from"@modelcontextprotocol/mcp-framework";const server =newMCPServer({ transport:{ type:"sse", options:{ port:8080,// Port to listen on (default: 8080) endpoint:"/sse",// SSE endpoint path (default: "/sse") messageEndpoint:"/messages",// Message endpoint path (default: "/messages") maxMessageSize:"4mb",// Maximum message size (default: "4mb") headers:{// Custom headers for SSE responses"X-Custom-Header":"value"}, cors:{// CORS configuration allowOrigin:"*", allowMethods:"GET, POST, OPTIONS", allowHeaders:"Content-Type, Authorization, x-api-key", exposeHeaders:"Content-Type, Authorization, x-api-key", maxAge:"86400"}, auth:{// Authentication configuration provider: authProvider, endpoints:{ sse:true,// Require auth for SSE connections messages:true// Require auth for messages}}}}});`
```

### Port Configuration[​](#port-configuration "Direct link to Port Configuration")

The `port` option specifies which port the SSE server should listen on. Default is 8080.

### Endpoints[​](#endpoints "Direct link to Endpoints")

  * `endpoint`: The path for the SSE connection endpoint (default: "/sse")
  * `messageEndpoint`: The path for receiving messages via POST (default: "/messages")



### Message Size Limit[​](#message-size-limit "Direct link to Message Size Limit")

The `maxMessageSize` option controls the maximum allowed size for incoming messages. Accepts string values like "4mb", "1kb", etc.

### Custom Headers[​](#custom-headers "Direct link to Custom Headers")

You can specify custom headers to be included in SSE responses:

```
`headers:{"X-Custom-Header":"value","Cache-Control":"no-cache"}`
```

### CORS Configuration[​](#cors-configuration "Direct link to CORS Configuration")

The SSE transport includes comprehensive CORS support with the following options:

```
`cors:{ allowOrigin:"*",// Access-Control-Allow-Origin allowMethods:"GET, POST, OPTIONS",// Access-Control-Allow-Methods allowHeaders:"Content-Type, Authorization, x-api-key",// Access-Control-Allow-Headers exposeHeaders:"Content-Type, Authorization, x-api-key",// Access-Control-Expose-Headers maxAge:"86400"// Access-Control-Max-Age}`
```

### Authentication[​](#authentication "Direct link to Authentication")

The SSE transport supports authentication through various providers. See the [Authentication](/docs/Authentication/overview) documentation for details.

```
`auth:{ provider: authProvider,// Authentication provider instance endpoints:{ sse:true,// Require auth for SSE connections messages:true// Require auth for messages}}`
```

## Connection Management[​](#connection-management "Direct link to Connection Management")

### Keep-Alive[​](#keep-alive "Direct link to Keep-Alive")

The SSE transport automatically manages connection keep-alive:

  * Sends keep-alive messages every 15 seconds
  * Includes ping messages with timestamps
  * Optimizes socket settings for long-lived connections



### Session Management[​](#session-management "Direct link to Session Management")

Each SSE connection is assigned a unique session ID that must be included in message requests:

  1. Client establishes SSE connection
  2. Server sends endpoint URL with session ID
  3. Client uses this URL for sending messages



### Error Handling[​](#error-handling "Direct link to Error Handling")

The transport includes robust error handling:

  * Connection errors
  * Message parsing errors
  * Authentication failures
  * Size limit exceeded errors



Error responses include detailed information:

```
`{"jsonrpc":"2.0","id":null,"error":{"code":-32000,"message":"Error message","data":{"method":"method_name","sessionId":"session_id","connectionActive":true,"type":"message_handler_error"}}}`
```

## Security Considerations[​](#security-considerations "Direct link to Security Considerations")

  1. **HTTPS** : Always use HTTPS in production environments
  2. **Authentication** : Enable authentication for both SSE and message endpoints
  3. **CORS** : Configure appropriate CORS settings for your environment
  4. **Message Size** : Set appropriate message size limits
  5. **Rate Limiting** : Implement rate limiting for production use



## Client Implementation[​](#client-implementation "Direct link to Client Implementation")

Here's an example of how to implement a client for the SSE transport:

```
`// Establish SSE connectionconst eventSource =newEventSource('http://localhost:8080/sse');// Handle endpoint URLeventSource.addEventListener('endpoint',(event)=>{const messageEndpoint = event.data;// Store messageEndpoint for sending messages});// Handle messageseventSource.addEventListener('message',(event)=>{const message =JSON.parse(event.data);// Process message});// Send messageasyncfunctionsendMessage(message){const response =awaitfetch(messageEndpoint,{ method:'POST', headers:{'Content-Type':'application/json','Authorization':'Bearer your-token'// If using authentication}, body:JSON.stringify(message)});if(!response.ok){thrownewError(`HTTP error! status: ${response.status}`);}}`
```

[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Transports/sse.md)

[PreviousSTDIO Transport](/docs/Transports/stdio-transport)[NextServer Configuration](/docs/server-configuration)

  * [Configuration](#configuration)
    * [Port Configuration](#port-configuration)
    * [Endpoints](#endpoints)
    * [Message Size Limit](#message-size-limit)
    * [Custom Headers](#custom-headers)
    * [CORS Configuration](#cors-configuration)
    * [Authentication](#authentication)
  * [Connection Management](#connection-management)
    * [Keep-Alive](#keep-alive)
    * [Session Management](#session-management)
    * [Error Handling](#error-handling)
  * [Security Considerations](#security-considerations)
  * [Client Implementation](#client-implementation)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/debugging

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](#)

  * [Examples](#)

  * [Prompts](#)

  * [Resources](#)

  * [Tools](#)

  * [Transports](#)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Debugging



On this page

# Debugging MCP Servers

tip

The Model Context Protocol provides an open-source Inspector tool that makes debugging your MCP servers easy!

## MCP Inspector[​](#mcp-inspector "Direct link to MCP Inspector")

The MCP Inspector is an external developer tool maintained by the Model Context Protocol team that helps you test and debug MCP servers. It provides a user interface for interacting with your server and testing your tools, resources, and prompts.

### Using the Inspector[​](#using-the-inspector "Direct link to Using the Inspector")

You can run the Inspector directly through `npx` without installation:

```
`npx @modelcontextprotocol/inspector <path-to-your-server>`
```

For example, if you've built your MCP Framework server:

```
`# First build your servernpm run build# Then run the inspectornpx @modelcontextprotocol/inspector dist/index.js`
```

### Customizing Ports[​](#customizing-ports "Direct link to Customizing Ports")

The Inspector runs both a client UI (default port 5173) and an MCP proxy server (default port 3000). You can customize these ports if needed:

```
`CLIENT_PORT=8080 SERVER_PORT=9000 npx @modelcontextprotocol/inspector dist/index.js`
```

## Using the Inspector[​](#using-the-inspector-1 "Direct link to Using the Inspector")

### Server Connection[​](#server-connection "Direct link to Server Connection")

When you open the Inspector in your browser, you'll see:

  * Connection status to your server
  * Server capabilities
  * Server metadata



### Testing Tools[​](#testing-tools "Direct link to Testing Tools")

The Tools tab allows you to:

  * View all registered tools
  * See tool schemas and descriptions
  * Test tools with custom inputs
  * View execution results



Example testing workflow:

  1. Select your tool from the list
  2. Enter test inputs in the JSON editor
  3. Execute the tool
  4. Review the response



### Inspecting Resources[​](#inspecting-resources "Direct link to Inspecting Resources")

The Resources tab enables you to:

  * Browse available resources
  * View resource metadata
  * Test resource content retrieval
  * Test subscriptions (if supported)



### Testing Prompts[​](#testing-prompts "Direct link to Testing Prompts")

In the Prompts tab, you can:

  * View available prompt templates
  * Test prompts with different arguments
  * Preview generated messages



## Framework Logging[​](#framework-logging "Direct link to Framework Logging")

MCP Framework includes built-in logging that integrates well with the Inspector:

```
`import{ logger }from"mcp-framework";classMyToolextendsMCPTool{asyncexecute(input){ logger.info("Starting execution");try{const result =awaitthis.process(input); logger.info("Execution successful");return result;}catch(error){ logger.error("Execution failed:", error);throw error;}}}`
```

### Log Levels[​](#log-levels "Direct link to Log Levels")

```
`logger.debug("Detailed information");logger.info("General information");logger.warn("Warning messages");logger.error("Error messages");`
```

## Development Workflow[​](#development-workflow "Direct link to Development Workflow")

  1. **Start Development**

     * Launch your server with the Inspector
     * Verify basic connectivity
     * Check that your tools are listed
  2. **Iterative Testing**

     * Make changes to your server
     * Rebuild (`npm run build`)
     * Reconnect the Inspector
     * Test the changes
     * Monitor the logs
  3. **Test Edge Cases**

     * Try invalid inputs
     * Test error handling
     * Check concurrent operations



## Common Issues[​](#common-issues "Direct link to Common Issues")

### Tool Not Found[​](#tool-not-found "Direct link to Tool Not Found")

  * Ensure the tool is properly exported
  * Check that the tool name matches
  * Verify the tool is being loaded by the server



### Resource Errors[​](#resource-errors "Direct link to Resource Errors")

  * Check resource URI formatting
  * Verify resource read implementation
  * Test subscription cleanup



### Prompt Issues[​](#prompt-issues "Direct link to Prompt Issues")

  * Validate prompt arguments
  * Check message generation
  * Verify resource references



## Best Practices[​](#best-practices "Direct link to Best Practices")

  1. **Use Descriptive Logging**



```
`logger.info(`Processing request for user ${userId}`);logger.error(`Failed to fetch data: ${error.message}`);`
```

  1. **Handle Errors Gracefully**



```
`try{// Your operation}catch(error){ logger.error(`Operation failed: ${error.message}`);thrownewError(`Failed to complete operation: ${error.message}`);}`
```

  1. **Monitor Performance**



```
`const start =Date.now();// ... operation ...logger.debug(`Operation took ${Date.now()- start}ms`);`
```

[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/debugging.md)

[PreviousQuickstart](/docs/quickstart)[NextAuthentication](/docs/Authentication/overview)

  * [MCP Inspector](#mcp-inspector)
    * [Using the Inspector](#using-the-inspector)
    * [Customizing Ports](#customizing-ports)
  * [Using the Inspector](#using-the-inspector-1)
    * [Server Connection](#server-connection)
    * [Testing Tools](#testing-tools)
    * [Inspecting Resources](#inspecting-resources)
    * [Testing Prompts](#testing-prompts)
  * [Framework Logging](#framework-logging)
    * [Log Levels](#log-levels)
  * [Development Workflow](#development-workflow)
  * [Common Issues](#common-issues)
    * [Tool Not Found](#tool-not-found)
    * [Resource Errors](#resource-errors)
    * [Prompt Issues](#prompt-issues)
  * [Best Practices](#best-practices)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/server-configuration

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](/docs/Authentication/overview)

  * [Examples](/docs/Examples/fiscal-data)

  * [Prompts](/docs/Prompts/prompts-overview)

  * [Resources](/docs/Resources/resources-overview)

  * [Tools](/docs/Tools/tools-overview)

  * [Transports](/docs/Transports/transports-overview)

  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Server Configuration



On this page

# Server Configuration

The MCP Framework provides extensive configuration options for customizing your server's behavior. This guide covers all available configuration options and best practices.

## Basic Configuration[​](#basic-configuration "Direct link to Basic Configuration")

When creating a new MCP server, you can provide configuration options:

```
`import{MCPServer}from"@modelcontextprotocol/mcp-framework";const server =newMCPServer({ name:"my-mcp-server",// Server name version:"1.0.0",// Server version basePath:"./dist",// Base path for tools/prompts/resources transport:{// Transport configuration type:"sse", options:{// Transport-specific options}}});`
```

## Server Name and Version[​](#server-name-and-version "Direct link to Server Name and Version")

The server name and version are used to identify your MCP server:

```
`const server =newMCPServer({ name:"my-mcp-server",// Default: package.json name or "unnamed-mcp-server" version:"1.0.0"// Default: package.json version or "0.0.0"});`
```

If not provided, the server will attempt to read these values from your project's package.json file.

## Base Path[​](#base-path "Direct link to Base Path")

The `basePath` option specifies where the server should look for tools, prompts, and resources:

```
`const server =newMCPServer({ basePath:"./dist"// Default: join(process.cwd(), 'dist')});`
```

The server will look for:

  * Tools in `${basePath}/tools`
  * Prompts in `${basePath}/prompts`
  * Resources in `${basePath}/resources`



## Transport Configuration[​](#transport-configuration "Direct link to Transport Configuration")

The transport configuration determines how clients will communicate with your server:

```
`const server =newMCPServer({ transport:{ type:"sse",// "sse" or "stdio" options:{// Transport-specific options port:8080, endpoint:"/sse",// ... other options}}});`
```

See the transport-specific documentation for detailed configuration options:

  * [SSE Transport](/docs/Transports/sse)
  * [STDIO Transport](/docs/Transports/stdio-transport)



## Server Capabilities[​](#server-capabilities "Direct link to Server Capabilities")

The server automatically detects and enables capabilities based on your project structure:

```
`interfaceServerCapabilities{ tools?:{ enabled:true;}; schemas?:{ enabled:true;}; prompts?:{ enabled:true;}; resources?:{ enabled:true;};}`
```

  * Tools capability is always enabled
  * Prompts capability is enabled if prompts are found in the prompts directory
  * Resources capability is enabled if resources are found in the resources directory



## Server Lifecycle[​](#server-lifecycle "Direct link to Server Lifecycle")

### Starting the Server[​](#starting-the-server "Direct link to Starting the Server")

```
`await server.start();`
```

The start process:

  1. Loads tools, prompts, and resources
  2. Detects capabilities
  3. Sets up request handlers
  4. Initializes the transport
  5. Starts listening for connections



### Stopping the Server[​](#stopping-the-server "Direct link to Stopping the Server")

```
`await server.stop();`
```

The stop process:

  1. Closes active connections
  2. Stops the transport
  3. Cleans up resources
  4. Exits gracefully



The server also handles SIGINT signals (Ctrl+C) for graceful shutdown.

## Logging[​](#logging "Direct link to Logging")

The server uses a built-in logger that can be imported and configured:

```
`import{ logger }from"@modelcontextprotocol/mcp-framework";// Log levels: debug, info, warn, errorlogger.debug("Debug message");logger.info("Info message");logger.warn("Warning message");logger.error("Error message");`
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

  1. **Project Structure**

     * Keep tools, prompts, and resources in separate directories
     * Use TypeScript for better type safety
     * Follow the naming conventions for each component
  2. **Configuration**

     * Use environment variables for sensitive values
     * Set appropriate base paths for your deployment
     * Configure proper authentication in production
  3. **Error Handling**

     * Implement proper error handling in your tools
     * Use the logger for debugging and monitoring
     * Handle transport errors appropriately
  4. **Security**

     * Enable authentication in production
     * Use HTTPS for SSE transport
     * Set appropriate CORS settings
     * Implement rate limiting
  5. **Performance**

     * Keep message sizes reasonable
     * Implement proper cleanup in tools
     * Monitor server resources



## Example Configuration[​](#example-configuration "Direct link to Example Configuration")

Here's a complete example with all configuration options:

```
`import{MCPServer,APIKeyAuthProvider}from"@modelcontextprotocol/mcp-framework";const server =newMCPServer({ name:"my-mcp-server", version:"1.0.0", basePath:"./dist", transport:{ type:"sse", options:{ port:8080, endpoint:"/sse", messageEndpoint:"/messages", maxMessageSize:"4mb", headers:{"X-Custom-Header":"value"}, cors:{ allowOrigin:"*", allowMethods:"GET, POST, OPTIONS", allowHeaders:"Content-Type, Authorization, x-api-key", exposeHeaders:"Content-Type, Authorization, x-api-key", maxAge:"86400"}, auth:{ provider:newAPIKeyAuthProvider({ keys:["your-api-key"]}), endpoints:{ sse:true, messages:true}}}}});// Start the serverawait server.start();// Handle shutdownprocess.on('SIGINT',async()=>{await server.stop();});`
```

[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/server-configuration.md)

[PreviousSSE Transport](/docs/Transports/sse)

  * [Basic Configuration](#basic-configuration)
  * [Server Name and Version](#server-name-and-version)
  * [Base Path](#base-path)
  * [Transport Configuration](#transport-configuration)
  * [Server Capabilities](#server-capabilities)
  * [Server Lifecycle](#server-lifecycle)
    * [Starting the Server](#starting-the-server)
    * [Stopping the Server](#stopping-the-server)
  * [Logging](#logging)
  * [Best Practices](#best-practices)
  * [Example Configuration](#example-configuration)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---



## Untitled Page
URL: https://mcp-framework.com/docs/Transports/transports-overview

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![MCP Framework Logo](/img/logo.svg)**MCP Framework**](/)[Documentation](/docs/introduction)

[GitHub](https://github.com/QuantGeekDev/mcp-framework)

  * [Introduction](/docs/introduction)
  * [Installation](/docs/installation)
  * [Quickstart](/docs/quickstart)
  * [Debugging](/docs/debugging)
  * [Authentication](#)

  * [Examples](#)

  * [Prompts](#)

  * [Resources](#)

  * [Tools](#)

  * [Transports](#)

    * [Transport Overview](/docs/Transports/transports-overview)
    * [STDIO Transport](/docs/Transports/stdio-transport)
    * [SSE Transport](/docs/Transports/sse)
  * [Server Configuration](/docs/server-configuration)



  * [](/)
  * Transports
  * Transport Overview



On this page

# Transport Overview

MCP Framework supports multiple transport mechanisms for communication between the client and server. Each transport type has its own characteristics, advantages, and use cases.

## Available Transports[​](#available-transports "Direct link to Available Transports")

The framework currently supports two transport types:

  * **STDIO Transport** : The default transport that uses standard input/output streams
  * **SSE Transport** : Server-Sent Events based transport that enables HTTP/web-based communication



## Comparison[​](#comparison "Direct link to Comparison")

Feature| STDIO Transport| SSE Transport  
---|---|---  
Protocol| Standard I/O streams| HTTP/SSE  
Connection| Direct process communication| Network-based  
Authentication| Not applicable| Supports JWT and API Key  
Use Case| CLI tools, local integrations| Web applications, distributed systems  
Configuration| Minimal| Configurable (port, endpoints, auth)  
Scalability| Single process| Multiple clients  
  
## Choosing a Transport[​](#choosing-a-transport "Direct link to Choosing a Transport")

Choose your transport based on your application's needs:

  * Use **STDIO Transport** when:

    * Building CLI tools
    * Need direct process communication
    * Working with local integrations
    * Want minimal configuration
  * Use **SSE Transport** when:

    * Building web applications
    * Need network-based communication
    * Require authentication
    * Want to support multiple clients
    * Need to scale horizontally



## Configuration[​](#configuration "Direct link to Configuration")

### STDIO Transport (Default)[​](#stdio-transport-default "Direct link to STDIO Transport \(Default\)")

```
`const server =newMCPServer();// or explicitly:const server =newMCPServer({ transport:{ type:"stdio"}});`
```

### SSE Transport[​](#sse-transport "Direct link to SSE Transport")

```
`const server =newMCPServer({ transport:{ type:"sse", options:{ port:8080,// Optional (default: 8080) endpoint:"/sse",// Optional (default: "/sse") messageEndpoint:"/messages",// Optional (default: "/messages") auth:{// Optional authentication configuration}}}});`
```

For detailed information about each transport type, see:

  * [STDIO Transport](/docs/Transports/stdio-transport)
  * [SSE Transport](/docs/Transports/sse)



[Edit this page](https://github.com/QuantGeekDev/mcp-framework/tree/main/docs/Transports/overview.md)

[PreviousAPI Integration](/docs/Tools/api-integration)[NextSTDIO Transport](/docs/Transports/stdio-transport)

  * [Available Transports](#available-transports)
  * [Comparison](#comparison)
  * [Choosing a Transport](#choosing-a-transport)
  * [Configuration](#configuration)
    * [STDIO Transport (Default)](#stdio-transport-default)
    * [SSE Transport](#sse-transport)



Documentation

  * [Getting Started](/docs/introduction)



Community

  * [GitHub Discussions](https://github.com/QuantGeekDev/mcp-framework/discussions)
  * [Discord](https://discord.gg/kqjRdn3T)



More

  * [GitHub](https://github.com/QuantGeekDev/mcp-framework)



Copyright © 2025 Alex Andru 


---

