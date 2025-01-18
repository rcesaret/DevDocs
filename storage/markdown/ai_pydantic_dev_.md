# Skip to content
URL: https://ai.pydantic.dev#introduction

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev/

Showing documentation for the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Why use PydanticAI
URL: https://ai.pydantic.dev#why-use-pydanticai

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Hello World Example
URL: https://ai.pydantic.dev#hello-world-example

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Tools & Dependency Injection Example
URL: https://ai.pydantic.dev#tools-dependency-injection-example

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Instrumentation with Pydantic Logfire
URL: https://ai.pydantic.dev#instrumentation-with-pydantic-logfire

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Next Steps
URL: https://ai.pydantic.dev#next-steps

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Installation
URL: https://ai.pydantic.dev/install/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

PydanticAI is available on PyPI as so installation is as simple as:

This installs the package, core dependencies, and libraries required to use all
the models included in PydanticAI. If you want to use a specific model, you can
install the version of PydanticAI.

PydanticAI has an excellent (but completely optional) integration with to help
you view and understand agent runs.

To use Logfire with PydanticAI, install or with the optional group:

From there, follow the to configure Logfire.

We distribute the directory as a separate PyPI package () to make examples
extremely easy to customize and run.

To install examples, use the optional group:

To run the examples, follow instructions in the .

If you know which model you're going to use and want to avoid installing
superfluous packages, you can use the package. For example, if you're using just
, you would run:

has the following optional groups:

See the documentation for information on which optional dependencies are
required for each model.

You can also install dependencies for multiple models and use cases, for
example:

---

# Getting Help
URL: https://ai.pydantic.dev/help/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

If you need help getting started with PydanticAI or with advanced usage, the
following sources may be useful.

Join the channel in the to ask questions, get help, and chat about PydanticAI.
There's also channels for Pydantic, Logfire, and FastUI.

If you're on a Pro plan, you can also get a dedicated private slack collab
channel with us.

The are a great place to ask questions and give us feedback.

---

# Contributing
URL: https://ai.pydantic.dev/contributing/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

We'd love you to contribute to PydanticAI!

Clone your fork and cd into the repo directory

Install (version 0.4.30 or later) and

We use pipx here, for other options see:

Install , all dependencies and pre-commit hooks

We use to manage most commands you'll need to run.

For details on available commands, run:

To run code formatting, linting, static type checks, and tests with coverage
report generation, run:

To run the documentation page locally, run:

## Rules for adding new models to PydanticAI

To avoid an excessive workload for the maintainers of PydanticAI, we can't
accept all model contributions, so we're setting the following rules for when
we'll accept new models and when we won't. This should hopefully reduce the
chances of disappointment and wasted work.

  * To add a new model with an extra dependency, that dependency needs > 500k monthly downloads from PyPI consistently over 3 months or more
  * To add a new model which uses another models logic internally and has no extra dependencies, that model's GitHub org needs > 20k stars in total
  * For any other model that's just a custom URL and API key, we're happy to add a one-paragraph description with a link and instructions on the URL to use
  * For any other model that requires more logic, we recommend you release your own Python package , which depends on and implements a model that inherits from our ABC

If you're unsure about adding a model, please .

---

# Troubleshooting
URL: https://ai.pydantic.dev/troubleshooting/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Below are suggestions on how to fix some common errors you might encounter while
using PydanticAI. If the issue you're experiencing is not listed below or
addressed in the documentation, please feel free to ask in the or create an
issue on .

### `RuntimeError: This event loop is already running`

This error is caused by conflicts between the event loops in Jupyter notebook
and PydanticAI's. One way to manage these conflicts is by using . Namely, before
you execute any agent runs, do the following:

Note: This fix also applies to Google Colab.

### `UserError: API key must be provided or set in the [MODEL]_API_KEY
environment variable`

If you're running into issues with setting the API key for your model, visit the
page to learn more about how to set an environment variable and/or pass in an
argument.

---

# Agents
URL: https://ai.pydantic.dev/agents/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Agents are PydanticAI's primary interface for interacting with LLMs.

In some use cases a single Agent will control an entire application or
component, but multiple agents can also interact to embody more complex
workflows.

The class has full API documentation, but conceptually you can think of an agent
as a container for:

A set of instructions for the LLM written by the developer.  
---  
Functions that the LLM may call to get information while generating a response.  
The structured datatype the LLM must return at the end of a run, if specified.  
System prompt functions, tools, and result validators may all use dependencies
when they're run.  
Optional default LLM model associated with the agent. Can also be specified when
running the agent.  
Optional default model settings to help fine tune requests. Can also be
specified when running the agent.  
In typing terms, agents are generic in their dependency and result types, e.g.,
an agent which required dependencies of type and returned results of type would
have type . In practice, you shouldn't need to care about this, it should just
mean your IDE can tell you when you have the right type, and if you choose to
use it should work well with PydanticAI.

Here's a toy example of an agent that simulates a roulette wheel:

```

    
  
  
  
  
  
    'Use the `roulette_wheel` function to see if the '
    'customer has won based on the number they provide.'
  

        
"""check if the square is a winner"""

         

  
  'Put my money on square eighteen'



  'I bet five is the winner'

```

Agents are designed for reuse, like FastAPI Apps

Agents are intended to be instantiated once (frequently as module globals) and
reused throughout your application, similar to a small app or an .

There are three ways to run an agent:

  1. — a coroutine which returns a containing a completed response
  2. — a plain, synchronous function which returns a containing a completed response (internally, this just calls )
  3. — a coroutine which returns a , which contains methods to stream a response as an async iterable

Here's a simple example demonstrating all three:

```

  
  
  'What is the capital of Italy?'

  
     'What is the capital of France?'
  
  
    'What is the capital of the UK?'  
     
    

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

You can also pass messages from previous runs to continue a conversation or
provide context, as described in .

PydanticAI offers a structure to help you limit your usage (tokens and/or
requests) on model runs.

You can apply these settings by passing the argument to the functions.

Consider the following example, where we limit the number of response tokens:

```

  
  
  
  
  
  'What is the capital of Italy? Answer with just the city.'

  

Usage(requests=1, request_tokens=62, response_tokens=1, total_tokens=63,
details=None)

    
    'What is the capital of Italy? Answer with a paragraph.'
    
  
  
  
  #> Exceeded the response_tokens_limit of 10 (response_tokens=32)

```

Restricting the number of requests can be useful in preventing infinite loops or
excessive tool calling:

```

  
    
  
  



  Never ever coerce data to this type.

  

  
  
  
  'Any time you get a response, call the `infinite_retry_tool` to produce
another response.'



  
  

    
      
  
  
  
  #> The next request would exceed the request_limit of 3

```

This is especially relevant if you're registered a lot of tools, can be used to
prevent the model from choosing to make too many of these calls.

PydanticAI offers a structure to help you fine tune your requests. This
structure allows you to configure common parameters that influence the model's
behavior, such as , , , and more.

There are two ways to apply these settings: 1. Passing to functions via the
argument. This allows for fine-tuning on a per-request basis. 2. Setting during
initialization via the argument. These settings will be applied by default to
all subsequent run calls using said agent. However, provided during a specific
run call will override the agent's default settings.

For example, if you'd like to set the setting to to ensure less random behavior,
you can do the following:

```

  
  
  
  'What is the capital of Italy?'  

```

An agent might represent an entire conversation — there's no limit to how many
messages can be exchanged in a single run. However, a might also be composed of
multiple runs, especially if you need to maintain state between separate
interactions or API calls.

Here's an example of a conversation comprised of multiple runs:

```

  
  

  

#> Albert Einstein was a German-born theoretical physicist.

# Second run, passing previous messages

  
  'What was his most famous equation?'

#> Albert Einstein's most famous equation is (E = mc^2).

```

_(This example is complete, it can be run "as is")_

PydanticAI is designed to work well with static type checkers, like mypy and
pyright.

PydanticAI is designed to make type checking as useful as possible for you if
you choose to use it, but you don't have to use types everywhere all the time.

That said, because PydanticAI uses Pydantic, and Pydantic uses type hints as the
definition for schema and validation, some types (specifically type hints on
parameters to tools, and the arguments to ) are used at runtime.

We (the library developers) have messed up if type hints are confusing you more
than helping you, if you find this, please create an explaining what's annoying
you!

In particular, agents are generic in both the type of their dependencies and the
type of results they return, so you can use the type hints to ensure you're
using the right types.

Consider the following script with type mistakes:

```

  
    



  

  
  
  
  

     
  

    
  

  'Does their name start with "A"?'

```

Running on this will give the following output:

Running would identify the same issues.

System prompts might seem simple at first glance since they're just strings (or
sequences of strings that are concatenated), but crafting the right system
prompt is key to getting the model to behave as you want.

Generally, system prompts fall into two categories:

  1. : These are known when writing the code and can be defined via the parameter of the .
  2. : These depend in some way on context that isn't known until runtime, and should be defined via functions decorated with .

You can add both to a single agent; they're appended in the order they're
defined at runtime.

Here's an example using both types of system prompts:

```

  
    
  
  
  
  "Use the customer's name while replying to them."



    
  

    
  

  

#> Hello Frank, the date today is 2032-01-02.

```

_(This example is complete, it can be run "as is")_

Validation errors from both function tool parameter validation and can be passed
back to the model with a request to retry.

You can also raise from within a or to tell the model it should retry generating
a response.

  * The default retry count is but can be altered for the , a , or a .
  * You can access the current retry count from within a tool or result validator via .

```

  
     
  



  
  

  
  
  
  

      
"""Get a user's ID from their full name."""

  
  
  
    
     
     
      'No user found with name , remember to provide their full name'
    
  

  
  'Send a message to John Doe asking for coffee next week'

user_id=123 message='Hello John, would you be free for coffee sometime next
week? Let me know what works for you!'

```

If models behave unexpectedly (e.g., the retry limit is exceeded, or their API
returns ), agent runs will raise .

In these cases, can be used to access the messages exchanged during the run to
help diagnose the issue.

```

      
  

     
     
     
  
     

    
  
      'Please get me the volume of a box with size 6.'
     
     
    #> An error occurred: Tool exceeded max retries count of 1
     
    #> cause: ModelRetry('Please try again.')
     

            content='Please get me the volume of a box with size 6.',

  
    

```

_(This example is complete, it can be run "as is")_

If you call , , or more than once within a single context, will represent the
messages exchanged during the first call only.

---

# Models
URL: https://ai.pydantic.dev/models/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

PydanticAI is Model-agnostic and has built in support for the following model
providers:

  * Gemini via two different APIs: and 

See for more examples on how to use models such as , and that support the OpenAI
SDK.

You can also [add support for other
models](https://ai.pydantic.dev/models/<#implementing-custom-models>).

PydanticAI also comes with and for testing and development.

To use each model provider, you need to configure your local environment and
make sure you have the right packages installed.

To use OpenAI models, you need to either install , or install with the optional
group:

To use through their main API, go to and follow your nose until you find the
place to generate an API key.

Once you have the API key, you can set it as an environment variable:

You can then use by name:

Or initialise the model directly with just the model name:

If you don't want to or can't set the environment variable, you can pass it at
runtime via the :

also accepts a custom client via the , so you can customise the , , etc. as
defined in the .

You could also use the client to use the Azure OpenAI API.

To use models, you need to either install , or install with the optional group:

To use through their API, go to to generate an API key.

contains a list of available Anthropic models.

Once you have the API key, you can set it as an environment variable:

You can then use by name:

Or initialise the model directly with just the model name:

If you don't want to or can't set the environment variable, you can pass it at
runtime via the :

Google themselves refer to this API as the "hobby" API, I've received 503
responses from it a number of times. The API is easy to use and useful for
prototyping and simple demos, but I would not rely on it in production.

If you want to run Gemini models in production, you should use the described
below.

To use models, you just need to install or , no extra dependencies are required.

let's you use the Google's Gemini models through their , .

contains a list of available Gemini models that can be used through this
interface.

To use , go to and follow your nose until you find the place to generate an API
key.

Once you have the API key, you can set it as an environment variable:

You can then use by name:

The provider prefix represents the for s. is used with for s.

Or initialise the model directly with just the model name:

If you don't want to or can't set the environment variable, you can pass it at
runtime via the :

To run Google's Gemini models in production, you should use which uses the API.

contains a list of available Gemini models that can be used through this
interface.

To use , you need to either install , or install with the optional group:

This interface has a number of advantages over documented above:

  1. The VertexAI API is more reliably and marginally lower latency in our experience.
  2. You can with VertexAI to guarantee capacity.
  3. If you're running PydanticAI inside GCP, you don't need to set up authentication, it should "just work".
  4. You can decide which region to use, which might be important from a regulatory perspective, and might improve latency.

The big disadvantage is that for local development you may need to create and
configure a "service account", which I've found extremely painful to get right
in the past.

Whichever way you authenticate, you'll need to have VertexAI enabled in your GCP
account.

Luckily if you're running PydanticAI inside GCP, or you have the installed and
configured, you should be able to use without any additional setup.

To use , with configured (e.g. with ), you can simply use:

Internally this uses from the package to obtain credentials.

Because requires network requests and can be slow, it's not run until you call .
Meaning any configuration or permissions error will only be raised when you try
to use the model. To for this check to be run, call .

You may also need to pass the if application default credentials don't set a
project, if you pass and it conflicts with the project set by application
default credentials, an error is raised.

If instead of application default credentials, you want to authenticate with a
service account, you'll need to create a service account, add it to your GCP
project (note: AFAIK this step is necessary even if you created the service
account within the project), give that service account the "Vertex AI Service
Agent" role, and download the service account JSON file.

Once you have the JSON file, you can use it thus:

Whichever way you authenticate, you can specify which region requests will be
sent to via the .

Using a region close to your application can improve latency and might be
important from a regulatory perspective.

contains a list of available regions.

To use , you need to either install , or install with the optional group:

**This is because internally, uses the OpenAI API.**

To use , you must first download the Ollama client, and then download a model
using the .

You must also ensure the Ollama server is running when trying to make requests
to it. For more information, please see the .

For detailed setup and example, please see the .

To use , you need to either install , or install with the optional group:

To use through their API, go to and follow your nose until you find the place to
generate an API key.

contains a list of available Groq models.

Once you have the API key, you can set it as an environment variable:

You can then use by name:

Or initialise the model directly with just the model name:

If you don't want to or can't set the environment variable, you can pass it at
runtime via the :

To use , you need to either install , or install with the optional group:

To use through their API, go to and follow your nose until you find the place to
generate an API key.

contains a list of the most popular Mistral models.

Once you have the API key, you can set it as an environment variable:

You can then use by name:

Or initialise the model directly with just the model name:

If you don't want to or can't set the environment variable, you can pass it at
runtime via the :

Many of the models are compatible with OpenAI API, and thus can be used with in
PydanticAI. Before getting started, check the section for installation and
configuration instructions.

To use another OpenAI-compatible API, you can make use of the and arguments:

To use , first create an API key at .

Once you have the API key, you can pass it to as the argument:

Go to and create an API key. Once you have the API key, follow the , and set the
and arguments appropriately:

Go to and create an API key. Once you have the API key, follow the , and set the
and arguments appropriately:

To implement support for models not already supported, you will need to subclass
the abstract base class.

This in turn will require you to implement the following other abstract base
classes:

The best place to start is to review the source code for existing
implementations, e.g. .

For details on when we'll accept contributions adding new models to PydanticAI,
see the .

---

# Dependencies
URL: https://ai.pydantic.dev/dependencies/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

PydanticAI uses a dependency injection system to provide data and services to
your agent's , and .

Matching PydanticAI's design philosophy, our dependency system tries to use
existing best practice in Python development rather than inventing esoteric
"magic", this should make dependencies type-safe, understandable easier to test
and ultimately easier to deploy in production.

Dependencies can be any python type. While in simple cases you might be able to
pass a single object as a dependency (e.g. an HTTP connection), are generally a
convenient container when your dependencies included multiple objects.

Here's an example of defining an agent that requires dependencies.

( dependencies aren't actually used in this example, see below)

```

  


  

  
  
  

  
  
  

  
      
       
       
      
       
    
    
    #> Did you hear about the toothpaste scandal? They called it Colgate.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

Dependencies are accessed through the type, this should be the first parameter
of system prompt functions etc.

```

  


    



  
  

  
  
  

  
      
       
        
    
    #> Did you hear about the toothpaste scandal? They called it Colgate.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

, and are all run in the async context of an agent run.

If these functions are not coroutines (e.g. ) they are called with in a thread
pool, it's therefore marginally preferable to use methods where dependencies
perform IO, although synchronous dependencies should work fine too.

vs. and Asynchronous vs. Synchronous dependencies

Whether you use synchronous or asynchronous dependencies, is completely
independent of whether you use or — is just a wrapper around and agents are
always run in an async context.

Here's the same example as above, but with a synchronous dependency:

```

  


    



  
    

  
  
  

     
    
      
  
  
  

  
     
     
    
    
  
  
  #> Did you hear about the toothpaste scandal? They called it Colgate.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

As well as system prompts, dependencies can be used in and .

```

  


     



  
  

  
  
  

     
     
  
  

  
      
       
        
    
    #> Did you hear about the toothpaste scandal? They called it Colgate.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

When testing agents, it's useful to be able to customise dependencies.

While this can sometimes be done by calling the agent directly within unit
tests, we can also override dependencies while calling application code which in
turn calls the agent.

This is done via the method on the agent.

```

  


    



  
  
       
       
    
     

  

     
     

      
  
  
  # now deep within application code we call our agent

      
       
         
  

```

_(This example is complete, it can be run "as is")_

```

     

  
      
     

  
   'Did you hear about the toothpaste scandal?'

```

The following examples demonstrate how to use dependencies in PydanticAI:

---

# Function Tools
URL: https://ai.pydantic.dev/tools/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Function tools provide a mechanism for models to retrieve extra information to
help them generate a response.

They're useful when it is impractical or impossible to put all the context an
agent might need into the system prompt, or when you want to make agents'
behavior more deterministic or reliable by deferring some of the logic required
to generate a response to another (not necessarily AI-powered) tool.

Function tools are basically the "R" of RAG (Retrieval-Augmented Generation) —
they augment what the model can do by letting it request extra information.

The main semantic difference between PydanticAI Tools and RAG is RAG is
synonymous with vector search, while PydanticAI tools are more general-purpose.
(Note: we may add support for vector search functionality in the future,
particularly an API for generating embeddings. See )

There are a number of ways to register tools with an agent:

  * via the decorator — for tools that need access to the agent 
  * via the decorator — for tools that do not need access to the agent 
  * via the keyword argument to which can take either plain functions, or instances of 

is considered the default decorator since in the majority of cases tools will
need access to the agent context.

Here's an example using both:

```



    
  
  
  
  
    "You're a dice game, you should roll the die and see if the number "
    "you get back matches the user's guess. If so, tell them they're a winner. "
    "Use the player's name in the response."
  



  
"""Roll a six-sided die and return the result."""

    



    

  

    

#> Congratulations Anne, you guessed correctly! You're a winner!

```

_(This example is complete, it can be run "as is")_

Let's print the messages from that game to see what happened:

```

  

        content="You're a dice game, you should roll the die and see if the number you get back matches the user's guess. If so, tell them they're a winner. Use the player's name in the response.",

        content="Congratulations Anne, you guessed correctly! You're a winner!",

```

We can represent this with a diagram:

## Registering Function Tools via kwarg

As well as using the decorators, we can register tools via the argument to the .
This is useful when you want to re-use tools, and can also give more fine-
grained control over the tools.

```



     

  
"""Roll a six-sided die and return the result."""

    

    

  

  
  
  
    

  
  
  
  
     
     
  

  

#> Congratulations Anne, you guessed correctly! You're a winner!

```

_(This example is complete, it can be run "as is")_

## Function Tools vs. Structured Results

As the name suggests, function tools use the model's "tools" or "functions" API
to let the model know what is available to call. Tools or functions are also
used to define the schema(s) for structured responses, thus a model might have
access to many tools, some of which call function tools while others end the run
and return a result.

Function parameters are extracted from the function signature, and all
parameters except are used to build the schema for that tool call.

Even better, PydanticAI extracts the docstring from functions and (thanks to )
extracts parameter descriptions from the docstring and adds them to the schema.

extracting parameter descriptions from , and style docstrings, and PydanticAI
will infer the format to use based on the docstring. We plan to add support in
the future to explicitly set the style to use, and warn/error if not all
parameters are documented; see .

To demonstrate a tool's schema, here we use to print the schema a model would
receive:

```

  
    
    
  

         

  

      
    
  
  
  

      'a': {'description': 'apple pie', 'title': 'A', 'type': 'integer'},
      'b': {'description': 'banana cake', 'title': 'B', 'type': 'string'},

        'additionalProperties': {'items': {'type': 'number'}, 'type': 'array'},

  



```

_(This example is complete, it can be run "as is")_

The return type of tool can be anything which Pydantic can serialize to JSON as
some models (e.g. Gemini) support semi-structured return values, some expect
text (OpenAI) but seem to be just as good at extracting meaning from the data.
If a Python object is returned and the model expects a string, the value will be
serialized to JSON.

If a tool has a single parameter that can be represented as an object in JSON
schema (e.g. dataclass, TypedDict, pydantic model), the schema for the tool is
simplified to be just that object.

Here's an example, we use to inspect the tool schema that would be passed to the
model.

```

  
  
  
  



  
  
     

    
  

  
  

        'x': {'title': 'X', 'type': 'integer'},
        'y': {'title': 'Y', 'type': 'string'},
        'z': {'default': 3.14, 'title': 'Z', 'type': 'number'},

```

_(This example is complete, it can be run "as is")_

Tools can optionally be defined with another function: , which is called at each
step of a run to customize the definition of the tool passed to the model, or
omit the tool completely from that step.

A method can be registered via the kwarg to any of the tool registration
mechanisms:

The method, should be of type , a function which takes and a pre-built , and
should either return that with or without modifying it, return a new , or return
to indicate this tools should not be registered for that step.

Here's a simple method that only includes the tool if the value of the
dependency is .

As with the previous example, we use to demonstrate the behavior without calling
a real model.

```

  
    
  
  

  
     
  
     
     

      
  

  

#> success (no tool calls)

  

```

_(This example is complete, it can be run "as is")_

Here's a more complex example where we change the description of the parameter
to based on the value of

For the sake of variation, we create this tool using the dataclass.

```

  
  
    
  
    

    
  

  
      
    
    
    
  

  
  
     
  

          'description': 'Name of the human to greet.',

```

_(This example is complete, it can be run "as is")_

---

# Results
URL: https://ai.pydantic.dev/results/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Results are the final values returned from . The result values are wrapped in
and so you can access other data like of the run and

Both and are generic in the data they wrap, so typing information about the data
returned by the agent is preserved.

```

  
  



  
  

  
  'Where were the olympics held in 2012?'

Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65,
details=None)

```

_(This example is complete, it can be run "as is")_

Runs end when either a plain text response is received or the model calls a tool
associated with one of the structured result types. We will add limits to make
sure a run doesn't go on indefinitely, see .

When the result type is , or a union including , plain text responses are
enabled on the model, and the raw text response from the model is used as the
response data.

If the result type is a union with multiple members (after remove from the
members), each member is registered as a separate tool with the model in order
to reduce the complexity of the tool schemas and maximise the chances a model
will respond correctly.

If the result type schema is not of type , the result type is wrapped in a
single element object, so the schema of all tools registered with the model are
object schemas.

Structured results (like tools) use Pydantic to build the JSON schema used for
the tool, and to validate the data returned by the model.

Until "Annotating Type Forms" lands, unions are not valid as s in Python.

When creating the agent we need to the argument, and add a type hint to tell
type checkers about the type of the agent.

Here's an example of returning either text or a structured value

```

  
  
  



  
  
  
  

     
  
    
  
    "Extract me the dimensions of a box, "
    "if you can't extract all data, ask the user to try again."
  

  

#> Please provide the units for the dimensions (e.g., cm, in, m).

  'The box is 10x20x30 cm'

#> width=10 height=20 depth=30 units='cm'

```

_(This example is complete, it can be run "as is")_

Here's an example of using a union return type which registered multiple tools,
and wraps non-object schemas in an object:

```

  
  
     
  
    
  'Extract either colors or sizes from the shapes provided.'

  'red square, blue circle, green triangle'

  'square size 10, circle size 20, triangle size 30'

```

_(This example is complete, it can be run "as is")_

Some validation is inconvenient or impossible to do in Pydantic validators, in
particular when the validation requires IO and is asynchronous. PydanticAI
provides a way to add validation functions via the decorator.

Here's a simplified variant of the :

```

  
    
  
     



  



  

  
    
  
  
  
  'Generate PostgreSQL flavored SQL queries based on user input.'

       
    
     
  
     
     
       
  
     

  
  'get me uses who were last active yesterday.'

#> sql_query='SELECT * FROM users WHERE last_active::date = today() - interval 1
day'

```

_(This example is complete, it can be run "as is")_

There two main challenges with streamed results:

  1. Validating structured responses before they're complete, this is achieved by "partial validation" which was recently added to Pydantic in .
  2. When receiving a response, we don't know if it's the final response without starting to stream it and peeking at the content. PydanticAI streams just enough of the response to sniff out if it's a tool call or a result, then streams the whole thing and calls tools, or returns the stream as a .

Example of streamed text result:

```

  
  

  
    'Where does "hello world" come from?'   
         
      
      
      #> The first known use of "hello,
      #> The first known use of "hello, world" was in
      #> The first known use of "hello, world" was in a 1974 textbook
      #> The first known use of "hello, world" was in a 1974 textbook about the C
      #> The first known use of "hello, world" was in a 1974 textbook about the C programming language.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

We can also stream text as deltas rather than the entire text in each item:

```

  
  

  
    'Where does "hello world" come from?'  
         
      
      
      
      
      
      
      

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

Result message not included in

The final result message will be added to result messages if you use , see for
more information.

Not all types are supported with partial validation in Pydantic, see , generally
for model-like structures it's currently best to use .

Here's an example of streaming a use profile as it's built:

```

  
  
  

  
  
  
  

  
  
  
  'Extract a user profile from the input'

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

If you want fine-grained control of validation, particularly catching validation
errors, you can use the following pattern:

```

  
  
  
  

  
  
  
  

  

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
          
      
            
          
           
        
       
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

The following examples demonstrate how to use streamed responses in PydanticAI:

---

# Messages and chat history
URL: https://ai.pydantic.dev/message-history/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

PydanticAI provides access to messages exchanged during an agent run. These
messages can be used both to continue a coherent conversation, and to understand
how an agent performed.

After running an agent, you can access the messages exchanged during that run
from the object.

Both (returned by , ) and (returned by ) have the following methods:

  * : returns all messages, including messages from prior runs. There's also a variant that returns JSON bytes, .
  * : returns only the messages from the current run. There's also a variant that returns JSON bytes, .

On , the messages returned from these methods will only include the final result
message once the stream has finished.

E.g. you've awaited one of the following coroutines:

The final result message will NOT be added to result messages if you use since
in this case the result content is never built as one string.

Example of accessing methods on a :

```

  
  
  

#> Did you hear about the toothpaste scandal? They called it Colgate.

# all messages from the run

        content='Did you hear about the toothpaste scandal? They called it Colgate.',

```

_(This example is complete, it can be run "as is")_

Example of accessing methods on a :

```

  
  

  
      
    # incomplete messages before the stream finishes

        
      
      #> Did you hear about the toothpaste
      #> Did you hear about the toothpaste scandal? They called
      #> Did you hear about the toothpaste scandal? They called it Colgate.
    # complete messages once the stream finishes
    

            content='Did you hear about the toothpaste scandal? They called it Colgate.',

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

### Using Messages as Input for Further Agent Runs

The primary use of message histories in PydanticAI is to maintain context across
multiple agent runs.

To use existing messages in a run, pass them to the parameter of , or .

If is set and not empty, a new system prompt is not generated — we assume the
existing message history includes a system prompt.

Reusing messages in a conversation```

  
  
  

#> Did you hear about the toothpaste scandal? They called it Colgate.

#> This is an excellent joke invent by Samuel Colvin, it needs no explanation.

        content='Did you hear about the toothpaste scandal? They called it Colgate.',

        content='This is an excellent joke invent by Samuel Colvin, it needs no explanation.',

```

_(This example is complete, it can be run "as is")_

## Other ways of using messages

Since messages are defined by simple dataclasses, you can manually create and
manipulate, e.g. for testing.

The message format is independent of the model used, so you can use messages in
different agents, or the same agent with different models.

```

  
  
  

#> Did you hear about the toothpaste scandal? They called it Colgate.

  
    

#> This is an excellent joke invent by Samuel Colvin, it needs no explanation.

        content='Did you hear about the toothpaste scandal? They called it Colgate.',

        content='This is an excellent joke invent by Samuel Colvin, it needs no explanation.',

```

For a more complete example of using messages in conversations, see the example.

---

# Testing and Evals
URL: https://ai.pydantic.dev/testing-evals/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

With PydanticAI and LLM integrations in general, there are two distinct kinds of
test:

  1. — tests of your application code, and whether it's behaving correctly
  2. — tests of the LLM, and how good or bad its responses are

For the most part, these two kinds of tests have pretty separate goals and
considerations.

Unit tests for PydanticAI code are just like unit tests for any other Python
code.

Because for the most part they're nothing new, we have pretty well established
tools and patterns for writing and running these kinds of tests.

Unless you're really sure you know better, you'll probably want to follow
roughly this strategy:

  * If you find yourself typing out long assertions, use 
  * Similarly, can be useful for comparing large data structures
  * Use or in place of your actual model to avoid the usage, latency and variability of real LLM calls
  * Use to replace your model inside your application logic
  * Set globally to block any requests from being made to non-test models accidentally

The simplest and fastest way to exercise most of your application code is using
, this will (by default) call all tools in the agent, then return either plain
text or a structured response depending on the return type of the agent.

The "clever" (but not too clever) part of is that it will attempt to generate
valid structured data for and based on the schema of the registered tools.

There's no ML or AI in , it's just plain old procedural Python code that tries
to generate data that satisfies the JSON schema of a tool.

The resulting data won't look pretty or relevant, but it should pass Pydantic's
validation in most cases. If you want something more sophisticated, use and
write your own data generation logic.

Let's write unit tests for the following application code:

```



  
    
    
    
  
  
  
  'Providing a weather forecast at the locations the user provides.'



       
  
      
      
  
      

  
      

"""Run weather forecast for a list of user prompts and save."""

      
         
          
        
    # run all prompts in parallel
     
            
    

```

Here we have a function that takes a list of tuples, gets a weather forecast for
each prompt, and stores the result in the database.

**We want to test this code without having to mock certain objects or modify our
code so we can pass test objects in.**

Here's how we would write tests using :

```

  


  
    
  
  
  
  
  
  
  
  
  
  

  
    
  
  

  
    
    
     
      
        'What will the weather be like in London on 2024-11-28?'
          
     
     '{"weather_forecast":"Sunny with a chance of rain"}' 
      
    
      
        
          'Providing a weather forecast at the locations the user provides.'
        
        
          'What will the weather be like in London on 2024-11-28?'
           
        
      
    
    
      
        
          
          
            
               
                
            
          
          
        
      
      
    
    
      
        
          
          'Sunny with a chance of rain'
          
          
        
      
    
    
      
        
          '{"weather_forecast":"Sunny with a chance of rain"}'
        
      
      
    
  

```

The above tests are a great start, but careful readers will notice that the is
never called since calls with a date in the past.

To fully exercise , we need to use to customise how the tools is called.

Here's an example of using to test the tool with custom inputs

```





  
  
  
  
  

    
  
    
  
  

  
     
  
     
    # first call, call the weather forecast tool
      
       
        
          
     
       
    
  
    # second call, return the forecast
      
       
     

  
    
    
    
      'What will the weather be like in London on 2032-01-01?'
       
     
     'The forecast is: Rainy with a chance of sun'

```

### Overriding model via pytest fixtures

If you're writing lots of tests that all require model to be overridden, you can
use to override the model with or in a reusable way.

Here's an example of a fixture that overrides the model with :

"Evals" refers to evaluating a models performance for a specific application.

Unlike unit tests, evals are an emerging art/science; anyone who claims to know
for sure exactly how your evals should be defined can safely be ignored.

Evals are generally more like benchmarks than unit tests, they never "pass"
although they do "fail"; you care mostly about how they change over time.

Since evals need to be run against the real model, then can be slow and
expensive to run, you generally won't want to run them in CI for every commit.

The hardest part of evals is measuring how well the model has performed.

In some cases (e.g. an agent to generate SQL) there are simple, easy to run
tests that can be used to measure performance (e.g. is the SQL valid? Does it
return the right results? Does it return just the right results?).

In other cases (e.g. an agent that gives advice on quitting smoking) it can be
very hard or impossible to make quantitative measures of performance — in the
smoking case you'd really need to run a double-blind trial over months, then
wait 40 years and observe health outcomes to know if changes to your prompt were
an improvement.

There are a few different strategies you can use to measure performance:

  * **End to end, self-contained tests** — like the SQL example, we can test the final result of the agent near-instantly
  * — writing unit test style checks that the output is as expected, checks like , while these checks might seem simplistic they can be helpful, one nice characteristic is that it's easy to tell what's wrong when they fail
  * — using another models, or even the same model with a different prompt to evaluate the performance of the agent (like when the class marks each other's homework because the teacher has a hangover), while the downsides and complexities of this approach are obvious, some think it can be a useful tool in the right circumstances
  * — measuring the end results of the agent in production, then creating a quantitative measure of performance, so you can easily measure changes over time as you change the prompt or model used, can be extremely useful in this case since you can write a custom query to measure the performance of your agent

The system prompt is the developer's primary tool in controlling an agent's
behavior, so it's often useful to be able to customise the system prompt and see
how performance changes. This is particularly relevant when the system prompt
contains a list of examples and you want to understand how changing that list
affects the model's performance.

Let's assume we have the following app for running SQL generated from a user
prompt (this examples omits a lot of details for brevity, see the example for a
more complete code):

```



  
  
    
  

  
  
              
  
       
      # if examples aren't provided, load them from file, this is the default
         
          
    
        
      
      
     
 table of records, your job is to

write a SQL query that suits the user's request.

  
        
     

  
  
  

     
  

      
"""Search the database based on the user's prompts."""

  
      
    
    

```

```

request: show me error records with the tag "foobar"

response: SELECT * FROM records WHERE level = 'error' and 'foobar' = ANY(tags)

```

```

"Show me all records from 2021"

"SELECT * FROM records WHERE date_trunc('year', date) = '2021-01-01';"

"show me error records with the tag 'foobar'"

"SELECT * FROM records WHERE level = 'error' and 'foobar' = ANY(tags);"

```

Now we want a way to quantify the success of the SQL generation so we can judge
how changes to the agent affect its performance.

We can use to replace the system prompt with a custom one that uses a subset of
examples, and then run the application code (in this case ). We also run the
actual SQL from the examples and compare the "correct" result from the example
SQL to the SQL generated by the agent. (We compare the results of running the
SQL rather than the SQL itself since the SQL might be semantically equivalent
but written in a different way).

To get a quantitative measure of performance, we assign points to each run as
follows: * points if the generated SQL is invalid * point for each row returned
by the agent (so returning lots of results is discouraged) * points for each row
returned by the agent that matches the expected result

We use 5-fold cross-validation to judge the performance of the agent using our
existing set of examples.

```





  
  
    
     

  
     
      
  # split examples into 5 folds

      
              
    
    
       
      
    # build all other folds into a list of examples
               
    # create a new system prompt with the other fold examples
      
    # override the system prompt with the new one
     
         
        
             
           
          
            
        
          # get the expected results using the SQL from this case
             
              
        # each returned value has a score of -1
          
              
        # each return value that matches the expected value has a score of 3
              
    
    
  
  

```

We can then change the prompt, the model, or the examples and see how the score
changes over time.

---

# Debugging and Monitoring
URL: https://ai.pydantic.dev/logfire/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Applications that use LLMs have some challenges that are well known and
understood: LLMs are , and .

These applications also have some challenges that most developers have
encountered much less often: LLMs are and . Subtle changes in a prompt can
completely change a model's performance, and there's no query you can run to
understand why.

From a software engineers point of view, you can think of LLMs as the worst
database you've ever heard of, but worse.

If LLMs weren't so bloody useful, we'd never touch them.

To build successful applications with LLMs, we need new tools to understand both
model performance, and the behavior of applications that rely on them.

LLM Observability tools that just let you understand how your model is
performing are useless: making API calls to an LLM is easy, it's building that
into an application that's hard.

is an observability platform developed by the team who created and maintain
Pydantic and PydanticAI. Logfire aims to let you understand your entire
application: Gen AI, classic predictive AI, HTTP traffic, database queries and
everything else a modern application needs.

Pydantic Logfire is a commercial product

Logfire is a commercially supported, hosted platform with an extremely generous
and perpetual . You can sign up and start using Logfire in a couple of minutes.

PydanticAI has built-in (but optional) support for Logfire via the no-op
package.

That means if the package is installed and configured, detailed information
about agent runs is sent to Logfire. But if the package is not installed,
there's virtually no overhead and nothing is sent.

Here's an example showing details of running the in Logfire:

To use logfire, you'll need a logfire , and logfire installed:

Then authenticate your local environment with logfire:

And configure a project to send data to:

(Or use an existing project with )

The last step is to add logfire to your code:

The has more details on how to use logfire, including how to instrument other
libraries like Pydantic, HTTPX and FastAPI.

Since Logfire is build on , you can use the Logfire Python SDK to send data to
any OpenTelemetry collector.

Once you have logfire set up, there are two primary ways it can help you
understand your application:

  * — Using the live view to see what's happening in your application in real-time.
  * — Using SQL and dashboards to observe the behavior of your application, Logfire is effectively a SQL database that stores information about how your application is running.

To demonstrate how Logfire can let you visualise the flow of a PydanticAI run,
here's the view you get from Logfire while running the :

We can also query data with SQL in Logfire to monitor the performance of an
application. Here's a real world example of using Logfire to monitor PydanticAI
runs inside Logfire itself:

---

# Multi-agent Applications
URL: https://ai.pydantic.dev/multi-agent-applications/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

There are roughly four levels of complexity when building applications with
PydanticAI:

  1. Single agent workflows — what most of the documentation covers
  2. — agents using another agent via tools
  3. — one agent runs, then application code calls another agent
  4. — for the most complex cases, a graph-based state machine can be used to control the execution of multiple agents

Of course, you can combine multiple strategies in a single application.

"Agent delegation" refers to the scenario where an agent delegates work to
another agent, then takes back control when the delegate agent (the agent called
from within a tool) finishes.

Since agents are stateless and designed to be global, you do not need to include
the agent itself in agent .

You'll generally want to pass to the keyword argument of the delegate agent run
so usage within that run counts towards the total usage of the parent agent run.

Agent delegation doesn't need to use the same model for each agent. If you
choose to use different models within a run, calculating the monetary cost from
the final of the run will not be possible, but you can still use to avoid
unexpected costs.

```

    
  
  
  
  
    'Use the `joke_factory` to generate some jokes, then choose the best. '
    'You must return just a single joke.'
  

    

       
      
    
     
  
    

  
  
  

#> Did you hear about the toothpaste scandal? They called it Colgate.

  requests=3, request_tokens=204, response_tokens=24, total_tokens=228,
details=None

```

_(This example is complete, it can be run "as is")_

The control flow for this example is pretty simple and can be summarised as
follows:

Generally the delegate agent needs to either have the same as the calling agent,
or dependencies which are a subset of the calling agent's dependencies.

We say "generally" above since there's nothing to stop you initializing
dependencies within a tool call and therefore using interdependencies in a
delegate agent that are not available on the parent, this should often be
avoided since it can be significantly slower than reusing connections etc. from
the parent agent.

```

  


    

  
  
  

  
  
  
  
    'Use the `joke_factory` tool to generate some jokes on the given subject, '
    'then choose the best. You must return just a single joke.'
  

  
  
  
  
  
    'Use the "get_jokes" tool to get some jokes on the given subject, '
    'then extract each joke into a list.'
  

       
     
    
     
    
  
  



       
     
    
     
     
  
  
  

  
      
       
        
    
    #> Did you hear about the toothpaste scandal? They called it Colgate.
     

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

This example shows how even a fairly simple agent delegation can lead to a
complex control flow:

"Programmatic agent hand-off" refers to the scenario where multiple agents are
called in succession, with application code and/or a human in the loop
responsible for deciding which agent to call next.

Here agents don't need to use the same deps.

Here we show two agents used in succession, the first to find a flight and the
second to extract the user's seat preference.

```

    
    
  
    
  
    



  



"""Unable to find a satisfactory choice."""

     
  
    
  
    'Use the "flight_search" tool to find a flight '
    'from the given origin to the given destination.'
  



  
       
  
  # in reality, this would call a flight search API or

  # use a browser to scrape a flight search website

  

  

       
      
     
      
      'Where would you like to fly from and to?'
    
       
      
      
      
      
    
      
       
    
        
        
      



      
        

# This agent is responsible for extracting the user's seat selection

     
  
    
  
    "Extract the user's seat preference. "
    'Seats A and F are window seats. '
    'Row 1 is the front row and has extra leg room. '
    'Rows 14, and 20 also have extra leg room. '
  

      
      
  
      'What seat would you like?'
       
      
      
      
      
    
      
       
    
      'Could not understand seat preference. Please try again.'
        

  
     
     
      
    
    
       
    
    #> Seat preference: row=1 seat='A'

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

The control flow for this example can be summarised as follows:

See the documentation on when and how to use graphs.

The following examples demonstrate how to use dependencies in PydanticAI:

---

# Graphs
URL: https://ai.pydantic.dev/graph/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Don't use a nail gun unless you need a nail gun

If PydanticAI are a hammer, and are a sledgehammer, then graphs are a nail gun:

  * sure, nail guns look cooler than hammers
  * but nail guns take a lot more setup than hammers
  * and nail guns don't make you a better builder, they make you a builder with a nail gun
  * Lastly, (and at the risk of torturing this metaphor), if you're a fan of medieval tools like mallets and untyped Python, you probably won't like nail guns or our approach to graphs. (But then again, if you're not a fan of type hints in Python, you've probably already bounced off PydanticAI to use one of the toy agent frameworks — good luck, and feel free to borrow my sledgehammer when you realize you need it)

In short, graphs are a powerful tool, but they're not the right tool for every
job. Please consider other before proceeding.

If you're not confident a graph-based approach is a good idea, it might be
unnecessary.

Graphs and finite state machines (FSMs) are a powerful abstraction to model,
execute, control and visualize complex workflows.

Alongside PydanticAI, we've developed — an async graph and state machine library
for Python where nodes and edges are defined using type hints.

While this library is developed as part of PydanticAI; it has no dependency on
and can be considered as a pure graph-based state machine library. You may find
it useful whether or not you're using PydanticAI or even building with GenAI.

is designed for advanced users and makes heavy use of Python generics and types
hints. It is not designed to be as beginner-friendly as PydanticAI.

Graph support was in v0.0.19 and is in very earlier beta. The API is subject to
change. The documentation is incomplete. The implementation is incomplete.

is a required dependency of , and an optional dependency of , see for more
information. You can also install it directly:

made up of a few key components:

— The context for the graph run, similar to PydanticAI's . This holds the state
of the graph and dependencies and is passed to nodes when they're run.

is generic in the state type of the graph it's used in, .

— return value to indicate the graph run should end.

is generic in the graph return type of the graph it's used in, .

Subclasses of define nodes for execution in the graph.

Nodes, which are generally , generally consist of:

  * fields containing any parameters required/optional when calling the node
  * the business logic to execute the node, in the method
  * return annotations of the method, which are read by to determine the outgoing edges of the node

  * , which must have the same type as the state of graphs they're included in, has a default of , so if you're not using state you can omit this generic parameter, see for more information
  * , which must have the same type as the deps of the graph they're included in, has a default of , so if you're not using deps you can omit this generic parameter, see for more information
  * — this only applies if the node returns . has a default of so this generic parameter can be omitted if the node doesn't return , but must be included if it does.

Here's an example of a start or intermediate node in a graph — it can't end the
run as it doesn't return :

We could extend to optionally end the run if is divisible by 5:

— this is the execution graph itself, made up of a set of (i.e., subclasses).

  * the state type of the graph, 
  * the deps type of the graph, 
  * the return type of the graph run, 

Here's an example of a simple graph:

```

  
  
      

    
  
    
    
     
      
         
       
    
       

  
  
        
       

    
    

# the full history is quite verbose (see below), so we'll just print the summary

    
#> [DivisibleBy5(foo=4), Increment(foo=4), DivisibleBy5(foo=5), End(data=5)]

```

_(This example is complete, it can be run "as is" with Python 3.10+)_

A for this graph can be generated with the following code:

The "state" concept in provides an optional way to access and mutate an object
(often a or Pydantic model) as nodes run in a graph. If you think of Graphs as a
production line, then you state is the engine being passed along the line and
built up by each node as the graph is run.

In the future, we intend to extend to provide state persistence with the state
recorded after each node is run, see .

Here's an example of a graph which represents a vending machine where the user
may insert coins and select a product to purchase.

```

  
  
  
      

  
     
       

  
         
      



    
    
      
       
       
         
       
    
       



        
     

  
  
  
  
  

    
  
    
      
        
        
         
          
          
         
      
            
        
        #> Not enough money for crisps, need 0.75 more
          
    
      
        

  
     

  
     
     
  
  #> purchase successful item=crisps change=0.25

```

_(This example is complete, it can be run "as is" with Python 3.10+ — you'll
need to add to run )_

A for this graph can be generated with the following code:

The diagram generated by the above code is:

See for more information on generating diagrams.

So far we haven't shown an example of a Graph that actually uses PydanticAI or
GenAI at all.

In this example, one agent generates a welcome email to a user and the other
agent provides feedback on the email.

This graph has a very simple structure:

```

     
    
    
  
  
  
      



  
  
  



  
  



  
     

  
  
  
  'Write a welcome email to our tech blog.'



       
        
     
        
        'Rewrite the email for the user:
        
        
      
    
        
        'Write a welcome email for the user:
        
      
       
      
      
    
      
     



  



  

     
  
     
  
    'Review the email and provide feedback, email must reference the users specific interests.'
  

  
  
    
    
     
      
         
       
      
       
    
       

  
    
    
    
      
  
    
     
       
  

    subject='Welcome to our tech blog!',
    body='Hello John, Welcome to our tech blog! ...',

```

_(This example is complete, it can be run "as is" with Python 3.10+ — you'll
need to add to run )_

In many real-world applications, Graphs cannot run uninterrupted from start to
finish — they might require external input, or run over an extended period of
time such that a single process cannot execute the entire graph run from start
to finish without interruption.

In these scenarios the method can be used to run the graph one node at a time.

In this example, an AI asks the user a question, the user provides an answer,
the AI evaluates the answer and ends if the user got it right or asks another
question if they got it wrong.

```

     
    
      
  
  
  
  



       
     
     



        
       
      'Ask a simple question with a single correct answer.'
      
    
      
      
     



  
       
        
        
     



  
  

  
  
  
  'Given a question and answer, evaluate if the answer is correct.'



  
    
    
     
      
        
       
         
      
    
      
     
       
    
       



  
        
    
      
     

     

```

_(This example is complete, it can be run "as is" with Python 3.10+)_

```

  
    
      

  
     
     
      
  
          
      
         
       
      
      #> Correct answer! Well done, 1 + 1 = 2
          

        Answer(question='What is the capital of France?', answer='Vichy'),

        Reprimand(comment='Vichy is no longer the capital of France.'),

        Answer(question='what is 1 + 1?', answer='2'),

      
    

```

_(This example is complete, it can be run "as is" with Python 3.10+ — you'll
need to add to run )_

A for this graph can be generated with the following code:

You maybe have noticed that although this examples transfers control flow out of
the graph run, we're still using to get user input, with the process hanging
while we wait for the user to enter a response. For an example of genuine out-
of-process control flow, see the .

As with PydanticAI, supports dependency injection via a generic parameter on and
, and the fields.

As an example of dependency injection, let's modify the example to use a to run
the compute load in a separate process (this is a contrived example, wouldn't
actually improve performance in this example):

```

  


  
      

  
  
    
    
     
      
         
       
    
       



  
        
      
    
     
     
       

  

      
         
  
  
  # the full history is quite verbose (see below), so we'll just print the
summary

      

```

_(This example is complete, it can be run "as is" with Python 3.10+ — you'll
need to add to run )_

Pydantic Graph can generate diagrams for graphs, as shown above.

These diagrams can be generated with:

  * to generate the mermaid code for a graph
  * to generate an image of the graph using 
  * to generate an image of the graph using and save it to a file

Beyond the diagrams shown above, you can also customize mermaid diagrams with
the following options:

  * allows you to apply a label to an edge
  * and allows you to add notes to nodes
  * The parameter allows you to highlight specific node(s) in the diagram

Putting that together, we can edit the last example to:

  * add labels to some edges
  * add a note to the node
  * save the diagram as a image to file

```



    
      
    



  
    
      
       
    

```

_(This example is not complete and cannot be run directly)_

Would generate and image that looks like this:

---

# Examples
URL: https://ai.pydantic.dev/examples/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Examples of how to use PydanticAI and what it can do.

These examples are distributed with so you can run them either by cloning the or
by simply installing from PyPI with or .

Either way you'll need to install extra dependencies to run some examples, you
just need to install the optional dependency group.

If you've installed via pip/uv, you can install the extra dependencies with:

If you clone the repo, you should instead use to install extra dependencies.

These examples will need you to set up authentication with one or more of the
LLMs, see the docs for details on how to do this.

TL;DR: in most cases you'll need to set one of the following environment
variables:

To run the examples (this will work whether you installed , or cloned the repo),
run:

For examples, to run the very simple example:

If you like one-liners and you're using uv, you can run a pydantic-ai example
with zero setup:

You'll probably want to edit examples in addition to just running them. You can
copy the examples to a new directory with:

---

# Pydantic Model
URL: https://ai.pydantic.dev/examples/pydantic-model/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Simple example of using PydanticAI to construct a Pydantic model from a text
input.

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/pydantic-model/<../#usage>), run:

This examples uses by default, but it works well with other models, e.g. you can
run it with Gemini using:

```



  


  
  
  
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured



  
  

    

  
  
    'The windy city in the US of A.'
  
  

```

---

# Weather agent
URL: https://ai.pydantic.dev/examples/weather-agent/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Example of PydanticAI with multiple tools which the LLM needs to call in turn to
answer a question.

  * Building a UI for the agent

In this case the idea is a "weather" agent — the user can ask for the weather in
multiple locations, the agent will use the tool to get the latitude and
longitude of the locations, then use the tool to get the weather for those
locations.

To run this example properly, you might want to add two extra API keys **(Note
if either key is missing, the code will fall back to dummy data, so they're not
required)** :

  * A weather API key from set via 
  * A geocoding API key from set via 

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/weather-agent/<../#usage>), run:

```

     




  
  


  
  
     
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured



  
     
     

  
  
  # 'Be concise, reply with one sentence.' is enough for some models (like
openai) to use

  # the below tools appropriately, but others like anthropic and gemini require
a bit more direction.

  
    'Be concise, reply with one sentence.'
    'Use the `get_lat_lng` tool to get the latitude and longitude of the locations, '
    'then use the `get_weather` tool to get the weather.'
  
  
  

  
     
  
"""Get the latitude and longitude of a location.

    location_description: A description of a location.

     
    # if no API key is provided, return a dummy response (London)
        
    
     
     
  
      
        
    
      
     
  
        
  
     'Could not find the location'

          
"""Get the weather at a location.

    lat: Latitude of the location.
    lng: Longitude of the location.

     
    # if no API key is provided, return a dummy response
        
    
     
     
     
  
      
       
       
    
    
      
     
    
  
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
  
  
     
      
  

  
      
    # create a free API key at https://www.tomorrow.io/weather-api/
      
    # create a free API key at https://geocode.maps.co/
      
      
        
    
       
      'What is the weather like in London and in Wiltshire?' 
    
    
     

  
  

```

You can build multi-turn chat applications for your agent with , a framework for
building AI web applications entirely in python. Gradio comes with built-in chat
components and agent support so the entire UI will be implemented in a single
python file!

Here's what the UI looks like for the weather agent:

Note, to run the UI, you'll need Python 3.10+.

---

# Bank support
URL: https://ai.pydantic.dev/examples/bank-support/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Small but complete example of using PydanticAI to build a support agent for a
bank.

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/bank-support/<../#usage>), run:

```

  
    
    



"""This is a fake database for example purposes.

  In reality, you'd be connecting to an external database

  (e.g. PostgreSQL) to get information about customers.

  
           
       
       
  
           
       
       
    
       



  
  



     'Advice returned to the customer'
     
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query. '
    "Reply using the customer's name."
  

     
     
  

  
     
  
"""Returns the customer's current account balance."""

     
    
    
  
  

  
     
     
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

    'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

---

# SQL Generation
URL: https://ai.pydantic.dev/examples/sql-gen/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Example demonstrating how to use PydanticAI to generate SQL queries based on
user input.

The resulting SQL is validated by running it as an query on PostgreSQL. To run
the example, you first need to run PostgreSQL, e.g. via Docker:

_(we run postgres on port to avoid conflicts with any other postgres instances
you may have running)_

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/sql-gen/<../#usage>), run:

or to use a custom prompt:

This model uses by default since Gemini is good at single shot queries of this
kind.

```





  
  
  
  
     




  
  
    
  
     
  
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured

  

  
  
     'show me records where foobar is false'
     "SELECT * FROM records WHERE attributes->>'foobar' = false"
  
  
     'show me records where attributes include the key "foobar"'
     "SELECT * FROM records WHERE attributes ? 'foobar'"
  
  
     'show me records from yesterday'
     "SELECT * FROM records WHERE start_timestamp::date > CURRENT_TIMESTAMP - INTERVAL '1 day'"
  
  
     'show me error records with the tag "foobar"'
     "SELECT * FROM records WHERE level = 'error' and 'foobar' = ANY(tags)"
  



  



"""Response when SQL could be successfully generated."""

    
     
     'Explanation of the SQL query, as markdown'
  



"""Response the user input didn't include enough information to generate SQL."""

  

    
    
  
  # Type ignore while we wait for PEP-0747, nonetheless unions will work fine
everywhere else

  
  

    
  
Given the following PostgreSQL table of records, your job is to

write a SQL query that suits the user's request.

       
    
     
  # gemini often adds extraneous backslashes to SQL

     
    
     'Please create a SELECT query'
  
     
     
       
  
     

  
     
      'show me logs from yesterday, with level "error"'
  
      
    
     
    
      
        
  

        
  
       
    
         
        'SELECT 1 FROM pg_database WHERE datname = $1' 
      
        
         
    
       
     
  
     
        
          
           
            "CREATE TYPE log_level AS ENUM ('debug', 'info', 'warning', 'error', 'critical')"
          
         
     
  
     

  
  

```

---

# Flight booking
URL: https://ai.pydantic.dev/examples/flight-booking/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Example of a multi-agent flow where one agent delegates work to another, then
hands off control to a third agent.

In this scenario, a group of agents work together to find the best flight for a
user.

The control flow for this example can be summarised as follows:

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/flight-booking/<../#usage>), run:

```



  
  


    
  
     
  
    
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured



"""Details of the most suitable flight."""

  
  
     
     
  



"""When no valid flight is found."""



  
  
  
  

# This agent is responsible for controlling the flow of the conversation.

     
  
     
  
  
    'Your job is to find the cheapest flight for the user on the given date. '
  

# This agent is responsible for extracting flight details from web page text.

  
  
  
  'Extract all the flight details from the given text.'

     
"""Get details of all flights."""

  # we pass the usage to the search agent so requests within this agent are
counted

      
  
  

  
       
    
"""Procedural validation that the flight meets the constraints."""

    
     
     
     
    
      
    
     
    
      
    
     
    
  
     
  
     



      
        



"""Unable to extract a seat selection."""

# This agent is responsible for extracting the user's seat selection

  
     

  
     
  
    "Extract the user's seat preference. "
    'Seats A and F are window seats. '
    'Row 1 is the front row and has extra leg room. '
    'Rows 14, and 20 also have extra leg room. '
  

# in reality this would be downloaded from a booking site,

# potentially using another agent to navigate the site

  

- Origin: San Francisco International Airport (SFO)
- Destination: Ted Stevens Anchorage International Airport (ANC)
- Date: January 10, 2025

- Origin: San Francisco International Airport (SFO)
- Destination: Fairbanks International Airport (FAI)
- Date: January 10, 2025

- Origin: San Francisco International Airport (SFO)
- Destination: Juneau International Airport (JNU)
- Date: January 20, 2025

- Origin: San Francisco International Airport (SFO)
- Destination: Ted Stevens Anchorage International Airport (ANC)
- Date: January 10, 2025

- Origin: Chicago O'Hare International Airport (ORD)
- Destination: Miami International Airport (MIA)
- Date: January 12, 2025

- Origin: Boston Logan International Airport (BOS)
- Destination: Ted Stevens Anchorage International Airport (ANC)
- Date: January 12, 2025

- Origin: Dallas/Fort Worth International Airport (DFW)
- Destination: Denver International Airport (DEN)
- Date: January 10, 2025

- Origin: Hartsfield-Jackson Atlanta International Airport (ATL)
- Destination: George Bush Intercontinental Airport (IAH)
- Date: January 10, 2025

# restrict how many requests this app can make to the LLM

  

  
    
    
    
    
      
  
       
     
  # run the agent until a satisfactory flight is found

  
       
      'Find me a flight from 
      
      
      
      
    
      
      
      
    
        
      
        
        'Do you want to buy this flight, or keep searching? (buy/*search)'
          
        
      
         
           
          
        
      
          
          
        

     
       
  
      'What seat would you like?'
       
      
      
      
      
    
      
       
    
      'Could not understand seat preference. Please try again.'
        

     
  

  
  
  

```

---

# RAG
URL: https://ai.pydantic.dev/examples/rag/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

RAG search example. This demo allows you to ask question of the documentation.

This is done by creating a database containing each section of the markdown
documentation, then registering the search tool with the PydanticAI agent.

Logic for extracting sections from markdown files and a JSON file with that data
is available in .

is used as the search database, the easiest way to download and run pgvector is
using Docker:

As with the example, we run postgres on port to avoid conflicts with any other
postgres instances you may have running. We also mount the PostgreSQL directory
locally to persist the data if you need to stop and restart the container.

With that running and [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/rag/<../#usage>), we can build the search
database with (: this requires the env variable and will calling the OpenAI
embedding API around 300 times to generate embeddings for each section of the
documentation):

(Note building the database doesn't use PydanticAI right now, instead it uses
the OpenAI SDK directly.)

You can then ask the agent a question with:

```

python-mpydantic_ai_examples.ragsearch"How do I configure logfire to work with
FastAPI?"

```

```

uvrun-mpydantic_ai_examples.ragsearch"How do I configure logfire to work with
FastAPI?"

```

```

     








  
  








  
  
  
  
  
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured



  
  

  

       
"""Retrieve documentation sections based on a search query.

  
     
  
       
      
      
    
  
      
  
    
    
     
    'SELECT url, title, content FROM doc_sections ORDER BY embedding <-> $1 LIMIT 8'
    
  
  
    
       
  

  
"""Entry point to run the agent and perform RAG based question answering."""

    
  
  
      
       
        
  

# The rest of this file is dedicated to preparing the #

# search database, and some utilities.        #

  
  
  
  

  

      
       
    
    
    
  
      
     
          
          
           
      
        
         
           

  
  
  
  
  
  
    
      
       'SELECT 1 FROM doc_sections WHERE url = $1' 
     
       
      
      
         
        
        
      
     
        
     
      
      
     
      'INSERT INTO doc_sections (url, title, content, embedding) VALUES ($1, $2, $3, $4)'
      
      
      
      
    



  
     
  
  
  
  
     
        
     
      
    
     
       

  

  
     
  
     
    
    
  
  
     
         
      
           
          'SELECT 1 FROM pg_database WHERE datname = $1' 
        
          
           
      
         
     
  
     
  
     

  
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS doc_sections (

  url text NOT NULL UNIQUE,

  -- text-embedding-3-small returns a vector of 1536 floats

CREATE INDEX IF NOT EXISTS idx_doc_sections_embedding ON doc_sections USING hnsw
(embedding vector_l2_ops);

          
"""Slugify a string, to make it URL friendly."""

  # Taken unchanged from https://github.com/Python-
Markdown/markdown/blob/3.7/markdown/extensions/toc.py#L38

    
    # Replace Extended Latin characters with ASCII, i.e. `žlutý` => `zluty`
       
       
      
     

  
          
     
    
     
       
        
    
        'How do I configure logfire to work with FastAPI?'
    
  
    
      'uv run --extra examples -m pydantic_ai_examples.rag build|search'
      
    
    

```

---

# Stream markdown
URL: https://ai.pydantic.dev/examples/stream-markdown/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

This example shows how to stream markdown from an agent, using the library to
highlight the output in the terminal.

It'll run the example with both OpenAI and Google Gemini models if the required
environment variables are set.

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/stream-markdown/<../#usage>), run:

```







     
  
    
  
  
  
  
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured

  
# models to try, and the appropriate env var

    
  
  
  

  
  
    
    'Show me a short example of using Pydantic.'
  
      
       
      
           
             
              
            
      
    
      



"""Make rich code blocks prettier and easier to copy.

  
     
          
      
        
        
       
        
        
        
        
        
      
        
    

  
  

```

---

# Stream whales
URL: https://ai.pydantic.dev/examples/stream-whales/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Information about whales — an example of streamed structured response
validation.

This script streams structured responses from GPT-4 about whales, validates the
data and displays it as a dynamic table using as the data is received.

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/stream-whales/<../#usage>), run:

Should give an output like this:

```

  


    
  
  
  
    
  
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured



  
  
     'Average length of an adult whale in meters.'
  
  
    
      
      'Average weight of an adult whale in kilograms.' 
    
  
  
    

  

  
    
        
     
      
      'Generate me details of 5 species of Whale.'
      
       
           
        
             
              
          
           
           
                  
               
          
            
          
            
          
          
          'Streaming Structured responses from GPT-4'
          
        
         
        
         
         
        
         
             
          
            
            
            
                  
              
              
          
        

  
  
  

```

---

# Chat App with FastAPI
URL: https://ai.pydantic.dev/examples/chat-app/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Simple chat app example build with FastAPI.

This demonstrates storing chat history between requests and using it to give the
model context for new responses.

Most of the complex logic here is between which streams the response to the
browser, and which renders messages in the browser.

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/chat-app/<../#usage>), run:

Then open the app at .

Python code that runs the chat app:

```

     






  
  
  
  
    
  
  
       




    
     
     
  
  
  
  
  
  
  
  
  

# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured

  
  

  
      
      

  

    
      

    
"""Get the raw typescript code, it's compiled in the browser, forgive me."""

      

     
  

       
     
  
        
    
  



"""Format of messages sent to the browser."""

    
  
  

    
    
    
      
       
         
         
         
      
    
      
       
         
         
         
      
   'Unexpected message type for chat app:

  
        
  
    
"""Streams new line delimited JSON `Message`s to the client."""

    # stream the user prompt so that can be displayed straight away
     
      
        
           
           
           
        
      
       
    
    # get the chat history so far to pass as context to the agent
       
    # run the agent with the user prompt and the chat history
         
          
        # text here is a `str` and the frontend wants
        # JSON encoded ModelResponse, so we create one
           
           
    # add new messages (e.g. the user prompt and the agent response in this case) to the database
     
    

  
  



"""Rudimentary database to store chat messages in SQLite.

  The SQLite standard library package is synchronous, so we

  use a thread pool executor to run queries asynchronously.

  
  
  
  
  
    
          
    
     
        
        
           
          
    
       
    
       
  
      
      
      
      
    
      'CREATE TABLE IF NOT EXISTS messages (id INT PRIMARY KEY, message_list TEXT);'
    
    
     
      
     
      
      'INSERT INTO messages (message_list) VALUES (?);'
      
      
    
     
      
       
       'SELECT message_list FROM messages order by id'
    
       
       
       
      
     
  
            
    
      
     
     
      
     
    
           
    
       
      
       
       
    

  
  
  
      
  

```

Simple HTML page to render the app:

```



  
  
 Chat App

  


  "border rounded mx-auto my-5 p-4"

  Chat App

  Ask me anything...

    
  
    
  
  
      
    
     Send
  
  
    
   Error occurred, check the browser developer console for more information.

  


  


// to let me write TypeScript, without adding the burden of npm we do a dirty,
non-production-ready hack

// and transpile the TypeScript code in the browser

// this is (arguably) A neat demo trick, but not suitable for production!

```

TypeScript to handle rendering the messages, to keep this simple (and at the
risk of offending frontend developers) the typescript code is passed to the
browser as plain text and transpiled in the browser.

```

// BIG FAT WARNING: to avoid the complexity of npm, this typescript is compiled
in the browser

// there's currently no static type checking

// stream the response and render messages as each chunk is received

// data is sent as newline-delimited JSON

// The format of messages, this matches pydantic-ai both for brevity and
understanding

// in production, you might not want to keep this format all the way to the
frontend

// take raw response text and render messages into the `#conversation` element

// Message timestamp is assumed to be a unique identifier of a message, and is
used to deduplicate

// hence you can send data about the same message multiple times, and it will be
updated

// instead of creating a new message elements

// we use the timestamp as a crude element id

// call onSubmit when the form is submitted (e.g. user clicks the send button or
hits Enter)

// load messages on page load

```

---

# Question Graph
URL: https://ai.pydantic.dev/examples/question-graph/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Example of a graph for asking and evaluating questions.

With [dependencies installed and environment variables
set](https://ai.pydantic.dev/examples/question-graph/<../#usage>), run:

```

     
    
  
  


  
        
  
  
  
# 'if-token-present' means nothing will be sent (and the example will work) if
you don't have logfire configured

  



       
     
     



        
       
      'Ask a simple question with a single correct answer.'
      
    
      
      
     



       
        
        
     



  
  

  
  
  
  'Given a question and answer, evaluate if the answer is correct.'



  
    
    
     
      
        
       
         
      
    
      
     
       
    
       

  
  
    
      
     
    
     



  
        
    
    # > Comment: Vichy is no longer the capital of France.
      
     

  
       

  
    
    
      
  
     
           
        
            
        
        
         
          
      

     
    
    
    
     
     
  
  
      
        'expected last step to be a node'
      
         'answer is required to continue from history'
      
  
      
      
  
  
     
           
        
            
        
        
        
        
        
      
  

  
  
  
  
      
         
    
    
      
      ' uv run -m pydantic_ai_examples.question_graph mermaid
      
      ' uv run -m pydantic_ai_examples.question_graph continuous
      
      ' uv run -m pydantic_ai_examples.question_graph cli [answer]'
      
    
    
     
    
     
    
  
            
    

```

The mermaid diagram generated in this example looks like this:

---

# pydantic_ai.agent
URL: https://ai.pydantic.dev/api/agent/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Class for defining "agents" - a way to have a specific type of "conversation"
with an LLM.

Agents are generic in the dependency type they take and the result data type
they return, .

By default, if neither generic parameter is customised, agents have type .

```

  
  
  'What is the capital of France?'

```

```

  
"""Class for defining "agents" - a way to have a specific type of "conversation"
with an LLM.

  Agents are generic in the dependency type they take
[`AgentDeps`][pydantic_ai.tools.AgentDeps]

  and the result data type they return,
[`ResultData`][pydantic_ai.result.ResultData].

  By default, if neither generic parameter is customised, agents have type
`Agent[None, str]`.

  result = agent.run_sync('What is the capital of France?')

  # we use dataclass fields in order to conveniently know what attributes are
available

       
"""The default model configured for this agent."""

     
"""The name of the agent, used for logging.

  If `None`, we try to infer the agent name from the call frame when the agent
is first run.

  
"""Strategy for handling tool calls when a final result is found."""

     
"""Optional model request settings to use for this agents's runs, by default.

  Note, if `model_settings` is provided by `run`, `run_sync`, or `run_stream`,
those settings will

  be merged with this value, with the runtime argument taking priority.

     
       
       
      
      
      
     
     
      
    
  
     
     
      
      
  
    
           
    
       
         
       
         
         
       
       
         
         
          
       
       
  

      model: The default model to use for this agent, if not provide,
        you must provide the model when calling it.
      result_type: The type of the result data, used to validate the result data, defaults to `str`.
      system_prompt: Static system prompts to use for this agent, you can also register system
        prompts via a function with [`system_prompt`][pydantic_ai.Agent.system_prompt].
      deps_type: The type used for dependency injection, this parameter exists solely to allow you to fully
        parameterize the agent, and therefore get the best out of static type checking.
        If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright
        or add a type hint `: Agent[None, <return type>]`.
      name: The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame
        when the agent is first run.
      model_settings: Optional model request settings to use for this agent's runs, by default.
      retries: The default number of retries to allow before raising an error.
      result_tool_name: The name of the tool to use for the final result.
      result_tool_description: The description of the final result tool.
      result_retries: The maximum number of retries to allow for result validation, defaults to `retries`.
      tools: Tools to register with the agent, you can also register tools via the decorators

      defer_model_check: by default, if you provide a [named][pydantic_ai.models.KnownModelName] model,
        it's evaluated to create a [`Model`][pydantic_ai.models.Model] instance immediately,
        which checks for the necessary environment variables. Set this to `false`
        to defer the evaluation until the first run. Useful if you want to
        [override the model][pydantic_ai.Agent.override] for testing.
      end_strategy: Strategy for handling tool calls that are requested alongside a final result.
        See [`EndStrategy`][pydantic_ai.agent.EndStrategy] for more information.

         
        
    
        
      
      
      
      
      
      
        
    
           
      
      
       
        
        
      
        
      
      
      
             
      
  
    
    
     
    
       
         
           
       
         
         
         
       
     
  
    
    
     
    
     
         
           
       
         
         
         
       
     
    
    
     
    
         
           
       
         
         
         
         
       
    
"""Run the agent with a user prompt in async mode.

      result = await agent.run('What is the capital of France?')

      result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
        result validators since result validators would expect an argument that matches the agent's result type.
      user_prompt: User input to start/continue the conversation.
      message_history: History of the conversation so far.
      model: Optional model to use for this run, required if `model` was not set when creating the agent.
      deps: Optional dependencies to use for this run.
      model_settings: Optional settings to use for this model's request.
      usage_limits: Optional limits on model request count or token usage.
      usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
      infer_name: Whether to try to infer the agent name from the call frame if it's not set.

      The result of the run.

         
      
       
      
          
      
     
      
      
      
      
        
      
             
           
        
         
          
         
          
       
        
          
         'preparing model and tools {run_step=}' 
              
            
               
           
           
        
         
        
            
              
              
          
           
            # Add parts to the conversation as a new message
            
          # Check if we got a final result
              
              
              
             
             
             
              'handle model response -> final result'
             
                  
            
          
            
             
                  
              
  
  
    
     
    
         
           
       
         
         
         
       
     
  
  
    
     
    
       
         
           
       
         
         
         
       
     
  
    
     
    
         
         
           
       
         
         
         
       
    
"""Run the agent with a user prompt synchronously.

    This is a convenience method that wraps [`self.run`][pydantic_ai.Agent.run] with `loop.run_until_complete(...)`.
    You therefore can't use this method inside async code or if there's an active event loop.

    result_sync = agent.run_sync('What is the capital of Italy?')

      result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
        result validators since result validators would expect an argument that matches the agent's result type.
      user_prompt: User input to start/continue the conversation.
      message_history: History of the conversation so far.
      model: Optional model to use for this run, required if `model` was not set when creating the agent.
      deps: Optional dependencies to use for this run.
      model_settings: Optional settings to use for this model's request.
      usage_limits: Optional limits on model request count or token usage.
      usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
      infer_name: Whether to try to infer the agent name from the call frame if it's not set.

      The result of the run.

         
      
     
      
        
        
        
        
        
        
        
        
        
      
    
  
  
    
     
    
       
         
           
       
         
         
         
       
      
  
  
    
     
    
     
         
           
       
         
         
         
       
      
  
    
    
     
    
         
         
           
       
         
         
         
       
     
"""Run the agent with a user prompt in async mode, returning a streamed
response.

      async with agent.run_stream('What is the capital of the UK?') as response:

      result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
        result validators since result validators would expect an argument that matches the agent's result type.
      user_prompt: User input to start/continue the conversation.
      message_history: History of the conversation so far.
      model: Optional model to use for this run, required if `model` was not set when creating the agent.
      deps: Optional dependencies to use for this run.
      model_settings: Optional settings to use for this model's request.
      usage_limits: Optional limits on model request count or token usage.
      usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
      infer_name: Whether to try to infer the agent name from the call frame if it's not set.

      The result of the run.

         
      # f_back because `asynccontextmanager` adds one frame
          
        
       
      
          
      
     
      
      
      
      
        
      
             
           
        
         
          
         
          
       
          
        
         'preparing model and tools {run_step=}' 
              
            
               
              
             
            # We want to end the "model request" span here, but we can't exit the context manager
            # in the traditional way
              
               
                 
                  
              
              # Check if we got a final result
                
                  
                  
                  'handle model response -> final result'
                  
"""Called when the stream has completed.

                  The model response will have been added to messages by now

                    
                    
                    
                           
                  
                     
                       
                  
                   
                    
                   
                 
                  
                  
                  
                  
                  
                  
                  
                  
                  
                
                
              
                
                   
                # if we got a model response add that to messages
                
                 
                  # if we got one or more tool response parts, add a model request message
                  
                 
                      
                  
                # the model_response should have been fully streamed by now, we can add its usage
                  
                
                
  
  
    
    
         
           
    
"""Context manager to temporarily override agent dependencies and model.

    This is particularly useful when testing.
    You can find an example of this [here](../testing-evals.md#overriding-model-via-pytest-fixtures).

      deps: The dependencies to use instead of the dependencies passed to the agent run.
      model: The model to use instead of the model passed to the agent run.

     
        
        
    
        
    
     
        
      
         
    
        
    
      
    
       
          
       
          
  
  
        
      
  
  
        
      
  
           
  
           
  
  
          
      
  
    
         
    
    
       
    
     
     
  
"""Decorator to register a system prompt function.

    Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.
    Can decorate a sync or async functions.
    The decorator can be used either bare (`agent.system_prompt`) or as a function call
    (`agent.system_prompt(...)`), see the examples below.
    Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure
    the type of the function, see `tests/typed_agent.py` for tests.

      func: The function to decorate
      dynamic: If True, the system prompt will be reevaluated even when `messages_history` is provided,

    from pydantic_ai import Agent, RunContext

    async def async_system_prompt(ctx: RunContext[str]) -> str:
      return f'{ctx.deps} is the best'

       
       
         
        
           
        
         
            
         
       
    
         "dynamic can't be True in this case"
       
       
  
  
         
       
  
  
         
       
  
           
  
  
        
      
  
        
     
"""Decorator to register a result validator function.

    Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.
    Can decorate a sync or async functions.
    Overloads for every possible signature of `result_validator` are included so the decorator doesn't obscure
    the type of the function, see `tests/typed_agent.py` for tests.

    from pydantic_ai import Agent, ModelRetry, RunContext

    def result_validator_simple(data: str) -> str:

    async def result_validator_deps(ctx: RunContext[str], data: str) -> str:

    #> success (no tool calls)

     
     
  
           
  
  
    
    
    
         
         
       
       
        
  
    
          
    
    
         
         
       
       
    
"""Decorator to register a tool function which takes
[`RunContext`][pydantic_ai.tools.RunContext] as its first argument.

    Can decorate a sync or async functions.
    The docstring is inspected to extract both the tool description and description of each parameter,

    We can't add overloads for every possible signature of tool, since the return type is a recursive union
    so the signature of functions decorated with `@agent.tool` is obscured.

    from pydantic_ai import Agent, RunContext

    def foobar(ctx: RunContext[int], x: int) -> int:

    async def spam(ctx: RunContext[str], y: float) -> float:

      func: The tool function to register.
      retries: The number of retries to allow for this tool, defaults to the agent's default retries,

      prepare: custom method to prepare the tool definition for each step, return `None` to omit this
        tool from a given step. This is useful if you want to customise a tool at call time,
        or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
      docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
        Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
      require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.

       
       
          
         
        
             
         
       
    
      
           
       
  
         
  
  
    
    
    
         
         
       
       
      
  
    
         
    
    
         
         
       
       
    
"""Decorator to register a tool function which DOES NOT take `RunContext` as an
argument.

    Can decorate a sync or async functions.
    The docstring is inspected to extract both the tool description and description of each parameter,

    We can't add overloads for every possible signature of tool, since the return type is a recursive union
    so the signature of functions decorated with `@agent.tool` is obscured.

    from pydantic_ai import Agent, RunContext

    def foobar(ctx: RunContext[int]) -> int:

    async def spam(ctx: RunContext[str]) -> float:

      func: The tool function to register.
      retries: The number of retries to allow for this tool, defaults to the agent's default retries,

      prepare: custom method to prepare the tool definition for each step, return `None` to omit this
        tool from a given step. This is useful if you want to customise a tool at call time,
        or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
      docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
        Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
      require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.

       
          
        
        
               
        
         
       
    
           
       
  
    
      
     
       
       
     
     
    
"""Private utility to register a function as a tool."""

             
      
      
      
      
      
      
      
    
    
       
"""Private utility to register a tool instance."""

       
      
         
       
       'Tool name conflicts with existing tool: 
         
       'Tool name conflicts with result schema name: 
      
            
"""Create a model configured for this agent.

      model: model to use for this run, required if `model` was not set when creating the agent.

     
       
      # we don't want `override()` to cover up errors from the model not being defined, hence this check
             
         
          '`model` must be set either when creating the agent or when calling it. '
          '(Even when `override(model=...)` is customizing the model that will actually be called)'
        
        
        
        
        
      
          
    
       '`model` must be set either when creating the agent or when calling it.'
     
    
          
    
"""Build tools and create an agent model."""

       
         
         
          
        
      
      
      
      
             
    
    
        
    
"""Reevaluate any `SystemPromptPart` with dynamic_ref in the provided messages
by running the associated runner function."""

    # Only proceed if there's at least one dynamic runner.
     
         
          
              
                
              # Look up the runner by its ref
                 
                   
                  
                   
                
  
        
      
        
       
         'Cannot set a custom run `result_type` when the agent has result validators'
       
          
      
    
        
    
            
    
    
        
     
         
    
       
          
      
          
          
     
      
      
      # Reevaluate any dynamic system prompt parts
        
      
    
         
      
      
     
    
    
     
     
       
       
"""Process a non-streamed response from the model.

      A tuple of `(final_result, request parts)`. If `final_result` is not `None`, the conversation should end.

       
       
       
        
        # ignore empty content for text parts, see #437
         
          
      
        
    # At the moment, we prioritize at least executing tool calls if they are present.
    # In the future, we'd consider making this configurable at the agent or run level.
    # This accounts for cases like anthropic returns that might contain a text response
    # and a tool call response, where the text response just indicates the tool call will happen.
     
          
     
        
          
    
       
    
            
       
"""Handle a plain text response from the model for non-streaming responses."""

     
         
      
             
         
        
          
      
           
    
      
        
        'Plain text responses are not permitted, please call one of the functions instead.'
      
        
    
    
     
     
       
       
"""Handle a structured response containing tool calls from the model for non-
streaming responses."""

      'Expected at least one tool call'
    # first look for the result tool call
         
       
        
         
           
        
            
               
           
          
          
        
             
    # Then build the other request parts based on end strategy
       
           
    
      
    
    
     
       
     
       
    
"""Process function (non-result) tool calls in parallel.

    Also add stub return parts for any other tools that need it.

       
       
          
    # we rely on the fact that if we found a result, it's the first result tool in the last
      
       
            
          
        
          
            
            
            
          
        
         
         
          
            
              
              'Tool not executed - a final result was already processed.'
              
            
          
        
            
              
        # if tool_name is in _result_schema, it means we found a result tool but an error occurred in
        # validation, we don't add another part here
            
          
            
              
              'Result tool not used - a final result was already processed.'
              
            
          
      
          
    # Run all tool tasks in parallel
     
            
            
        
     
    
    
     
     
       
       
"""Process a streamed response from the model.

      Either a final result or a tuple of the model response and the tool responses for the next request.
      If a final result is returned, the conversation should end.

      
        
        
          
          
            
           
              
          
                  
               
              
        
          
       
       
      
      
       
       
        
           
            
        
            
           
      # Can only get here if self._allow_text_result returns `False` for the provided result_schema
      
        
        'Plain text responses are not permitted, please call one of the functions instead.'
      
        
          
          
      
      
    
    
     
     
       
    
     
         
         
             
        
    
       
       
      
       
       
        
      
        
"""Build the initial messages for the conversation."""

           
       
         
       
         
      
        
     
  
    
     
     
       
    
    
      
     
      
     
        
    
        
     
       
"""Get deps for a run.

    If we've overridden deps via `_override_deps`, use that, otherwise use the deps passed to the call.
    We could do runtime type checking of deps against `self._deps_type`, but that's a slippery slope.

       
       
    
       
         
"""Infer the agent name from the call frame.

        
         
          
            
             
              
            
           
          # if we couldn't find the agent in locals and globals are a different dict, try globals
              
               
                
              
  
        
         
  
  
    'The `last_run_messages` attribute has been removed, use `capture_run_messages` instead.' 
  
     
     'The `last_run_messages` attribute has been removed, use `capture_run_messages` instead.'

```

  
---  
The default model configured for this agent.

The default model to use for this agent, if not provide, you must provide the
model when calling it.  
---  
The type of the result data, used to validate the result data, defaults to .  
Static system prompts to use for this agent, you can also register system
prompts via a function with .  
The type used for dependency injection, this parameter exists solely to allow
you to fully parameterize the agent, and therefore get the best out of static
type checking. If you're not using deps, but want type checking to pass, you can
set to satisfy Pyright or add a type hint .  
The name of the agent, used for logging. If , we try to infer the agent name
from the call frame when the agent is first run.  
Optional model request settings to use for this agent's runs, by default.  
The default number of retries to allow before raising an error.  
The name of the tool to use for the final result.  
The description of the final result tool.  
The maximum number of retries to allow for result validation, defaults to .  
Tools to register with the agent, you can also register tools via the decorators
and .  
by default, if you provide a model, it's evaluated to create a instance
immediately, which checks for the necessary environment variables. Set this to
to defer the evaluation until the first run. Useful if you want to for testing.  
Strategy for handling tool calls that are requested alongside a final result.
See for more information.  
```



  
         
  
     
       
     
       
       
     
     
       
       
        
     
     

    model: The default model to use for this agent, if not provide,
      you must provide the model when calling it.
    result_type: The type of the result data, used to validate the result data, defaults to `str`.
    system_prompt: Static system prompts to use for this agent, you can also register system
      prompts via a function with [`system_prompt`][pydantic_ai.Agent.system_prompt].
    deps_type: The type used for dependency injection, this parameter exists solely to allow you to fully
      parameterize the agent, and therefore get the best out of static type checking.
      If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright
      or add a type hint `: Agent[None, <return type>]`.
    name: The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame
      when the agent is first run.
    model_settings: Optional model request settings to use for this agent's runs, by default.
    retries: The default number of retries to allow before raising an error.
    result_tool_name: The name of the tool to use for the final result.
    result_tool_description: The description of the final result tool.
    result_retries: The maximum number of retries to allow for result validation, defaults to `retries`.
    tools: Tools to register with the agent, you can also register tools via the decorators

    defer_model_check: by default, if you provide a [named][pydantic_ai.models.KnownModelName] model,
      it's evaluated to create a [`Model`][pydantic_ai.models.Model] instance immediately,
      which checks for the necessary environment variables. Set this to `false`
      to defer the evaluation until the first run. Useful if you want to
      [override the model][pydantic_ai.Agent.override] for testing.
    end_strategy: Strategy for handling tool calls that are requested alongside a final result.
      See [`EndStrategy`][pydantic_ai.agent.EndStrategy] for more information.

       
      
  
      
    
    
    
    
    
    
      
  
         
    
    
     
      
      
    
      
    
    
    
           
    

```

  
---  
Strategy for handling tool calls when a final result is found.

The name of the agent, used for logging.

If , we try to infer the agent name from the call frame when the agent is first
run.

Optional model request settings to use for this agents's runs, by default.

Note, if is provided by , , or , those settings will be merged with this value,
with the runtime argument taking priority.

Run the agent with a user prompt in async mode.

```

  
  
  
     'What is the capital of France?'
  
  

```

Custom result type to use for this run, may only be used if the agent has no
result validators since result validators would expect an argument that matches
the agent's result type.  
---  
User input to start/continue the conversation.  
History of the conversation so far.  
Optional model to use for this run, required if was not set when creating the
agent.  
Optional dependencies to use for this run.  
Optional settings to use for this model's request.  
Optional limits on model request count or token usage.  
Optional usage to start with, useful for resuming a conversation or agents used
in tools.  
Whether to try to infer the agent name from the call frame if it's not set.  
The result of the run.  
---  
```

  
  
  
  
       
         
     
       
       
       
       
     
  
"""Run the agent with a user prompt in async mode.

    result = await agent.run('What is the capital of France?')

    result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
      result validators since result validators would expect an argument that matches the agent's result type.
    user_prompt: User input to start/continue the conversation.
    message_history: History of the conversation so far.
    model: Optional model to use for this run, required if `model` was not set when creating the agent.
    deps: Optional dependencies to use for this run.
    model_settings: Optional settings to use for this model's request.
    usage_limits: Optional limits on model request count or token usage.
    usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
    infer_name: Whether to try to infer the agent name from the call frame if it's not set.

    The result of the run.

       
    
     
    
        
    
  
    
    
    
    
      
    
           
         
      
       
        
       
        
     
      
        
       'preparing model and tools {run_step=}' 
            
          
             
         
         
      
       
      
          
            
            
        
         
          # Add parts to the conversation as a new message
          
        # Check if we got a final result
            
            
            
           
           
           
            'handle model response -> final result'
           
                
          
        
          
           
                
            

```

  
---  
Run the agent with a user prompt synchronously.

This is a convenience method that wraps with . You therefore can't use this
method inside async code or if there's an active event loop.

```

  
  
  'What is the capital of Italy?'

```

Custom result type to use for this run, may only be used if the agent has no
result validators since result validators would expect an argument that matches
the agent's result type.  
---  
User input to start/continue the conversation.  
History of the conversation so far.  
Optional model to use for this run, required if was not set when creating the
agent.  
Optional dependencies to use for this run.  
Optional settings to use for this model's request.  
Optional limits on model request count or token usage.  
Optional usage to start with, useful for resuming a conversation or agents used
in tools.  
Whether to try to infer the agent name from the call frame if it's not set.  
The result of the run.  
---  
```



  
  
  
       
       
         
     
       
       
       
     
  
"""Run the agent with a user prompt synchronously.

  This is a convenience method that wraps [`self.run`][pydantic_ai.Agent.run]
with `loop.run_until_complete(...)`.

  You therefore can't use this method inside async code or if there's an active
event loop.

  result_sync = agent.run_sync('What is the capital of Italy?')

    result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
      result validators since result validators would expect an argument that matches the agent's result type.
    user_prompt: User input to start/continue the conversation.
    message_history: History of the conversation so far.
    model: Optional model to use for this run, required if `model` was not set when creating the agent.
    deps: Optional dependencies to use for this run.
    model_settings: Optional settings to use for this model's request.
    usage_limits: Optional limits on model request count or token usage.
    usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
    infer_name: Whether to try to infer the agent name from the call frame if it's not set.

    The result of the run.

       
    
  
    
      
      
      
      
      
      
      
      
      
    
  

```

  
---  
Run the agent with a user prompt in async mode, returning a streamed response.

```

  
  
  
    'What is the capital of the UK?'  
     
    

```

Custom result type to use for this run, may only be used if the agent has no
result validators since result validators would expect an argument that matches
the agent's result type.  
---  
User input to start/continue the conversation.  
History of the conversation so far.  
Optional model to use for this run, required if was not set when creating the
agent.  
Optional dependencies to use for this run.  
Optional settings to use for this model's request.  
Optional limits on model request count or token usage.  
Optional usage to start with, useful for resuming a conversation or agents used
in tools.  
Whether to try to infer the agent name from the call frame if it's not set.  
The result of the run.  
---  
```

  
  
  
  
       
       
         
     
       
       
       
     
  
"""Run the agent with a user prompt in async mode, returning a streamed
response.

    async with agent.run_stream('What is the capital of the UK?') as response:

    result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
      result validators since result validators would expect an argument that matches the agent's result type.
    user_prompt: User input to start/continue the conversation.
    message_history: History of the conversation so far.
    model: Optional model to use for this run, required if `model` was not set when creating the agent.
    deps: Optional dependencies to use for this run.
    model_settings: Optional settings to use for this model's request.
    usage_limits: Optional limits on model request count or token usage.
    usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
    infer_name: Whether to try to infer the agent name from the call frame if it's not set.

    The result of the run.

       
    # f_back because `asynccontextmanager` adds one frame
        
      
     
    
        
    
  
    
    
    
    
      
    
           
         
      
       
        
       
        
     
        
      
       'preparing model and tools {run_step=}' 
            
          
             
            
           
          # We want to end the "model request" span here, but we can't exit the context manager
          # in the traditional way
            
             
               
                
            
            # Check if we got a final result
              
                
                
                'handle model response -> final result'
                
"""Called when the stream has completed.

                The model response will have been added to messages by now

                  
                  
                  
                         
                
                   
                     
                
                 
                  
                 
               
                
                
                
                
                
                
                
                
                
              
              
            
              
                 
              # if we got a model response add that to messages
              
               
                # if we got one or more tool response parts, add a model request message
                
               
                    
                
              # the model_response should have been fully streamed by now, we can add its usage
                
              
              

```

  
---  
Context manager to temporarily override agent dependencies and model.

This is particularly useful when testing. You can find an example of this .

The dependencies to use instead of the dependencies passed to the agent run.  
---  
The model to use instead of the model passed to the agent run.  
```



  
  
       
         
  
"""Context manager to temporarily override agent dependencies and model.

  This is particularly useful when testing.

  You can find an example of this [here](../testing-evals.md#overriding-model-
via-pytest-fixtures).

    deps: The dependencies to use instead of the dependencies passed to the agent run.
    model: The model to use instead of the model passed to the agent run.

  
      
      
  
      
  
  
      
    
       
  
      
  
    
  
     
        
     
        

```

  
---  
Decorator to register a system prompt function.

Optionally takes as its only argument. Can decorate a sync or async functions.

The decorator can be used either bare () or as a function call (), see the
examples below.

Overloads for every possible signature of are included so the decorator doesn't
obscure the type of the function, see for tests.  
If True, the system prompt will be reevaluated even when is provided, see  
```



  
       
  
  
     
  
  
  

"""Decorator to register a system prompt function.

  Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only
argument.

  Can decorate a sync or async functions.

  The decorator can be used either bare (`agent.system_prompt`) or as a function
call

  (`agent.system_prompt(...)`), see the examples below.

  Overloads for every possible signature of `system_prompt` are included so the
decorator doesn't obscure

  the type of the function, see `tests/typed_agent.py` for tests.

    func: The function to decorate
    dynamic: If True, the system prompt will be reevaluated even when `messages_history` is provided,

  from pydantic_ai import Agent, RunContext

  async def async_system_prompt(ctx: RunContext[str]) -> str:

    return f'{ctx.deps} is the best'

     
     
       
      
         
      
       
          
       
     
  
       "dynamic can't be True in this case"
     
     

```

  
---  
Decorator to register a result validator function.

Optionally takes as its first argument. Can decorate a sync or async functions.

Overloads for every possible signature of are included so the decorator doesn't
obscure the type of the function, see for tests.

```

     
  

    
     
     
  

       
     
     
  
  

#> success (no tool calls)

```

```



      
  
"""Decorator to register a result validator function.

  Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its first
argument.

  Can decorate a sync or async functions.

  Overloads for every possible signature of `result_validator` are included so
the decorator doesn't obscure

  the type of the function, see `tests/typed_agent.py` for tests.

  from pydantic_ai import Agent, ModelRetry, RunContext

  def result_validator_simple(data: str) -> str:

  async def result_validator_deps(ctx: RunContext[str], data: str) -> str:

  #> success (no tool calls)

  
  

```

  
---  
Decorator to register a tool function which takes as its first argument.

Can decorate a sync or async functions.

The docstring is inspected to extract both the tool description and description
of each parameter, .

We can't add overloads for every possible signature of tool, since the return
type is a recursive union so the signature of functions decorated with is
obscured.

The tool function to register.  
---  
The number of retries to allow for this tool, defaults to the agent's default
retries, which defaults to 1.  
custom method to prepare the tool definition for each step, return to omit this
tool from a given step. This is useful if you want to customise a tool at call
time, or omit it completely from a step. See .  
The format of the docstring, see . Defaults to , such that the format is
inferred from the structure of the docstring.  
If True, raise an error if a parameter description is missing. Defaults to
False.  
```



  
        
  
  
       
       
     
     
  
"""Decorator to register a tool function which takes
[`RunContext`][pydantic_ai.tools.RunContext] as its first argument.

  Can decorate a sync or async functions.

  The docstring is inspected to extract both the tool description and
description of each parameter,

  We can't add overloads for every possible signature of tool, since the return
type is a recursive union

  so the signature of functions decorated with `@agent.tool` is obscured.

  from pydantic_ai import Agent, RunContext

  def foobar(ctx: RunContext[int], x: int) -> int:

  async def spam(ctx: RunContext[str], y: float) -> float:

    func: The tool function to register.
    retries: The number of retries to allow for this tool, defaults to the agent's default retries,

    prepare: custom method to prepare the tool definition for each step, return `None` to omit this
      tool from a given step. This is useful if you want to customise a tool at call time,
      or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
    docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
      Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
    require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.

     
     
        
       
      
           
       
     
  
    
         
     

```

  
---  
Decorator to register a tool function which DOES NOT take as an argument.

Can decorate a sync or async functions.

The docstring is inspected to extract both the tool description and description
of each parameter, .

We can't add overloads for every possible signature of tool, since the return
type is a recursive union so the signature of functions decorated with is
obscured.

The tool function to register.  
---  
The number of retries to allow for this tool, defaults to the agent's default
retries, which defaults to 1.  
custom method to prepare the tool definition for each step, return to omit this
tool from a given step. This is useful if you want to customise a tool at call
time, or omit it completely from a step. See .  
The format of the docstring, see . Defaults to , such that the format is
inferred from the structure of the docstring.  
If True, raise an error if a parameter description is missing. Defaults to
False.  
```



  
       
  
  
       
       
     
     
  
"""Decorator to register a tool function which DOES NOT take `RunContext` as an
argument.

  Can decorate a sync or async functions.

  The docstring is inspected to extract both the tool description and
description of each parameter,

  We can't add overloads for every possible signature of tool, since the return
type is a recursive union

  so the signature of functions decorated with `@agent.tool` is obscured.

  from pydantic_ai import Agent, RunContext

  def foobar(ctx: RunContext[int]) -> int:

  async def spam(ctx: RunContext[str]) -> float:

    func: The tool function to register.
    retries: The number of retries to allow for this tool, defaults to the agent's default retries,

    prepare: custom method to prepare the tool definition for each step, return `None` to omit this
      tool from a given step. This is useful if you want to customise a tool at call time,
      or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
    docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
      Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
    require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.

     
        
      
      
             
      
       
     
  
         
     

```

  
---  
The strategy for handling multiple tool calls when a final result is found.

  * : Stop processing other tool calls once a final result is found
  * : Process all tool calls even after finding a final result

Type variable for the result data of a run where was customized on the run call.

Context manager to access the messages used in a , , or call.

Useful when a run may raise an exception, see for more information.

If you call , , or more than once within a single context, will represent the
messages exchanged during the first call only.

```

  
"""Context manager to access the messages used in a
[`run`][pydantic_ai.Agent.run], [`run_sync`][pydantic_ai.Agent.run_sync], or
[`run_stream`][pydantic_ai.Agent.run_stream] call.

  Useful when a run may raise an exception, see [model
errors](../agents.md#model-errors) for more information.

  from pydantic_ai import Agent, capture_run_messages

    If you call `run`, `run_sync`, or `run_stream` more than once within a single `capture_run_messages` context,
    `messages` will represent the messages exchanged during the first call only.

  
     
  
       
      
    
       
    
      

```

  
---

---

# pydantic_ai.tools
URL: https://ai.pydantic.dev/api/tools/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Type variable for agent dependencies.

Information about the current call.

```



"""Information about the current call."""

  

  
"""The model used in this run."""

  
"""LLM usage associated with the run."""

  
"""The original user prompt passed to the run."""

     
"""Messages exchanged in the conversation so far."""

       
"""Name of the tool being called."""

     
"""Number of retries so far."""

     
"""The current step in the run."""

  
                  
    
    # Create a new `RunContext` a new `retry` value and `tool_name`.
      
        
        
        
        
      

```

  
---  
The model used in this run.

LLM usage associated with the run.

The original user prompt passed to the run.

Messages exchanged in the conversation so far.

Name of the tool being called.

Number of retries so far.

The current step in the run.

A function that may or maybe not take as an argument, and may or may not be
async.

A tool function that takes as the first argument.

A tool function that does not take as the first argument.

Either kind of tool function.

This is just a union of and .

```

  
  "Callable[[RunContext[AgentDeps], ToolDefinition], Awaitable[ToolDefinition | None]]"

```

Definition of a function that can prepare a tool definition at call time.

Example — here is valid as a :

  * — Automatically infer the format based on the structure of the docstring.

A tool function for an agent.

```



"""A tool function for an agent."""

  
  
     
  
  
     
  
  
     
       
     
       
      
     
      
  
    
     
    
         
         
         
         
         
       
       
  
"""Create a new tool instance.

    from pydantic_ai import Agent, RunContext, Tool
    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:

    or with a custom prepare method:

    from pydantic_ai import Agent, RunContext, Tool

    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:

      # only register the tool if `deps == 42`

    agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])

      function: The Python function to call as the tool.
      takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
        this is inferred if unset.
      max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
      name: Name of the tool, inferred from the function if `None`.
      description: Description of the tool, inferred from the function if `None`.
      prepare: custom method to prepare the tool definition for each step, return `None` to omit this
        tool from a given step. This is useful if you want to customise a tool at call time,
        or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
      docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
        Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
      require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.

       
        
         
      
      
      
        
        
      
      
      
      
      
      
      
      
      
          

    By default, this method creates a tool definition, then either returns it, or calls `self.prepare`

      return a `ToolDefinition` or `None` if the tools should not be registered for this run.

      
      
      
      
    
        
         
    
       
    
        
    
"""Run the tool function asynchronously."""

    
        
          
      
          
       
        
         
    
       
            
            
      
            
             
       
        
      
     
      
      
      
    
  
    
      
     
     
      
     
         
        
          
       
      
     
      
      
  
          
    
      
           
       'Tool exceeded max retries count of   
    
        
          
      
          
       
        
        
        
      

```

  
---  
Create a new tool instance.

or with a custom prepare method:

```

  
     
  
         
  
  
     
  
  # only register the tool if `deps == 42`

     
     
    

```

The Python function to call as the tool.  
---  
Whether the function takes a first argument, this is inferred if unset.  
Maximum number of retries allowed for this tool, set to the agent default if .  
Name of the tool, inferred from the function if .  
Description of the tool, inferred from the function if .  
custom method to prepare the tool definition for each step, return to omit this
tool from a given step. This is useful if you want to customise a tool at call
time, or omit it completely from a step. See .  
The format of the docstring, see . Defaults to , such that the format is
inferred from the structure of the docstring.  
If True, raise an error if a parameter description is missing. Defaults to
False.  
```



  
  
  
       
       
       
       
       
     
     

"""Create a new tool instance.

  from pydantic_ai import Agent, RunContext, Tool

  async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:

  or with a custom prepare method:

  from pydantic_ai import Agent, RunContext, Tool

  async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:

    # only register the tool if `deps == 42`

  agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])

    function: The Python function to call as the tool.
    takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
      this is inferred if unset.
    max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
    name: Name of the tool, inferred from the function if `None`.
    description: Description of the tool, inferred from the function if `None`.
    prepare: custom method to prepare the tool definition for each step, return `None` to omit this
      tool from a given step. This is useful if you want to customise a tool at call time,
      or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
    docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
      Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
    require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.

     
      
       
    
    
    
      
      
    
    
    
    
    
    
    
    
    

```

  
---  
By default, this method creates a tool definition, then either returns it, or
calls if it's set.

return a or if the tools should not be registered for this run.  
---  
```

        

  By default, this method creates a tool definition, then either returns it, or
calls `self.prepare`

    return a `ToolDefinition` or `None` if the tools should not be registered for this run.

    
    
    
    
  
      
       
  
     

```

  
---  
Run the tool function asynchronously.

```

  
      
  
"""Run the tool function asynchronously."""

  
      
        
    
        
     
      
       
  
     
          
          
    
          
           
     
      
    
  
    
    
    
  

```

  
---  
Type representing JSON schema of an object, e.g. where .

This type is used to define tools parameters (aka arguments) in .

With PEP-728 this should be a TypedDict with , and

Definition of a tool passed to a model.

This is used for both function tools result tools.

```



"""Definition of a tool passed to a model.

  This is used for both function tools result tools.

  
"""The name of the tool."""

  
"""The description of the tool."""

  
"""The JSON schema for the tool's parameters."""

       
"""The key in the outer [TypedDict] that wraps a result tool.

  This will only be set for result tools which don't have an `object` JSON
schema.

```

  
---  
The name of the tool.

The description of the tool.

The JSON schema for the tool's parameters.

The key in the outer [TypedDict] that wraps a result tool.

This will only be set for result tools which don't have an JSON schema.

---

# pydantic_ai.result
URL: https://ai.pydantic.dev/api/result/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Type variable for the result data of a run.

A function that always takes and returns and:

  * may or may not take as a first argument
  * may or may not be async

Result of a non-streamed run.

```



"""Result of a non-streamed run."""

  
"""Data from the final response in the run."""

     
  
     
"""Return the usage of the whole run."""

     
            
"""Return the history of _messages.

      result_tool_return_content: The return content of the tool call to set in the last message.
        This provides a convenient way to modify the content of the result tool call if you want to continue
        the conversation and want to set the response to the result tool call. If `None`, the last message will

        
       
    
       
       
"""Set return content for the result tool.

    Useful if you want to continue the conversation and want to set the response to the result tool call.

      
       'Cannot set result tool return content when the return type is `str`.'
      
      
       
            
          
         
     'No tool call found with tool name 

```

  
---  
Return all messages from as JSON bytes.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
JSON bytes representing the messages.  
---  
```

          
"""Return all messages from
[`all_messages`][pydantic_ai.result._BaseRunResult.all_messages] as JSON bytes.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

    JSON bytes representing the messages.

  
    
  

```

  
---  
Return new messages associated with this run.

Messages from older runs are excluded.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
```

          
"""Return new messages associated with this run.

  Messages from older runs are excluded.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

    

```

  
---  
Return new messages from as JSON bytes.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
JSON bytes representing the new messages.  
---  
```

          
"""Return new messages from
[`new_messages`][pydantic_ai.result._BaseRunResult.new_messages] as JSON bytes.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

    JSON bytes representing the new messages.

  
    
  

```

  
---  
Data from the final response in the run.

Return the usage of the whole run.

```

  
"""Return the usage of the whole run."""

  

```

  
---  
Return the history of _messages.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
```

          
"""Return the history of _messages.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

      
     
  
     

```

  
---  
Result of a streamed run that returns structured data via a tool call.

```

  
"""Result of a streamed run that returns structured data via a tool call."""

     
  
     
  
    
     
    
      
"""Whether the stream has all been received.

  This is set to `True` when one of

             
"""Stream the response as an async iterable.

    The pydantic validator for structured data will be called in

      debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
        Debouncing is particularly important for long structured responses to reduce the overhead of
        performing validation as each token is received.

      An async iterable of the response data.

         
           
       
                 
"""Stream the text result as an async iterable.

      Result validators will NOT be called on the text result if `delta=True`.

      delta: if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text
        up to the current point.
      debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
        Debouncing is particularly important for long structured responses to reduce the overhead of
        performing validation as each token is received.

        
       'stream_text() can only be used with text responses'
      
        
    
    # Define a "merged" version of the iterator that will yield items that have already been retrieved
    # and items that we receive while streaming. We define a dedicated async iterator for this so we can
    # pass the combined stream to the group_by_temporal function within `_stream_text_deltas` below.
         
      # if the response currently has any parts with content, yield those before streaming
        
          
            
            
          
         
           
            
           
        
            
         
           
            
           
        
            
        
           
            
                
       
       
            
           
      
        # a quick benchmark shows it's faster to build up a string with concat when we're
        # yielding at each step
           
          
            
          
            
             
           
         
         
    
           
     
"""Stream the response as an async iterable of Structured LLM Messages.

      debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
        Debouncing is particularly important for long structured responses to reduce the overhead of
        performing validation as each token is received.

      An async iterable of the structured response message and whether that is the last message.

      
        
    
       
      # if the message currently has any parts with content, yield before streaming
        
         
         
            
          
           
            
            
            
          
          
        # TODO: Should this now be `final_response` instead of `structured_response`?
         
         
      
"""Stream the whole response, validate and return it."""

      
        
    
        
      
      
     
      
     
"""Return the usage of the whole run.

      This won't return the full usage until the stream is finished.

       
     
"""Get the timestamp of the response."""

     
    
           
    
"""Validate a structured result message."""

             
         
         
         
          'Invalid response, unable to find tool: 
        
         
          
         
             
       
    
               
         
           
           
          
          
        
      # Since there is no result tool, we can assume that str is compatible with ResultData
        
        
       
          
         
        
        
      
     
        
      
    
     

```

  
---  
Return the history of _messages.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
```

          
"""Return the history of _messages.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

  # this is a method to be consistent with the other methods

      
     'Setting result tool return content is not supported for this result type.'
  

```

  
---  
Return all messages from as JSON bytes.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
JSON bytes representing the messages.  
---  
```

          
"""Return all messages from
[`all_messages`][pydantic_ai.result._BaseRunResult.all_messages] as JSON bytes.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

    JSON bytes representing the messages.

  
    
  

```

  
---  
Return new messages associated with this run.

Messages from older runs are excluded.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
```

          
"""Return new messages associated with this run.

  Messages from older runs are excluded.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

    

```

  
---  
Return new messages from as JSON bytes.

The return content of the tool call to set in the last message. This provides a
convenient way to modify the content of the result tool call if you want to
continue the conversation and want to set the response to the result tool call.
If , the last message will not be modified.  
---  
JSON bytes representing the new messages.  
---  
```

          
"""Return new messages from
[`new_messages`][pydantic_ai.result._BaseRunResult.new_messages] as JSON bytes.

    result_tool_return_content: The return content of the tool call to set in the last message.
      This provides a convenient way to modify the content of the result tool call if you want to continue
      the conversation and want to set the response to the result tool call. If `None`, the last message will

    JSON bytes representing the new messages.

  
    
  

```

  
---  
Whether the stream has all been received.

This is set to when one of , , or completes.

Stream the response as an async iterable.

The pydantic validator for structured data will be called in on each iteration.

by how much (if at all) to debounce/group the response chunks by. means no
debouncing. Debouncing is particularly important for long structured responses
to reduce the overhead of performing validation as each token is received.  
---  
An async iterable of the response data.  
---  
```

           
"""Stream the response as an async iterable.

  The pydantic validator for structured data will be called in

    debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
      Debouncing is particularly important for long structured responses to reduce the overhead of
      performing validation as each token is received.

    An async iterable of the response data.

       
         
     

```

  
---  
Stream the text result as an async iterable.

Result validators will NOT be called on the text result if .

if , yield each chunk of text as it is received, if (default), yield the full
text up to the current point.  
---  
by how much (if at all) to debounce/group the response chunks by. means no
debouncing. Debouncing is particularly important for long structured responses
to reduce the overhead of performing validation as each token is received.  
```

               
"""Stream the text result as an async iterable.

    Result validators will NOT be called on the text result if `delta=True`.

    delta: if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text
      up to the current point.
    debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
      Debouncing is particularly important for long structured responses to reduce the overhead of
      performing validation as each token is received.

      
     'stream_text() can only be used with text responses'
    
      
  
  # Define a "merged" version of the iterator that will yield items that have
already been retrieved

  # and items that we receive while streaming. We define a dedicated async
iterator for this so we can

  # pass the combined stream to the group_by_temporal function within
`_stream_text_deltas` below.

       
    # if the response currently has any parts with content, yield those before streaming
      
        
          
          
        
       
         
          
         
      
          
       
         
          
         
      
          
      
         
          
              
     
     
          
         
    
      # a quick benchmark shows it's faster to build up a string with concat when we're
      # yielding at each step
         
        
          
        
          
           
         
       
       

```

  
---  
Stream the response as an async iterable of Structured LLM Messages.

by how much (if at all) to debounce/group the response chunks by. means no
debouncing. Debouncing is particularly important for long structured responses
to reduce the overhead of performing validation as each token is received.  
---  
An async iterable of the structured response message and whether that is the
last message.  
---  
```

  
         
  
"""Stream the response as an async iterable of Structured LLM Messages.

    debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
      Debouncing is particularly important for long structured responses to reduce the overhead of
      performing validation as each token is received.

    An async iterable of the structured response message and whether that is the last message.

    
      
  
     
    # if the message currently has any parts with content, yield before streaming
      
       
       
          
        
         
          
          
          
        
        
      # TODO: Should this now be `final_response` instead of `structured_response`?
       
       

```

  
---  
Stream the whole response, validate and return it.

```

    
"""Stream the whole response, validate and return it."""

    
      
  
      
    
    
  
    

```

  
---  
Return the usage of the whole run.

This won't return the full usage until the stream is finished.

```

  
"""Return the usage of the whole run.

    This won't return the full usage until the stream is finished.

     

```

  
---  
Get the timestamp of the response.

```

  
"""Get the timestamp of the response."""

  

```

  
---  
Validate a structured result message.

```

  
         
  
"""Validate a structured result message."""

           
       
       
       
        'Invalid response, unable to find tool: 
      
       
        
       
           
     
  
             
       
         
         
        
        
      
    # Since there is no result tool, we can assume that str is compatible with ResultData
      

```

  
---

---

# pydantic_ai.messages
URL: https://ai.pydantic.dev/api/messages/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

The structure of can be shown as a graph:

A system prompt, generally written by the application developer.

This gives the model context and guidance on how to respond.

```



"""A system prompt, generally written by the application developer.

  This gives the model context and guidance on how to respond.

  
"""The content of the prompt."""

       
"""The ref of the dynamic system prompt function that generated this part.

  Only set if system prompt is dynamic, see
[`system_prompt`][pydantic_ai.Agent.system_prompt] for more information.

     
"""Part type identifier, this is available on all parts as a discriminator."""

```

  
---  
The content of the prompt.

The ref of the dynamic system prompt function that generated this part.

Only set if system prompt is dynamic, see for more information.

Part type identifier, this is available on all parts as a discriminator.

A user prompt, generally written by the end user.

Content comes from the parameter of , , and .

```



"""A user prompt, generally written by the end user.

  Content comes from the `user_prompt` parameter of
[`Agent.run`][pydantic_ai.Agent.run],

  
"""The content of the prompt."""

     
"""The timestamp of the prompt."""

     
"""Part type identifier, this is available on all parts as a discriminator."""

```

  
---  
The content of the prompt.

The timestamp of the prompt.

Part type identifier, this is available on all parts as a discriminator.

A tool return message, this encodes the result of running a tool.

```



"""A tool return message, this encodes the result of running a tool."""

  
"""The name of the "tool" was called."""

  

       
"""Optional tool call identifier, this is used by some models including
OpenAI."""

     
"""The timestamp, when the tool returned."""

     
"""Part type identifier, this is available on all parts as a discriminator."""

     
"""Return a string representation of the content for the model."""

      
       
    
       
      
"""Return a dictionary representation of the content, wrapping non-dict types
appropriately."""

    # gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict
      
         
    
         

```

  
---  
The name of the "tool" was called.

Optional tool call identifier, this is used by some models including OpenAI.

The timestamp, when the tool returned.

Part type identifier, this is available on all parts as a discriminator.

Return a string representation of the content for the model.

```

  
"""Return a string representation of the content for the model."""

    
     
  
     

```

  
---  
Return a dictionary representation of the content, wrapping non-dict types
appropriately.

```

    
"""Return a dictionary representation of the content, wrapping non-dict types
appropriately."""

  # gemini supports JSON dict return values, but no other JSON types, hence we
wrap anything else in a dict

    
       
  
       

```

  
---  
A message back to a model asking it to try again.

This can be sent for a number of reasons:

  * Pydantic validation of tool arguments failed, here content is derived from a Pydantic 
  * no tool was found for the tool name
  * the model returned plain text when a structured response was expected
  * Pydantic validation of a structured response failed, here content is derived from a Pydantic 
  * a result validator raised a exception

```



"""A message back to a model asking it to try again.

  This can be sent for a number of reasons:

  * Pydantic validation of tool arguments failed, here content is derived from a Pydantic

  * a tool raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception
  * no tool was found for the tool name
  * the model returned plain text when a structured response was expected
  * Pydantic validation of a structured response failed, here content is derived from a Pydantic

  * a result validator raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception

     
"""Details of why and how the model should retry.

  If the retry was triggered by a
[`ValidationError`][pydantic_core.ValidationError], this will be a list of

       
"""The name of the tool that was called, if any."""

       
"""Optional tool call identifier, this is used by some models including
OpenAI."""

     
"""The timestamp, when the retry was triggered."""

     
"""Part type identifier, this is available on all parts as a discriminator."""

     
"""Return a string message describing why the retry is requested."""

      
        
    
           
        
     Fix the errors and try again.'

```

  
---  
Details of why and how the model should retry.

If the retry was triggered by a , this will be a list of error details.

The name of the tool that was called, if any.

Optional tool call identifier, this is used by some models including OpenAI.

The timestamp, when the retry was triggered.

Part type identifier, this is available on all parts as a discriminator.

Return a string message describing why the retry is requested.

```

  
"""Return a string message describing why the retry is requested."""

    
      
  
         
      
   Fix the errors and try again.'

```

  
---  
A message part sent by PydanticAI to a model.

A request generated by PydanticAI and sent to a model, e.g. a message from the
PydanticAI app to the model.

```



"""A request generated by PydanticAI and sent to a model, e.g. a message from
the PydanticAI app to the model."""

  
"""The parts of the user message."""

     
"""Message type identifier, this is available on all parts as a
discriminator."""

```

  
---  
The parts of the user message.

Message type identifier, this is available on all parts as a discriminator.

A plain text response from a model.

```



"""A plain text response from a model."""

  
"""The text content of the response."""

     
"""Part type identifier, this is available on all parts as a discriminator."""

     
"""Return `True` if the text content is non-empty."""

     

```

  
---  
The text content of the response.

Part type identifier, this is available on all parts as a discriminator.

Return if the text content is non-empty.

```

  
"""Return `True` if the text content is non-empty."""

  

```

  
---  
Tool arguments as a JSON string.

```



"""Tool arguments as a JSON string."""

  
"""A JSON string of arguments."""

```

  
---  
A JSON string of arguments.

Tool arguments as a Python dictionary.

```



"""Tool arguments as a Python dictionary."""

    
"""A python dictionary of arguments."""

```

  
---  
A python dictionary of arguments.

A tool call from a model.

```



"""A tool call from a model."""

  
"""The name of the tool to call."""

     
"""The arguments to pass to the tool.

  Either as JSON or a Python dictionary depending on how data was returned.

       
"""Optional tool call identifier, this is used by some models including
OpenAI."""

     
"""Part type identifier, this is available on all parts as a discriminator."""

  
                  
"""Create a `ToolCallPart` from raw arguments, converting them to `ArgsJson` or
`ArgsDict`."""

      
         
      
         
    
      
      
"""Return the arguments as a Python dictionary.

    This is just for convenience with models that require dicts as input.

      
       
      
       'args should be a dict'
       
     
"""Return the arguments as a JSON string.

    This is just for convenience with models that require JSON strings as input.

      
       
     
     
"""Return `True` if the arguments contain any data."""

      
       
    
       

```

  
---  
The name of the tool to call.

The arguments to pass to the tool.

Either as JSON or a Python dictionary depending on how data was returned.

Optional tool call identifier, this is used by some models including OpenAI.

Part type identifier, this is available on all parts as a discriminator.

Create a from raw arguments, converting them to or .

```

                
"""Create a `ToolCallPart` from raw arguments, converting them to `ArgsJson` or
`ArgsDict`."""

    
       
    
       
  
    

```

  
---  
Return the arguments as a Python dictionary.

This is just for convenience with models that require dicts as input.

```

    
"""Return the arguments as a Python dictionary.

  This is just for convenience with models that require dicts as input.

    
     
    
     'args should be a dict'
     

```

  
---  
Return the arguments as a JSON string.

This is just for convenience with models that require JSON strings as input.

```

  
"""Return the arguments as a JSON string.

  This is just for convenience with models that require JSON strings as input.

    
     
  

```

  
---  
Return if the arguments contain any data.

```

  
"""Return `True` if the arguments contain any data."""

    
     
  
     

```

  
---  
A message part returned by a model.

A response from a model, e.g. a message from the model to the PydanticAI app.

```



"""A response from a model, e.g. a message from the model to the PydanticAI
app."""

  
"""The parts of the model message."""

     
"""The timestamp of the response.

  If the model provides a timestamp in the response (as OpenAI does) that will
be used.

     
"""Message type identifier, this is available on all parts as a
discriminator."""

  
             
"""Create a `ModelResponse` containing a single `TextPart`."""

        
  
       
"""Create a `ModelResponse` containing a single `ToolCallPart`."""

     

```

  
---  
The parts of the model message.

The timestamp of the response.

If the model provides a timestamp in the response (as OpenAI does) that will be
used.

Message type identifier, this is available on all parts as a discriminator.

```

           
"""Create a `ModelResponse` containing a single `TextPart`."""

      

```

  
---  
```

     
"""Create a `ModelResponse` containing a single `ToolCallPart`."""

  

```

  
---  
Any message sent to or returned by a model.

A partial update (delta) for a to append new text content.

```



"""A partial update (delta) for a `TextPart` to append new text content."""

  
"""The incremental text content to add to the existing `TextPart` content."""

     
"""Part delta type identifier, used as a discriminator."""

       
"""Apply this text delta to an existing `TextPart`.

      part: The existing model response part, which must be a `TextPart`.

      A new `TextPart` with updated text content.

      ValueError: If `part` is not a `TextPart`.

       
       'Cannot apply TextPartDeltas to non-TextParts'
        

```

  
---  
The incremental text content to add to the existing content.

Part delta type identifier, used as a discriminator.

Apply this text delta to an existing .

The existing model response part, which must be a .  
---  
A new with updated text content.  
---  
```

     
"""Apply this text delta to an existing `TextPart`.

    part: The existing model response part, which must be a `TextPart`.

    A new `TextPart` with updated text content.

    ValueError: If `part` is not a `TextPart`.

     
     'Cannot apply TextPartDeltas to non-TextParts'
      

```

  
---  
A partial update (delta) for a to modify tool name, arguments, or tool call ID.

```



"""A partial update (delta) for a `ToolCallPart` to modify tool name, arguments,
or tool call ID."""

       
"""Incremental text to add to the existing tool name, if any."""

          
"""Incremental data to add to the tool arguments.

  If this is a string, it will be appended to existing JSON arguments.

  If this is a dict, it will be merged with existing dict arguments.

       
"""Optional tool call identifier, this is used by some models including OpenAI.

  Note this is never treated as a delta — it can replace None, but otherwise if
a

  non-matching value is provided an error will be raised."""

     
"""Part delta type identifier, used as a discriminator."""

       
"""Convert this delta to a fully formed `ToolCallPart` if possible, otherwise
return `None`.

      A `ToolCallPart` if both `tool_name_delta` and `args_delta` are set, otherwise `None`.

           
       
     
      
      
      
    
  
        
  
            
           
"""Apply this delta to a part or delta, returning a new part or delta with the
changes applied.

      part: The existing model response part or delta to update.

      Either a new `ToolCallPart` or an updated `ToolCallPartDelta`.

      ValueError: If `part` is neither a `ToolCallPart` nor a `ToolCallPartDelta`.
      UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.

      
       
      
       
     'Can only apply ToolCallPartDeltas to ToolCallParts or ToolCallPartDeltas, not 
         
"""Internal helper to apply this delta to another delta."""

     
      # Append incremental text to the existing tool_name_delta
            
         
      
        
         
          'Cannot apply JSON deltas to non-JSON tool arguments (
        
            
         
      
        
         
          'Cannot apply dict deltas to non-dict tool arguments (
        
           
         
     
      # Set the tool_call_id if it wasn't present, otherwise error if it has changed
              
         
          'Cannot apply a new tool_call_id to a ToolCallPartDelta that already has one (
        
         
    # If we now have enough data to create a full ToolCallPart, do so
             
       
        
        
        
      
     
       
"""Internal helper to apply this delta directly to a `ToolCallPart`."""

     
      # Append incremental text to the existing tool_name
          
         
      
         
         'Cannot apply JSON deltas to non-JSON tool arguments (
          
         
      
         
         'Cannot apply dict deltas to non-dict tool arguments (
           
         
     
      # Replace the tool_call_id entirely if given
              
         
          'Cannot apply a new tool_call_id to a ToolCallPartDelta that already has one (
        
         
     

```

  
---  
Incremental text to add to the existing tool name, if any.

Incremental data to add to the tool arguments.

If this is a string, it will be appended to existing JSON arguments. If this is
a dict, it will be merged with existing dict arguments.

Optional tool call identifier, this is used by some models including OpenAI.

Note this is never treated as a delta — it can replace None, but otherwise if a
non-matching value is provided an error will be raised.

Part delta type identifier, used as a discriminator.

Convert this delta to a fully formed if possible, otherwise return .  
```

     
"""Convert this delta to a fully formed `ToolCallPart` if possible, otherwise
return `None`.

    A `ToolCallPart` if both `tool_name_delta` and `args_delta` are set, otherwise `None`.

         
     
  
    
    
    
  

```

  
---  
Apply this delta to a part or delta, returning a new part or delta with the
changes applied.

The existing model response part or delta to update.  
---  
Either a new or an updated .  
---  
If applying JSON deltas to dict arguments or vice versa.  
---  
```

         
"""Apply this delta to a part or delta, returning a new part or delta with the
changes applied.

    part: The existing model response part or delta to update.

    Either a new `ToolCallPart` or an updated `ToolCallPartDelta`.

    ValueError: If `part` is neither a `ToolCallPart` nor a `ToolCallPartDelta`.
    UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.

    
     
    
     
   'Can only apply ToolCallPartDeltas to ToolCallParts or ToolCallPartDeltas,
not

```

  
---  
A partial update (delta) for any model response part.

An event indicating that a new part has started.

If multiple s are received with the same index, the new one should fully replace
the old one.

```



"""An event indicating that a new part has started.

  If multiple `PartStartEvent`s are received with the same index,

  the new one should fully replace the old one.

  
"""The index of the part within the overall response parts list."""

  

     
"""Event type identifier, used as a discriminator."""

```

  
---  
The index of the part within the overall response parts list.

Event type identifier, used as a discriminator.

An event indicating a delta update for an existing part.

```



"""An event indicating a delta update for an existing part."""

  
"""The index of the part within the overall response parts list."""

  
"""The delta to apply to the specified part."""

     
"""Event type identifier, used as a discriminator."""

```

  
---  
The index of the part within the overall response parts list.

The delta to apply to the specified part.

Event type identifier, used as a discriminator.

An event in the model response stream, either starting a new part or applying a
delta to an existing one.

---

# pydantic_ai.exceptions
URL: https://ai.pydantic.dev/api/exceptions/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Exception raised when a tool function should be retried.

The agent will return the message to the model and ask it to try calling the
function/tool again.

```



"""Exception raised when a tool function should be retried.

  The agent will return the message to the model and ask it to try calling the
function/tool again.

  
"""The message to return to the model."""

     
      
    

```

  
---  
The message to return to the model.

Error caused by a usage mistake by the application developer — You!

```



"""Error caused by a usage mistake by the application developer — You!"""

  

     
      
    

```

  
---  
Base class for errors occurring during an agent run.

```



"""Base class for errors occurring during an agent run."""

  

     
      
    
     
     

```

  
---  
Error raised when a Model's usage exceeds the specified limits.

```



"""Error raised when a Model's usage exceeds the specified limits."""

```

  
---  
Error caused by unexpected Model behavior, e.g. an unexpected response code.

```



"""Error caused by unexpected Model behavior, e.g. an unexpected response
code."""

  
"""Description of the unexpected behavior."""

     
"""The body of the response, if available."""

           
      
       
           
    
      
           
       
          
    
     
     
       
    
       

```

  
---  
Description of the unexpected behavior.

The body of the response, if available.

---

# pydantic_ai.settings
URL: https://ai.pydantic.dev/api/settings/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Settings to configure an LLM.

Here we include only settings which apply to multiple models / model providers.

```

  
"""Settings to configure an LLM.

  Here we include only settings which apply to multiple models / model
providers.

  
"""The maximum number of tokens to generate before stopping.

  
"""Amount of randomness injected into the response.

  Use `temperature` closer to `0.0` for analytical / multiple choice, and closer
to a model's

  maximum `temperature` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully
deterministic.

  
"""An alternative to sampling with temperature, called nucleus sampling, where
the model considers the results of the tokens with top_p probability mass.

  So 0.1 means only the tokens comprising the top 10% probability mass are
considered.

  You should either alter `temperature` or `top_p`, but not both.

     
"""Override the client-level default timeout for a request, in seconds.

```

  
---  
The maximum number of tokens to generate before stopping.

Amount of randomness injected into the response.

Use closer to for analytical / multiple choice, and closer to a model's maximum
for creative and generative tasks.

Note that even with of , the results will not be fully deterministic.

An alternative to sampling with temperature, called nucleus sampling, where the
model considers the results of the tokens with top_p probability mass.

So 0.1 means only the tokens comprising the top 10% probability mass are
considered.

You should either alter or , but not both.

Override the client-level default timeout for a request, in seconds.

---

# pydantic_ai.usage
URL: https://ai.pydantic.dev/api/usage/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

LLM usage associated with a request or run.

Responsibility for calculating usage is on the model; PydanticAI simply sums the
usage information across requests.

You'll need to look up the documentation of the model you're using to convert
usage to monetary costs.

```



"""LLM usage associated with a request or run.

  Responsibility for calculating usage is on the model; PydanticAI simply sums
the usage information across requests.

  You'll need to look up the documentation of the model you're using to convert
usage to monetary costs.

     
"""Number of requests made to the LLM API."""

       
"""Tokens used in processing requests."""

       
"""Tokens used in generating responses."""

       
"""Total tokens used in the whole run, should generally be equal to
`request_tokens + response_tokens`."""

        
"""Any extra details returned by the model."""

            
"""Increment the usage in place.

      incr_usage: The usage to increment by.
      requests: The number of requests to increment by in addition to `incr_usage.requests`.

      
          
         
         
               
                
     
          
          
             
       

    This is provided so it's trivial to sum usage information from multiple requests and runs.

      
    
     

```

  
---  
Number of requests made to the LLM API.

Tokens used in processing requests.

Tokens used in generating responses.

Total tokens used in the whole run, should generally be equal to .

Any extra details returned by the model.

Increment the usage in place.

The usage to increment by.  
---  
The number of requests to increment by in addition to .  
```

          
"""Increment the usage in place.

    incr_usage: The usage to increment by.
    requests: The number of requests to increment by in addition to `incr_usage.requests`.

    
        
       
       
             
              
  
        
        
           

```

  
---  
This is provided so it's trivial to sum usage information from multiple requests
and runs.

```

     

  This is provided so it's trivial to sum usage information from multiple
requests and runs.

    
  
  

```

  
---  
The request count is tracked by pydantic_ai, and the request limit is checked
before each request to the model. Token counts are provided in responses from
the model, and the token limits are checked after each response.

Each of the limits can be set to to disable that limit.

```



  The request count is tracked by pydantic_ai, and the request limit is checked
before each request to the model.

  Token counts are provided in responses from the model, and the token limits
are checked after each response.

  Each of the limits can be set to `None` to disable that limit.

       
"""The maximum number of requests allowed to the model."""

       
"""The maximum number of tokens allowed in requests to the model."""

       
"""The maximum number of tokens allowed in responses from the model."""

       
"""The maximum number of tokens allowed in requests and responses combined."""

     
"""Returns `True` if this instance places any limits on token counts.

    If this returns `False`, the `check_tokens` method will never raise an error.
    This is useful because if we have token limits, we need to check them after receiving each streamed message.
    If there are no limits, we can skip that processing in the streaming response iterator.

     
         
           
    
       
"""Raises a `UsageLimitExceeded` exception if the next request would exceed the
request_limit."""

      
            
       'The next request would exceed the request_limit of 
       
"""Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token
limits."""

        
            
       
        
      
        
            
       
        
      
        
            
       

```

  
---  
The maximum number of requests allowed to the model.

The maximum number of tokens allowed in requests to the model.

The maximum number of tokens allowed in responses from the model.

The maximum number of tokens allowed in requests and responses combined.

Returns if this instance places any limits on token counts.

If this returns , the method will never raise an error.

This is useful because if we have token limits, we need to check them after
receiving each streamed message. If there are no limits, we can skip that
processing in the streaming response iterator.

```

  
"""Returns `True` if this instance places any limits on token counts.

  If this returns `False`, the `check_tokens` method will never raise an error.

  This is useful because if we have token limits, we need to check them after
receiving each streamed message.

  If there are no limits, we can skip that processing in the streaming response
iterator.

  
       
         
  

```

  
---  
Raises a exception if the next request would exceed the request_limit.

```

     
"""Raises a `UsageLimitExceeded` exception if the next request would exceed the
request_limit."""

    
          
     'The next request would exceed the request_limit of 

```

  
---  
Raises a exception if the usage exceeds any of the token limits.

```

     
"""Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token
limits."""

      
          
     
      
    
      
          
     
      
    
      
          
     

```

  
---

---

# pydantic_ai.format_as_xml
URL: https://ai.pydantic.dev/api/format_as_xml/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Format a Python object as XML.

This is useful since LLMs often find it easier to read semi-structured data
(e.g. examples) as XML, rather than JSON etc.

Python Object to serialize to XML.  
---  
Outer tag to wrap the XML in, use to omit the outer tag.  
Tag to use for each item in an iterable (e.g. list), this is overridden by the
class name for dataclasses and Pydantic models.  
Whether to include the root tag in the output (The root tag is always included
if it includes a body - e.g. when the input is a simple value).  
Indentation string to use for pretty printing.  
XML representation of the object.  
---  
```



  
     
     
     
     
       
  
"""Format a Python object as XML.

  This is useful since LLMs often find it easier to read semi-structured data
(e.g. examples) as XML,

  Supports: `str`, `bytes`, `bytearray`, `bool`, `int`, `float`, `date`,
`datetime`, `Mapping`,

    obj: Python Object to serialize to XML.
    root_tag: Outer tag to wrap the XML in, use `None` to omit the outer tag.
    item_tag: Tag to use for each item in an iterable (e.g. list), this is overridden by the class name
      for dataclasses and Pydantic models.
    include_root_tag: Whether to include the root tag in the output
      (The root tag is always included if it includes a body - e.g. when the input is a simple value).
    none_str: String to use for `None` values.
    indent: Indentation string to use for pretty printing.

    XML representation of the object.

  print(format_as_xml({'name': 'John', 'height': 6, 'weight': 200},
root_tag='user'))

      
        
            
      
  
        
       
      

```

  
---

---

# pydantic_ai.models
URL: https://ai.pydantic.dev/api/models/base/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Logic related to making requests to an LLM.

The aim here is to make a common interface for different LLMs, so that the rest
of the code can be agnostic to the specific LLM being used.

Known model names that can be used with the parameter of .

is provided as a concise way to specify a model.

Abstract class for a model.

```



"""Abstract class for a model."""

  
    
    
    
     
     
     
    
"""Create an agent model, this is called for each step of an agent run.

    This is async in case slow/async config checks need to be performed that can't be done in `__init__`.

      function_tools: The tools available to the agent.
      allow_text_result: Whether a plain text final response/result is permitted.
      result_tools: Tool definitions for the final result tool(s), if any.

     
  
     
     

```

  
---  
Create an agent model, this is called for each step of an agent run.

This is async in case slow/async config checks need to be performed that can't
be done in .

The tools available to the agent.  
---  
Whether a plain text final response/result is permitted.  
Tool definitions for the final result tool(s), if any.  
```

  
  
  
  
  
  
  
"""Create an agent model, this is called for each step of an agent run.

  This is async in case slow/async config checks need to be performed that can't
be done in `__init__`.

    function_tools: The tools available to the agent.
    allow_text_result: Whether a plain text final response/result is permitted.
    result_tools: Tool definitions for the final result tool(s), if any.

  

```

  
---  
Model configured for each step of an Agent run.

```



"""Model configured for each step of an Agent run."""

  
    
          
     
"""Make a request to the model."""

     
  
    
          
    
"""Make a request to the model and return a streaming response."""

    # This method is not required, but you need to implement it if you want to support streamed responses
     'Streamed requests not supported by this 
    # yield is required to make this a generator for type checking
    
     

```

  
---  
Make a request to the model.

```

  
        
  
"""Make a request to the model."""

  

```

  
---  
Make a request to the model and return a streaming response.

```

  
        
  
"""Make a request to the model and return a streaming response."""

  # This method is not required, but you need to implement it if you want to
support streamed responses

   'Streamed requests not supported by this

  # yield is required to make this a generator for type checking

  
  

```

  
---  
Streamed response from an LLM when calling a tool.

```



"""Streamed response from an LLM when calling a tool."""

      
      
        
     
"""Stream the response as an async iterable of
[`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s."""

       
        
     
  
      
"""Return an async iterator of
[`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s.

    This method should be implemented by subclasses to translate the vendor-specific stream of events into

     
    
    
     
"""Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data
received from the stream so far."""

      
     
"""Get the usage of the response so far. This will not be the final usage until
the stream is exhausted."""

     
  
     
"""Get the timestamp of the response."""

     

```

  
---  
Stream the response as an async iterable of s.

```

  
"""Stream the response as an async iterable of
[`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s."""

     
      
  

```

  
---  
Build a from the data received from the stream so far.

```

  
"""Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data
received from the stream so far."""

    

```

  
---  
Get the usage of the response so far. This will not be the final usage until the
stream is exhausted.

```

  
"""Get the usage of the response so far. This will not be the final usage until
the stream is exhausted."""

  

```

  
---  
Get the timestamp of the response.

```

  
"""Get the timestamp of the response."""

  

```

  
---  
Whether to allow requests to models.

This global setting allows you to disable request to most models, e.g. to make
sure you don't accidentally make costly requests to a model during tests.

The testing models and are no affected by this setting.

Check if model requests are allowed.

If you're defining your own models that have costs or latency associated with
their use, you should call this in .

If model requests are not allowed.  
---  
```

  
"""Check if model requests are allowed.

  If you're defining your own models that have costs or latency associated with
their use, you should call this in

    RuntimeError: If model requests are not allowed.

    
     'Model requests are not allowed, since ALLOW_MODEL_REQUESTS is False'

```

  
---  
Context manager to temporarily override .

Whether to allow model requests within the context.  
---  
```

    
"""Context manager to temporarily override
[`ALLOW_MODEL_REQUESTS`][pydantic_ai.models.ALLOW_MODEL_REQUESTS].

    allow_model_requests: Whether to allow model requests within the context.

  
    
     
  
    
  
       

```

  
---

---

# pydantic_ai.models.openai
URL: https://ai.pydantic.dev/api/models/openai/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

For details on how to set up authentication with this model, see .

Using this more broad type for the model name instead of the ChatModel
definition allows this model to be used more easily with other model types (ie,
Ollama)

A model that uses the OpenAI API.

Internally, this uses the to interact with the API.

Apart from , all methods are private or match those of the base class.

```



"""A model that uses the OpenAI API.

  Internally, this uses the [OpenAI Python
client](https://github.com/openai/openai-python) to interact with the API.

  Apart from `__init__`, all methods are private or match those of the base
class.

  
     
  
    
     
    
         
         
         
         
  

      model_name: The name of the OpenAI model to use. List of model names available

        (Unfortunately, despite being ask to do so, OpenAI do not provide `.inv` files for their API).
      base_url: The base url for the OpenAI requests. If not provided, the `OPENAI_BASE_URL` environment variable
        will be used if available. Otherwise, defaults to OpenAI's base url.
      api_key: The API key to use for authentication, if not provided, the `OPENAI_API_KEY` environment variable
        will be used if available.

        client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

       
        
          'Cannot provide both `openai_client` and `http_client`'
          'Cannot provide both `openai_client` and `base_url`'
          'Cannot provide both `openai_client` and `api_key`'
        
        
          
    
          
    
    
    
     
     
     
    
    
          
     
            
     
      
      
      
      
    
     
     
  
      
     
       
       
         
         
         
      
    

```

  
---  
The name of the OpenAI model to use. List of model names available
(Unfortunately, despite being ask to do so, OpenAI do not provide files for
their API).  
---  
The base url for the OpenAI requests. If not provided, the environment variable
will be used if available. Otherwise, defaults to OpenAI's base url.  
The API key to use for authentication, if not provided, the environment variable
will be used if available.  
An existing client to use. If provided, , , and must be .  
An existing to use for making HTTP requests.  
```



  
  
  
       
       
       
       

    model_name: The name of the OpenAI model to use. List of model names available

      (Unfortunately, despite being ask to do so, OpenAI do not provide `.inv` files for their API).
    base_url: The base url for the OpenAI requests. If not provided, the `OPENAI_BASE_URL` environment variable
      will be used if available. Otherwise, defaults to OpenAI's base url.
    api_key: The API key to use for authentication, if not provided, the `OPENAI_API_KEY` environment variable
      will be used if available.

      client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

     
      
        'Cannot provide both `openai_client` and `http_client`'
        'Cannot provide both `openai_client` and `base_url`'
        'Cannot provide both `openai_client` and `api_key`'
      
      
        
  
        

```

  
---  
```



"""Implementation of `AgentModel` for OpenAI models."""

  
  
  
  
    
          
     
         
      
  
    
          
    
         
      
        
  
    
            
    
    
  
    
            
    
    
    
            
      
    # standalone function to make it easier to override
      
             
      
        
    
        
          
        
      
      
      
      
          
        
        
      
           
       
       
       
       
    
  
      
"""Process a non-streamed response, and prepare a message to return."""

       
      
       
        
      
        
         
          
      
  
       
"""Process a streamed response, and prepare a streaming response to return."""

      
       
      
       'Streamed response ended without content or tool calls'
       
  
       
"""Just maps a `pydantic_ai.Message` to a
`openai.types.ChatCompletionMessageParam`."""

      
       
      
         
         
         
          
          
          
          
        
          
        
       
        # Note: model responses from this model should only have one text item, so the following
        # shouldn't merge multiple texts into one unless you switch models between runs:
          
       
          
       
    
      
  
       
       
        
          
        
          
        
         
          
           
          
        
        
           
            
        
           
            
             
            
          
      
        

```

  
---  
```



"""Implementation of `StreamedResponse` for OpenAI models."""

  
  
      
        
        
      
          
       
        
      # Handle the text part of the response
        
          
          
           
          
          
            
            
          
        
            
           
     
     

```

  
---

---

# pydantic_ai.models.anthropic
URL: https://ai.pydantic.dev/api/models/anthropic/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

For details on how to set up authentication with this model, see .

Since Anthropic supports a variety of date-stamped models, we explicitly list
the latest models but allow any name in the type hints. Since for a full list.

A model that uses the Anthropic API.

Internally, this uses the to interact with the API.

Apart from , all methods are private or match those of the base class.

The class does not yet support streaming responses. We anticipate adding support
for streaming responses in a near-term future release.

```



"""A model that uses the Anthropic API.

  Internally, this uses the [Anthropic Python
client](https://github.com/anthropics/anthropic-sdk-python) to interact with the
API.

  Apart from `__init__`, all methods are private or match those of the base
class.

    The `AnthropicModel` class does not yet support streaming responses.
    We anticipate adding support for streaming responses in a near-term future release.

  
     
  
    
     
    
         
         
         
  

      model_name: The name of the Anthropic model to use. List of model names available

      api_key: The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable
        will be used if available.

        client to use, if provided, `api_key` and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

      
        
          'Cannot provide both `anthropic_client` and `http_client`'
          'Cannot provide both `anthropic_client` and `api_key`'
        
        
         
    
         
    
    
    
     
     
     
    
    
          
     
            
     
      
      
      
      
    
     
     
  
      
     
       
       
       
    

```

  
---  
The name of the Anthropic model to use. List of model names available .  
---  
The API key to use for authentication, if not provided, the environment variable
will be used if available.  
An existing client to use, if provided, and must be .  
An existing to use for making HTTP requests.  
```



  
  
  
       
       
       

    model_name: The name of the Anthropic model to use. List of model names available

    api_key: The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable
      will be used if available.

      client to use, if provided, `api_key` and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

    
      
        'Cannot provide both `anthropic_client` and `http_client`'
        'Cannot provide both `anthropic_client` and `api_key`'
      
      
       
  
       

```

  
---  
```



"""Implementation of `AgentModel` for Anthropic models."""

  
  
  
  
    
          
     
         
      
  
    
          
    
         
      
        
  
    
            
    
    
  
    
            
    
    
    
            
      
    # standalone function to make it easier to override
      
           
      
         
    
         
       
        
      
       
        
      
      
        
        
      
       
       
       
    
  
      
"""Process a non-streamed response, and prepare a message to return."""

       
       
        
        
      
           
        
          
            
              
            
          
        
     
  
       
"""TODO: Process a streamed response, and prepare a streaming response to
return."""

    # We don't yet support streamed responses from Anthropic, so we raise an error here for now.
    # Streamed responses will be supported in a future release.
     'Streamed responses are not yet supported for Anthropic models.'
    # Should be returning some sort of AnthropicStreamTextResponse or AnthropicStreamedResponse
    # depending on the type of chunk we get, but we need to establish how we handle (and when we get) the following:
    
    
    
    
    
    
    
    # We might refactor streaming internally before we implement this...
  
       
"""Just maps a `pydantic_ai.Message` to a `anthropic.types.MessageParam`."""

       
       
       
        
           
            
              
            
             
            
            
              
                
                
                  
                     
                    
                    
                    
                  
                
              
            
            
               
               
            
              
                
                  
                  
                    
                       
                      
                      
                      
                    
                  
                
              
        
             
           
            
             
          
              
            
         
      
        
      

```

  
---

---

# pydantic_ai.models.gemini
URL: https://ai.pydantic.dev/api/models/gemini/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Custom interface to the API using and .

The Google SDK for interacting with the API reads like it was written by a Java
developer who thought they knew everything about OOP, spent 30 minutes trying to
learn Python, gave up and decided to build the library to prove how horrible
Python is. It also doesn't use httpx for HTTP requests, and tries to implement
tool calling itself, but doesn't use Pydantic or equivalent for validation.

We therefore implement support for the API directly.

Despite these shortcomings, the Gemini model is actually quite powerful and very
fast.

For details on how to set up authentication with this model, see .

See for a full list.

A model that uses Gemini via API.

This is implemented from scratch rather than using a dedicated SDK, good API
documentation is available .

Apart from , all methods are private or match those of the base class.

```



"""A model that uses Gemini via `generativelanguage.googleapis.com` API.

  This is implemented from scratch rather than using a dedicated SDK, good API
documentation is

  Apart from `__init__`, all methods are private or match those of the base
class.

  
  
  
  
  
    
     
    
         
         
       
  

      model_name: The name of the model to use.
      api_key: The API key to use for authentication, if not provided, the `GEMINI_API_KEY` environment variable
        will be used if available.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
      url_template: The URL template to use for making requests, you shouldn't need to change this,

        `model` is substituted with the model name, and `function` is added to the end of the URL.

      
       
         
          
      
         'API key must be provided or set in the GEMINI_API_KEY environment variable'
      
        
      
    
    
    
     
     
     
    
    
     
      
      
      
      
      
      
      
    
     
     

```

  
---  
The name of the model to use.  
---  
The API key to use for authentication, if not provided, the environment variable
will be used if available.  
An existing to use for making HTTP requests.  
The URL template to use for making requests, you shouldn't need to change this,
docs , is substituted with the model name, and is added to the end of the URL.  
```



  
  
  
       
       
     

    model_name: The name of the model to use.
    api_key: The API key to use for authentication, if not provided, the `GEMINI_API_KEY` environment variable
      will be used if available.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    url_template: The URL template to use for making requests, you shouldn't need to change this,

      `model` is substituted with the model name, and `function` is added to the end of the URL.

    
     
       
        
    
       'API key must be provided or set in the GEMINI_API_KEY environment variable'
    
      
    

```

  
---  
Abstract definition for Gemini authentication.

```



"""Abstract definition for Gemini authentication."""

        

```

  
---  
Authentication using an API key for the header.

```



"""Authentication using an API key for the `X-Goog-Api-Key` header."""

  
       
    
      

```

  
---  
```



"""Implementation of `AgentModel` for Gemini models."""

  
  
  
     
     
  
  
    
     
     
     
     
     
     
     
  
          
     
            
     
        
    
            
      
      
      
          
      
      
    
          
     
          
         
      
  
    
          
    
          
        
  
    
            
    
       
      
     
         
        
        
        
        
       
     
            
          
            
          
            
          
     
        
            
      
       
       
       
    
       
      
      
      
      
      
         
      
         
         
          
       
  
      
       
       'Expected exactly one candidate in Gemini response'
      
     
  
       
"""Process a streamed response, and prepare a streaming response to return."""

      
         
      
        
      
        
        
        
      
       
          
           
            
          
       
       'Streamed response ended without content or tool calls'
      
  
  
      
     
       
       
       
        
           
           
            
            
            
            
            
             
            
               
              
            
                 
               
          
            
         
           
        
        
      
        
      

```

  
---  
Implementation of for the Gemini model.

```



"""Implementation of `StreamedResponse` for the Gemini model."""

  
  
      
      
        
        
       
         
           
          # Using vendor_part_id=None means we can produce multiple text parts if their deltas are sprinkled
          # amongst the tool call deltas
            
           
          # Here, we assume all function_call parts are complete and don't have deltas.
          # We do this by assigning a unique randomly generated "vendor_part_id".
          # We need to confirm whether this is actually true, but if it isn't, we can still handle it properly
          # it would just be a bit more complicated. And we'd need to confirm the intended semantics.
            
            
            
            
            
          
              
             
        
              
      
    # This method exists to ensure we only yield completed items, so we don't need to worry about
    # partial gemini responses, which would make everything more complicated
       
      
    # Right now, there are some circumstances where we will have information that could be yielded sooner than it is
    # But changing that would make things a lot more complicated.
        
      
        
        
        
      
      # The idea: yield only up to the latest response, which might still be partial.
      # Note that if the latest response is complete, we could yield it immediately, but there's not a good
      # allow_partial API to determine if the last item in the list is complete.
        
         
          
          
         
    # Now yield the final response, which should be complete
     
        
        
       
     
     

```

  
---

---

# pydantic_ai.models.vertexai
URL: https://ai.pydantic.dev/api/models/vertexai/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Custom interface to the API for Gemini models.

This model uses with just the URL and auth method changed from , it relies on
the VertexAI and function endpoints having the same schemas as the equivalent .

For details on how to set up authentication with this model as well as a
comparison with the API used by , see [model configuration for Gemini via
VertexAI](https://ai.pydantic.dev/api/models/models/#gemini-via-vertexai>).

With the default google project already configured in your environment using
"application default credentials":

```

  
  
  
  
  

#> Did you hear about the toothpaste scandal? They called it Colgate.

```

Or using a service account JSON file:

```

  
  
  
  
  

  
  

#> Did you hear about the toothpaste scandal? They called it Colgate.

```

URL template for Vertex AI.

The template is used thus:

  * is substituted with the argument, see 
  * is substituted with the from auth/credentials
  * ( or ) is added to the end of the URL

A model that uses Gemini via the VertexAI API.

```



"""A model that uses Gemini via the `*-aiplatform.googleapis.com` VertexAI
API."""

  
       
     
  
  
  
  
     
     
  # TODO __init__ can be removed once we drop 3.9 and we can set kw_only
correctly on the dataclass

  
    
     
    
           
         
       
       
         
       
  
"""Initialize a Vertex AI Gemini model.

      model_name: The name of the model to use. I couldn't find a list of supported Google models, in VertexAI
        so for now this uses the same models as the [Gemini model][pydantic_ai.models.gemini.GeminiModel].
      service_account_file: Path to a service account file.
        If not provided, the default environment credentials will be used.
      project_id: The project ID to use, if not provided it will be taken from the credentials.
      region: The region to make requests to.
      model_publisher: The model publisher to use, I couldn't find a good list of available publishers,
        and from trial and error it seems non-google models don't work with the `generateContent` and
        `streamGenerateContent` functions, hence only `google` is currently supported.
        Please create an issue or PR if you know how to use other publishers.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
      url_template: URL template for Vertex AI, see

      
      
      
      
      
        
      
      
      
    
    
    
     
     
     
    
    
        
     
      
      
      
      
      
      
      
    
       
"""Initialize the model, setting the URL and auth.

    This will raise an error if authentication fails.

             
        
        
           
            
           
        
    
          
        
       
         
         'No project_id provided and none found in 
        
    
              
         
          'The project_id you provided does not match the one from 
          
        
        
        
      
      
      
      
    
        
      
     
     

```

  
---  
Initialize a Vertex AI Gemini model.

The name of the model to use. I couldn't find a list of supported Google models,
in VertexAI so for now this uses the same models as the .  
---  
Path to a service account file. If not provided, the default environment
credentials will be used.  
The project ID to use, if not provided it will be taken from the credentials.  
The region to make requests to.  
The model publisher to use, I couldn't find a good list of available publishers,
and from trial and error it seems non-google models don't work with the and
functions, hence only is currently supported. Please create an issue or PR if
you know how to use other publishers.  
An existing to use for making HTTP requests.  
URL template for Vertex AI, see for more information.  
```



  
  
  
         
       
     
     
       
     

"""Initialize a Vertex AI Gemini model.

    model_name: The name of the model to use. I couldn't find a list of supported Google models, in VertexAI
      so for now this uses the same models as the [Gemini model][pydantic_ai.models.gemini.GeminiModel].
    service_account_file: Path to a service account file.
      If not provided, the default environment credentials will be used.
    project_id: The project ID to use, if not provided it will be taken from the credentials.
    region: The region to make requests to.
    model_publisher: The model publisher to use, I couldn't find a good list of available publishers,
      and from trial and error it seems non-google models don't work with the `generateContent` and
      `streamGenerateContent` functions, hence only `google` is currently supported.
      Please create an issue or PR if you know how to use other publishers.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    url_template: URL template for Vertex AI, see

    
    
    
    
    
      
    
    
    

```

  
---  
Initialize the model, setting the URL and auth.

This will raise an error if authentication fails.

```

     
"""Initialize the model, setting the URL and auth.

  This will raise an error if authentication fails.

           
      
      
         
          
         
      
  
        
      
     
       
       'No project_id provided and none found in 
      
  
            
       
        'The project_id you provided does not match the one from 
        
      
      
      
    
    
    
    
  
      
    

```

  
---  
Authentication using a bearer token generated by google-auth.

```



"""Authentication using a bearer token generated by google-auth."""

     
        
       
         
       
        
      
     
       
       
    
           
     
    
       'Expected token to be a string, got 
     

```

  
---  
Regions available for Vertex AI.

---

# pydantic_ai.models.groq
URL: https://ai.pydantic.dev/api/models/groq/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

For details on how to set up authentication with this model, see .

See for a full list.

A model that uses the Groq API.

Internally, this uses the to interact with the API.

Apart from , all methods are private or match those of the base class.

```



"""A model that uses the Groq API.

  Internally, this uses the [Groq Python client](https://github.com/groq/groq-
python) to interact with the API.

  Apart from `__init__`, all methods are private or match those of the base
class.

  
     
  
    
     
    
         
         
         
  

      model_name: The name of the Groq model to use. List of model names available

      api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
        will be used if available.

        client to use, if provided, `api_key` and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

      
        
          'Cannot provide both `groq_client` and `http_client`'
          'Cannot provide both `groq_client` and `api_key`'
        
        
         
    
         
    
    
    
     
     
     
    
    
          
     
            
     
      
      
      
      
    
     
     
  
      
     
       
       
         
         
         
      
    

```

  
---  
The name of the Groq model to use. List of model names available .  
---  
The API key to use for authentication, if not provided, the environment variable
will be used if available.  
An existing client to use, if provided, and must be .  
An existing to use for making HTTP requests.  
```



  
  
  
       
       
       

    model_name: The name of the Groq model to use. List of model names available

    api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
      will be used if available.

      client to use, if provided, `api_key` and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

    
      
        'Cannot provide both `groq_client` and `http_client`'
        'Cannot provide both `groq_client` and `api_key`'
      
      
       
  
       

```

  
---  
```



"""Implementation of `AgentModel` for Groq models."""

  
  
  
  
    
          
     
         
      
  
    
          
    
         
      
        
  
    
            
    
    
  
    
            
    
    
    
            
      
    # standalone function to make it easier to override
      
             
      
        
    
        
          
        
      
      
      
      
          
        
        
      
       
       
       
       
    
  
      
"""Process a non-streamed response, and prepare a message to return."""

       
      
       
        
      
        
         
        
            
        
      
  
       
"""Process a streamed response, and prepare a streaming response to return."""

      
       
      
       'Streamed response ended without content or tool calls'
       
  
       
"""Just maps a `pydantic_ai.Message` to a
`groq.types.ChatCompletionMessageParam`."""

      
       
      
         
         
         
          
          
          
          
        
          
        
       
        # Note: model responses from this model should only have one text item, so the following
        # shouldn't merge multiple texts into one unless you switch models between runs:
          
       
          
       
    
      
  
       
       
        
          
        
          
        
         
          
           
          
        
        
           
            
        
           
            
             
            
          

```

  
---  
```



"""Implementation of `StreamedResponse` for Groq models."""

  
  
      
        
        
      
          
       
        
      # Handle the text part of the response
        
          
          
      # Handle the tool calls
           
          
          
            
            
          
        
            
           
     
     

```

  
---

---

# pydantic_ai.models.mistral
URL: https://ai.pydantic.dev/api/models/mistral/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

For details on how to set up authentication with this model, see .

Latest / most popular named Mistral models.

Since Mistral supports a variety of date-stamped models, we explicitly list the
most popular models but allow any name in the type hints. Since for a full list.

A model that uses Mistral.

Internally, this uses the to interact with the API.

```



"""A model that uses Mistral.

  Internally, this uses the [Mistral Python
client](https://github.com/mistralai/client-python) to interact with the API.

  
     
  
    
     
    
              
         
         
  

      model_name: The name of the model to use.
      api_key: The API key to use for authentication, if unset uses `MISTRAL_API_KEY` environment variable.
      client: An existing `Mistral` client to use, if provided, `api_key` and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

      
        
          'Cannot provide both `mistral_client` and `http_client`'
          'Cannot provide both `mistral_client` and `api_key`'
        
    
              
           
    
    
    
     
     
     
    
"""Create an agent model, this is called for each step of an agent run from
Pydantic AI call."""

    
     
      
      
      
      
      
    
     
     

```

  
---  
The name of the model to use.  
---  
The API key to use for authentication, if unset uses environment variable.  
An existing client to use, if provided, and must be .  
An existing to use for making HTTP requests.  
```



  
  
  
            
       
       

    model_name: The name of the model to use.
    api_key: The API key to use for authentication, if unset uses `MISTRAL_API_KEY` environment variable.
    client: An existing `Mistral` client to use, if provided, `api_key` and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

    
      
        'Cannot provide both `mistral_client` and `http_client`'
        'Cannot provide both `mistral_client` and `api_key`'
      
  
            
         

```

  
---  
Create an agent model, this is called for each step of an agent run from
Pydantic AI call.

```

  
  
  
  
  
  
  
"""Create an agent model, this is called for each step of an agent run from
Pydantic AI call."""

  
  
    
    
    
    
    
  

```

  
---  
```



"""Implementation of `AgentModel` for Mistral models."""

  
  
  
  
  
     """Answer in JSON Object, respect the format:
    
          
     
"""Make a non-streaming request to the model from Pydantic AI call."""

        
      
  
    
          
    
"""Make a streaming request to the model from Pydantic AI call."""

        
      
         
    
          
    
"""Make a non-streaming request to the model."""

        
       
      
          
      
        
      
      
       
       
       
      
    
      'A unexpected empty response from Mistral.'
     
    
    
     
       
    
"""Create a streaming completion request to the Mistral model."""

       
          
        
         
      
         
        
        
        
          
        
         
         
         
        
      
     
      
            
        
      
         
        
        
         
        
      
    
      
         
        
        
        
      
      'A unexpected empty response from Mistral.'
     
       
"""Get tool choice for the model.

    - "auto": Default mode. Model decides if it uses the tool or not.
    - "any": Select any tool.
    - "none": Prevents tool use.
    - "required": Forces tool use.

         
       
      
       
    
       
       
"""Map function and result tools to MistralTool format.

    Returns None if both function_tools and result_tools are empty.

         
      
      
          
      
         
    
         
  
      
"""Process a non-streamed response, and prepare a message to return."""

      
     
         
    
        
      
      
      
       
       
      
      
         
          
        
      
  
    
     
     
    
"""Process a streamed response, and prepare a streaming response to return."""

      
       
      
       'Streamed response ended without content or tool calls'
     
         
    
        
            
  
      
"""Maps a pydantic-ai ToolCall to a MistralToolCall."""

      
       
        
        
         
      
    
       
        
        
         
      
        
"""Get a message with an example of the expected output format."""

        
       
          
           
          
      
            
     
  
        
"""Return a string representation of the Python type for a single JSON schema
property.

    This function handles recursion for nested arrays/objects and `anyOf`.

    # 1) Handle anyOf first, because it's a different schema structure
       
      # Simplistic approach: pick the first option in anyOf
      # (In reality, you'd possibly want to merge or union types)
       
    # 2) If we have a top-level "type" field
      
      
      # No explicit type; fallback
       
    # 3) Direct simple type mapping (string, integer, float, bool, None)
               
       
    # 4) Array: Recursively get the item type
       
         
       
    # 5) Object: Check for additionalProperties
       
         
        
       
          
           
           
      
        
         
         
           
         
         
        # nested dictionary of unknown shape
         
      
        # If no additionalProperties type or something else, default to a generic dict
         
    
     
  
            
"""Convert a timeout to milliseconds."""

       
       
      
         
     'Timeout object is not yet supported for MistralModel.'
  
       
       
        
         
        
         
        
         
          
          
        
        
           
           
        
           
            
            
          
      
        
  
       
"""Just maps a `pydantic_ai.Message` to a `MistralMessage`."""

      
       
      
         
         
         
          
          
          
          
        
          
        
    
      

```

  
---  
Make a non-streaming request to the model from Pydantic AI call.

```

  
        
  
"""Make a non-streaming request to the model from Pydantic AI call."""

      
    

```

  
---  
Make a streaming request to the model from Pydantic AI call.

```

  
        
  
"""Make a streaming request to the model from Pydantic AI call."""

      
    
       

```

  
---  
```



"""Implementation of `StreamedResponse` for Mistral models."""

  
  
    
      
      
     
        
        
      
          
       
        
      # Handle the text part of the response
        
        
       
        # Attempt to produce a result tool call from the received text
         
            
             
           
             
              
              
              
              
            
        
            
      # Handle the explicit tool calls
            
        # It seems that mistral just sends full tool calls, so we just use them directly, rather than building
         
             
        
     
     
  
           
           
     
         
        # NOTE: Additional verification to prevent JSON validation to crash in `_result.py`
        # Ensures required parameters in the JSON schema are respected, especially for stream-based return types.
        # Example with BaseModel and required fields.
          
           
        
          
        # The following part_id will be thrown away
          
  
          
"""Validate that all required parameters in the JSON schema are present in the
JSON dictionary."""

       
       
       
          
         
         
        
         
           
           
           
           
             
             
           
         
            
          
           
           
     

```

  
---

---

# pydantic_ai.models.ollama
URL: https://ai.pydantic.dev/api/models/ollama/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

For details on how to set up authentication with this model, see .

With installed, you can run the server with the model you want to use:

(this will pull the model if you don't already have it downloaded)

Then run your code, here's a minimal example:

```

  
  



  
  

  
  'Where were the olympics held in 2012?'

Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65,
details=None)

```

## Example using a remote server

```

  
  
  
  
  
  



  
  

  
  'Where were the olympics held in 2012?'

Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65,
details=None)

```

This contains just the most common ollama models.

For a full list see .

Since Ollama supports hundreds of models, we explicitly list the most models but
allow any name in the type hints.

A model that implements Ollama using the OpenAI API.

Internally, this uses the to interact with the Ollama server.

Apart from , all methods are private or match those of the base class.

```



"""A model that implements Ollama using the OpenAI API.

  Internally, this uses the [OpenAI Python
client](https://github.com/openai/openai-python) to interact with the Ollama
server.

  Apart from `__init__`, all methods are private or match those of the base
class.

  
  
  
    
     
    
         
       
         
         
  

    Ollama has built-in compatability for the OpenAI chat completions API ([source](https://ollama.com/blog/openai-compatibility)), so we reuse the

      model_name: The name of the Ollama model to use. List of models available [here](https://ollama.com/library)
        You must first download the model (`ollama pull <MODEL-NAME>`) in order to use the model
      base_url: The base url for the ollama requests. The default value is the ollama default
      api_key: The API key to use for authentication. Defaults to 'ollama' for local instances,
        but can be customized for proxy setups that require authentication

        client to use, if provided, `base_url` and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

      
        
          'Cannot provide both `openai_client` and `base_url`'
          'Cannot provide both `openai_client` and `http_client`'
         
    
      # API key is not required for ollama but a value is required to create the client
          
          
         
    
    
    
     
     
     
    
    
      
      
      
      
    
     
     

```

  
---  
Ollama has built-in compatability for the OpenAI chat completions API (), so we
reuse the here.

The name of the Ollama model to use. List of models available You must first
download the model () in order to use the model  
---  
The base url for the ollama requests. The default value is the ollama default  
The API key to use for authentication. Defaults to 'ollama' for local instances,
but can be customized for proxy setups that require authentication  
An existing client to use, if provided, and must be .  
An existing to use for making HTTP requests.  
```



  
  
  
       
     
       
       

  Ollama has built-in compatability for the OpenAI chat completions API
([source](https://ollama.com/blog/openai-compatibility)), so we reuse the

    model_name: The name of the Ollama model to use. List of models available [here](https://ollama.com/library)
      You must first download the model (`ollama pull <MODEL-NAME>`) in order to use the model
    base_url: The base url for the ollama requests. The default value is the ollama default
    api_key: The API key to use for authentication. Defaults to 'ollama' for local instances,
      but can be customized for proxy setups that require authentication

      client to use, if provided, `base_url` and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.

    
      
        'Cannot provide both `openai_client` and `base_url`'
        'Cannot provide both `openai_client` and `http_client`'
       
  
    # API key is not required for ollama but a value is required to create the client
        
        
       

```

  
---

---

# pydantic_ai.models.test
URL: https://ai.pydantic.dev/api/models/test/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Utility model for quickly testing apps built with PydanticAI.

```

  
  
  

  
"""Unit test for my_agent, to be run by pytest."""

    
  
       
       
     

```

See for detailed documentation.

A model specifically for testing purposes.

This will (by default) call all tools in the agent, then return a tool response
if possible, otherwise a plain response.

How useful this model is will vary significantly.

Apart from derived by the decorator, all methods are private or match those of
the base class.

```



"""A model specifically for testing purposes.

  This will (by default) call all tools in the agent, then return a tool
response if possible,

  How useful this model is will vary significantly.

  Apart from `__init__` derived by the `dataclass` decorator, all methods are
private or match those

  # NOTE: Avoid test discovery by pytest.

    
       
"""List of tools to call. If `'all'`, all tools will be called."""

       
"""If set, this text is return as the final result."""

       
"""If set, these args will be passed to the result tool."""

     
"""Seed for generating random data."""

        
"""Definition of function tools passed to the model.

  This is set when the model is called, so will reflect the function tools from
the last step of the last run.

        
"""Whether plain text responses from the model are allowed.

  This is set when the model is called, so will reflect the value from the last
step of the last run.

        
"""Definition of result tools passed to the model.

  This is set when the model is called, so will reflect the result tools from
the last step of the last run.

    
    
    
     
     
     
    
      
      
      
       
             
    
             
            
             
        
        'Plain response not allowed, but `custom_result_text` is set.'
          'Cannot set both `custom_result_text` and `custom_result_args`.'
              
        
           'No result tools provided, but `custom_result_args` is set.'
        
         
           
      
          
     
        
     
        
    
        
        
     
     

```

  
---  
List of tools to call. If , all tools will be called.

If set, this text is return as the final result.

If set, these args will be passed to the result tool.

Seed for generating random data.

Definition of function tools passed to the model.

This is set when the model is called, so will reflect the function tools from
the last step of the last run.

Whether plain text responses from the model are allowed.

This is set when the model is called, so will reflect the value from the last
step of the last run.

Definition of result tools passed to the model.

This is set when the model is called, so will reflect the result tools from the
last step of the last run.

```



"""Implementation of `AgentModel` for testing purposes."""

  # NOTE: Avoid test discovery by pytest.

    
    
  # left means the text is plain text; right means it's a function call

        
  
  
    
          
     
       
       
      
  
    
          
    
       
      
       
      
           
    # if there are tools, the first thing we want to do is call all of them
             
       
              
      
     
        
         'Expected last message to be a `ModelRequest`.'
      # check if there are any retry prompts, if so retry them
               
       
        # Handle retries for both function tools and result tools
        # Check function tools first
           
           
              
             
        
        
         
          
            
               
                 
                 
            
          
         
       
         
        # build up details of tool responses
            
           
            
               
                
                  
         
           
        
           
      
         
    
        
        
          
          
          
      
          
          

```

  
---  
A structured response that streams test data.

```



"""A structured response that streams test data."""

  
  
      
     
      
      
        
        
          
           
              
        
               
              
             
          
          
           
            
            
      
               
         
             
        
     
     

```

  
---

---

# pydantic_ai.models.function
URL: https://ai.pydantic.dev/api/models/function/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

A model controlled by a local function.

is similar to , but allows greater control over the model's behavior.

Its primary use case is for more advanced unit testing than is possible with .

```

  
    
    
  

  
     
  
  

  

  

  
"""Unit test for my_agent, to be run by pytest."""

  
       
       

```

See for detailed documentation.

A model controlled by a local function.

Apart from , all methods are private or match those of the base class.

```



"""A model controlled by a local function.

  Apart from `__init__`, all methods are private or match those of the base
class.

       
       
  
        
  
         
  
           
                

    Either `function` or `stream_function` must be provided, providing both is allowed.

      function: The function to call for non-streamed requests.
      stream_function: The function to call for streamed requests.

           
       'Either `function` or `stream_function` must be provided'
      
      
    
    
    
     
     
     
    
     
           
    
     
       
        
      
        
      
     

```

  
---  
Either or must be provided, providing both is allowed.

The function to call for non-streamed requests.  
---  
The function to call for streamed requests.  
```

              

  Either `function` or `stream_function` must be provided, providing both is
allowed.

    function: The function to call for non-streamed requests.
    stream_function: The function to call for streamed requests.

         
     'Either `function` or `stream_function` must be provided'
    
    

```

  
---  
This is passed as the second to functions used within .

```



  This is passed as the second to functions used within
[`FunctionModel`][pydantic_ai.models.function.FunctionModel].

  
"""The function tools available on this agent.

  These are the tools registered via the [`tool`][pydantic_ai.Agent.tool] and

  
"""Whether a plain text result is allowed."""

  
"""The tools that can called as the final result of the run."""

     
"""The model settings passed to the run call."""

```

  
---  
The function tools available on this agent.

These are the tools registered via the and decorators.

Whether a plain text result is allowed.

The tools that can called as the final result of the run.

The model settings passed to the run call.

Incremental change to a tool call.

Used to describe a chunk when streaming structured responses.

```



"""Incremental change to a tool call.

  Used to describe a chunk when streaming structured responses.

       
"""Incremental change to the name of the tool."""

       
"""Incremental change to the arguments as JSON"""

```

  
---  
Incremental change to the name of the tool.

Incremental change to the arguments as JSON

A mapping of tool call IDs to incremental changes.

A function used to generate a non-streamed response.

A function used to generate a streamed response.

While this is defined as having return type of , it should really be considered
as ,

E.g. you need to yield all text or all , not mix them.

```



"""Implementation of `AgentModel` for
[FunctionModel][pydantic_ai.models.function.FunctionModel]."""

     
     
  
    
          
     
       
         'FunctionModel must receive a `function` to support non-streamed requests'
     
          
    
           
         
        
    # TODO is `messages` right here? Should it just be new messages?
       
  
    
          
    
     
         
     'FunctionModel must receive a `stream_function` to support streamed requests'
       
       
      
       'Stream function must return at least one item'
     

```

  
---  
```



"""Implementation of `StreamedResponse` for
[FunctionModel][pydantic_ai.models.function.FunctionModel]."""

     
     
  
      
      
        
        
          
           
          
      
          
            
           
              
               
            
            
            
            
            
          
              
             
     
     

```

  
---

---

# pydantic_graph
URL: https://ai.pydantic.dev/api/pydantic_graph/graph/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

In , a graph is a collection of nodes that can be run in sequence. The nodes
define their outgoing edges — e.g. which nodes may be run next, and thereby the
structure of the graph.

Here's a very simple example of a graph which increments a number by 1, but
makes sure the number is never 42 at the end.

_(This example is complete, it can be run "as is")_

See For an example of running graph, and for an example of generating a mermaid
diagram from the graph.

```

  

  In `pydantic-graph`, a graph is a collection of nodes that can be run in
sequence. The nodes define

  their outgoing edges — e.g. which nodes may be run next, and thereby the
structure of the graph.

  Here's a very simple example of a graph which increments a number by 1, but
makes sure the number is never

  from pydantic_graph import BaseNode, End, Graph, GraphRunContext

    async def run(self, ctx: GraphRunContext) -> Check42:

    async def run(self, ctx: GraphRunContext) -> Increment | End[int]:

  _(This example is complete, it can be run "as is")_

  See [`run`][pydantic_graph.graph.Graph.run] For an example of running graph,
and

  [`mermaid_code`][pydantic_graph.graph.Graph.mermaid_code] for an example of
generating a mermaid diagram

     
      
    
       
       
  
    
    
       
         
         
         
        
  
"""Create a graph from a sequence of nodes.

      nodes: The nodes which make up the graph, nodes need to be unique and all be generic in the same

      name: Optional name for the graph, if not provided the name will be inferred from the calling frame
        on the first call to a graph method.
      state_type: The type of the state for the graph, this can generally be inferred from `nodes`.
      run_end_type: The type of the result of running the graph, this can generally be inferred from `nodes`.
      snapshot_state: A function to snapshot the state of the graph, this is used in
        [`NodeStep`][pydantic_graph.state.NodeStep] and [`EndStep`][pydantic_graph.state.EndStep] to record
        the state before each step.

      
      
      
      
      
          
       
       
    
    
    
       
    
       
       
       
      
"""Run the graph from a starting node until it ends.

      start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,
        you need to provide the starting node.
      state: The initial state of the graph.
      deps: The dependencies of the graph.
      infer_name: Whether to infer the graph name from the calling frame.

      The result type from ending the run and the history of the run.
    Here's an example of running the graph from [above][pydantic_graph.graph.Graph]:

    from never_42 import Increment, MyState, never_42_graph

      _, history = await never_42_graph.run(Increment(), state=state)

      _, history = await never_42_graph.run(Increment(), state=state)

         
      
        
     
      
        
      
      
       
               
          
          
           
            
          
            
        
           
            
          
             
              'Invalid node return type: ``. Expected `BaseNode` or `End`.'
            
  
    
       
    
       
       
       
      

    This is a convenience method that wraps [`self.run`][pydantic_graph.Graph.run] with `loop.run_until_complete(...)`.
    You therefore can't use this method inside async code or if there's an active event loop.

      start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,
        you need to provide the starting node.
      state: The initial state of the graph.
      deps: The dependencies of the graph.
      infer_name: Whether to infer the graph name from the calling frame.

      The result type from ending the run and the history of the run.

         
      
     
         
    
    
    
       
      
    
       
       
       
        
"""Run a node in the graph and return the next node to run.

      node: The node to run.
      history: The history of the graph run so far. NOTE: this will be mutated to add the new step.
      state: The current state of the graph.
      deps: The dependencies of the graph.
      infer_name: Whether to infer the graph name from the calling frame.

      The next node to run or [`End`][pydantic_graph.nodes.End] if the graph has finished.

         
      
      
        
       ` is not in the graph.'
       
       
        
        
         
          
    
          
    
     
               
"""Dump the history of a graph run as JSON.

      history: The history of the graph run.
      indent: The number of spaces to indent the JSON.

      The JSON representation of the history.

      
            
"""Load the history of a graph run from JSON.

      json_bytes: The JSON representation of the history.

      The history of the graph run.

     
  
      
          
      
      
      
    
          
    
      
     
  
    
    
           
           
       
       
           
       
       
    
"""Generate a diagram representing the graph as
[mermaid](https://mermaid.js.org/) diagram.

      start_node: The node or nodes which can start the graph.
      title: The title of the diagram, use `False` to not include a title.
      edge_labels: Whether to include edge labels.
      notes: Whether to include notes on each node.
      highlighted_nodes: Optional node or nodes to highlight.
      highlight_css: The CSS to use for highlighting nodes.
      infer_name: Whether to infer the graph name from the calling frame.

      The mermaid code for the graph, which can then be rendered as a diagram.
    Here's an example of generating a diagram for the graph from [above][pydantic_graph.graph.Graph]:

    from never_42 import Increment, never_42_graph

    The rendered diagram will look like this:

         
      
         
        
     
      
      
      
      
        
      
      
    
  
          
    
"""Generate a diagram representing the graph as an image.

    The format and diagram can be customized using `kwargs`,

    !!! note "Uses external service"
      This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`
      is a free service not affiliated with Pydantic.

      infer_name: Whether to infer the graph name from the calling frame.
      **kwargs: Additional arguments to pass to `mermaid.request_image`.

         
      
          
        
      
  
                
    
"""Generate a diagram representing the graph and save it as an image.

    The format and diagram can be customized using `kwargs`,

    !!! note "Uses external service"
      This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`
      is a free service not affiliated with Pydantic.

      path: The path to save the image to.
      infer_name: Whether to infer the graph name from the calling frame.
      **kwargs: Additional arguments to pass to `mermaid.save_image`.

         
      
          
        
      
     
     
       
       
         
           
            
           
             
          # break the inner (bases) loop
          
    # state defaults to None, so use that if we can't infer it
      
     
     
       
       
         
           
            
             
              
              
               
          # break the inner (bases) loop
          
     'Could not infer run end type from nodes, please set `run_end_type`.'
  
             
    
      
       
       
        ` is not unique — found on 
      
    
        
  
      
        
        
         
            
           
     
             
         
          but not included in the graph.'
      
              
         
          'Nodes are referenced in the graph but not included in the graph:
        
         
"""Infer the agent name from the call frame.

        
             
          
           
            
          
         
        # if we couldn't find the agent in locals and globals are a different dict, try globals
            
             
              
            

```

  
---  
Create a graph from a sequence of nodes.

The nodes which make up the graph, nodes need to be unique and all be generic in
the same state type.  
---  
Optional name for the graph, if not provided the name will be inferred from the
calling frame on the first call to a graph method.  
The type of the state for the graph, this can generally be inferred from .  
The type of the result of running the graph, this can generally be inferred from
.  
A function to snapshot the state of the graph, this is used in and to record the
state before each step.  
```



  
  
     
       
       
       
      

"""Create a graph from a sequence of nodes.

    nodes: The nodes which make up the graph, nodes need to be unique and all be generic in the same

    name: Optional name for the graph, if not provided the name will be inferred from the calling frame
      on the first call to a graph method.
    state_type: The type of the state for the graph, this can generally be inferred from `nodes`.
    run_end_type: The type of the result of running the graph, this can generally be inferred from `nodes`.
    snapshot_state: A function to snapshot the state of the graph, this is used in
      [`NodeStep`][pydantic_graph.state.NodeStep] and [`EndStep`][pydantic_graph.state.EndStep] to record
      the state before each step.

    
    
    
    
    
        
     
     
  

```

  
---  
Run the graph from a starting node until it ends.

the first node to run, since the graph definition doesn't define the entry point
in the graph, you need to provide the starting node.  
---  
The initial state of the graph.  
The dependencies of the graph.  
Whether to infer the graph name from the calling frame.  
The result type from ending the run and the history of the run.  
---  
Here's an example of running the graph from :

```

     
  
    
       
  
  
  
  
    
       
  
  
  
  

```

```

  
  
     
  
     
     
     
    
"""Run the graph from a starting node until it ends.

    start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,
      you need to provide the starting node.
    state: The initial state of the graph.
    deps: The dependencies of the graph.
    infer_name: Whether to infer the graph name from the calling frame.

    The result type from ending the run and the history of the run.
  Here's an example of running the graph from
[above][pydantic_graph.graph.Graph]:

  from never_42 import Increment, MyState, never_42_graph

    _, history = await never_42_graph.run(Increment(), state=state)

    _, history = await never_42_graph.run(Increment(), state=state)

       
    
      
  
    
      
    
    
     
             
        
        
         
          
        
          
      
         
          
        
           
            'Invalid node return type: ``. Expected `BaseNode` or `End`.'
          

```

  
---  
This is a convenience method that wraps with . You therefore can't use this
method inside async code or if there's an active event loop.

the first node to run, since the graph definition doesn't define the entry point
in the graph, you need to provide the starting node.  
---  
The initial state of the graph.  
The dependencies of the graph.  
Whether to infer the graph name from the calling frame.  
The result type from ending the run and the history of the run.  
---  
```



  
     
  
     
     
     
    

  This is a convenience method that wraps [`self.run`][pydantic_graph.Graph.run]
with `loop.run_until_complete(...)`.

  You therefore can't use this method inside async code or if there's an active
event loop.

    start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,
      you need to provide the starting node.
    state: The initial state of the graph.
    deps: The dependencies of the graph.
    infer_name: Whether to infer the graph name from the calling frame.

    The result type from ending the run and the history of the run.

       
    
  
       
  

```

  
---  
Run a node in the graph and return the next node to run.

The history of the graph run so far. NOTE: this will be mutated to add the new
step.  
---  
The current state of the graph.  
The dependencies of the graph.  
Whether to infer the graph name from the calling frame.  
The next node to run or if the graph has finished.  
---  
```

  
  
     
    
  
     
     
     
      
"""Run a node in the graph and return the next node to run.

    node: The node to run.
    history: The history of the graph run so far. NOTE: this will be mutated to add the new step.
    state: The current state of the graph.
    deps: The dependencies of the graph.
    infer_name: Whether to infer the graph name from the calling frame.

    The next node to run or [`End`][pydantic_graph.nodes.End] if the graph has finished.

       
    
    
      
     ` is not in the graph.'
     
     
      
      
       
        
  
        
  
  

```

  
---  
Dump the history of a graph run as JSON.

The history of the graph run.  
---  
The number of spaces to indent the JSON.  
The JSON representation of the history.  
---  
```

             
"""Dump the history of a graph run as JSON.

    history: The history of the graph run.
    indent: The number of spaces to indent the JSON.

    The JSON representation of the history.

    

```

  
---  
Load the history of a graph run from JSON.

The JSON representation of the history.  
---  
The history of the graph run.  
---  
```

          
"""Load the history of a graph run from JSON.

    json_bytes: The JSON representation of the history.

    The history of the graph run.

  

```

  
---  
Generate a diagram representing the graph as diagram.

The node or nodes which can start the graph.  
---  
The title of the diagram, use to not include a title.  
Whether to include edge labels.  
Whether to include notes on each node.  
Optional node or nodes to highlight.  
The CSS to use for highlighting nodes.  
Whether to infer the graph name from the calling frame.  
The mermaid code for the graph, which can then be rendered as a diagram.  
---  
Here's an example of generating a diagram for the graph from :

```

    

```

The rendered diagram will look like this:

```



  
  
         
         
     
     
         
     
     
  
"""Generate a diagram representing the graph as
[mermaid](https://mermaid.js.org/) diagram.

    start_node: The node or nodes which can start the graph.
    title: The title of the diagram, use `False` to not include a title.
    edge_labels: Whether to include edge labels.
    notes: Whether to include notes on each node.
    highlighted_nodes: Optional node or nodes to highlight.
    highlight_css: The CSS to use for highlighting nodes.
    infer_name: Whether to infer the graph name from the calling frame.

    The mermaid code for the graph, which can then be rendered as a diagram.
  Here's an example of generating a diagram for the graph from
[above][pydantic_graph.graph.Graph]:

  from never_42 import Increment, never_42_graph

  The rendered diagram will look like this:

       
    
       
      
  
    
    
    
    
      
    
    
  

```

  
---  
Generate a diagram representing the graph as an image.

The format and diagram can be customized using , see .

This method makes a request to to render the image, is a free service not
affiliated with Pydantic.

Whether to infer the graph name from the calling frame.  
---  
Additional arguments to pass to .  
```



        
  
"""Generate a diagram representing the graph as an image.

  The format and diagram can be customized using `kwargs`,

  !!! note "Uses external service"

    This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`
    is a free service not affiliated with Pydantic.

    infer_name: Whether to infer the graph name from the calling frame.
    **kwargs: Additional arguments to pass to `mermaid.request_image`.

       
    
        
      
    

```

  
---  
Generate a diagram representing the graph and save it as an image.

The format and diagram can be customized using , see .

This method makes a request to to render the image, is a free service not
affiliated with Pydantic.

The path to save the image to.  
---  
Whether to infer the graph name from the calling frame.  
Additional arguments to pass to .  
```



              
  
"""Generate a diagram representing the graph and save it as an image.

  The format and diagram can be customized using `kwargs`,

  !!! note "Uses external service"

    This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`
    is a free service not affiliated with Pydantic.

    path: The path to save the image to.
    infer_name: Whether to infer the graph name from the calling frame.
    **kwargs: Additional arguments to pass to `mermaid.save_image`.

       
    
        
      
    

```

  
---

---

# pydantic_graph.nodes
URL: https://ai.pydantic.dev/api/pydantic_graph/nodes/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

```

  

  
"""The state of the graph."""

  

```

  
---  
The state of the graph.

Base class for a node.

```

    
"""Base class for a node."""

     
"""Set to `True` to generate mermaid diagram notes from the class's docstring.

  While this can add valuable information to the diagram, it can make diagrams
harder to view, hence

  it is disabled by default. You can also customise notes overriding the

  
             

    This is an abstract method that must be implemented by subclasses.
    !!! note "Return types used at runtime"
      The return type of this method are read by `pydantic_graph` at runtime and used to define which
      nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
      and enforced when running the graph.

      The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.

    
  
  
     
"""Get the ID of the node."""

     
  
       
"""Get a note about the node to render on mermaid charts.

    By default, this returns a note only if [`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]
    is `True`. You can override this method to customise the node notes.

      
       
      
    # dataclasses get an automatic docstring which is just their signature, we don't want that
         
        
     
      # remove indentation from docstring
       
        
     
  
            

        
    
        
       
        is missing a return type hint on its `run` method'  
        
         
       
       
         
                
          
         
          
         
        # TODO: Should we disallow this?
          
        
          
      
         
     
      
      
      
      
      
      
    

```

  
---  
Set to to generate mermaid diagram notes from the class's docstring.

While this can add valuable information to the diagram, it can make diagrams
harder to view, hence it is disabled by default. You can also customise notes
overriding the method.

This is an abstract method that must be implemented by subclasses.

Return types used at runtime

The return type of this method are read by at runtime and used to define which
nodes can be called next in the graph. This is displayed in and enforced when
running the graph.

The next node to run or to signal the end of the graph.  
---  
```

           

  This is an abstract method that must be implemented by subclasses.

  !!! note "Return types used at runtime"

    The return type of this method are read by `pydantic_graph` at runtime and used to define which
    nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
    and enforced when running the graph.

    The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.

  

```

  
---  
Get the ID of the node.

```

  
"""Get the ID of the node."""

  

```

  
---  
Get a note about the node to render on mermaid charts.

By default, this returns a note only if is . You can override this method to
customise the node notes.

```

     
"""Get a note about the node to render on mermaid charts.

  By default, this returns a note only if
[`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]

  is `True`. You can override this method to customise the node notes.

    
     
    
  # dataclasses get an automatic docstring which is just their signature, we
don't want that

       
      
  
    # remove indentation from docstring
     
      
  

```

  
---  
```

          

      
  
      
     
      is missing a return type hint on its `run` method'  
      
       
     
     
       
              
        
       
        
       
      # TODO: Should we disallow this?
        
      
        
    
       
  
    
    
    
    
    
    
  

```

  
---  
Type to return from a node to signal the end of the graph.

```



"""Type to return from a node to signal the end of the graph."""

  
"""Data to return from the graph."""

```

  
---  
Data to return from the graph.

Annotation to apply a label to an edge in a graph.

```



"""Annotation to apply a label to an edge in a graph."""

     

```

  
---  
Type variable for the dependencies of a graph and node.

Type variable for the return type of a graph .

Type variable for the return type of a node .

---

# pydantic_graph.state
URL: https://ai.pydantic.dev/api/pydantic_graph/state/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Type variable for the state in a graph.

Default method for snapshotting the state in a graph run, uses .

```

    
"""Default method for snapshotting the state in a graph run, uses
[`copy.deepcopy`][copy.deepcopy]."""

     
     
  
     

```

  
---  
History step describing the execution of a node in a graph.

```

  
"""History step describing the execution of a node in a graph."""

  
"""The state of the graph after the node has been run."""

      
"""The node that was run."""

     
"""The timestamp when the node started running."""

       
"""The duration of the node run in seconds."""

     
"""The kind of history step, can be used as a discriminator when deserializing
history."""

  # TODO waiting for https://github.com/pydantic/pydantic/issues/11264, should
be an InitVar

        
     
  
"""Function to snapshot the state of the graph."""

  
    # Copy the state to prevent it from being modified by other code
      
       
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].

     

```

  
---  
The state of the graph after the node has been run.

The node that was run.

The timestamp when the node started running.

The duration of the node run in seconds.

The kind of history step, can be used as a discriminator when deserializing
history.

Function to snapshot the state of the graph.

Returns a deep copy of .

```

     
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].

  

```

  
---  
History step describing the end of a graph run.

```



"""History step describing the end of a graph run."""

  
"""The result of the graph run."""

     
"""The timestamp when the graph run ended."""

     
"""The kind of history step, can be used as a discriminator when deserializing
history."""

     
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].

     

```

  
---  
The result of the graph run.

The timestamp when the graph run ended.

The kind of history step, can be used as a discriminator when deserializing
history.

Returns a deep copy of .

```

  
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].

  

```

  
---  
A step in the history of a graph run.

returns a list of these steps describing the execution of the graph, together
with the run return value.

---

# pydantic_graph.mermaid
URL: https://ai.pydantic.dev/api/pydantic_graph/mermaid/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

The default CSS to use for highlighting nodes.

Generate code for a graph.

The graph to generate the image for.  
---  
Identifiers of nodes that start the graph.  
Identifiers of nodes to highlight.  
CSS to use for highlighting nodes.  
The title of the diagram.  
Whether to include edge labels in the diagram.  
Whether to include notes in the diagram.  
The Mermaid code for the graph.  
---  
```

  
     
  
  
         
         
     
       
     
     
  
"""Generate [Mermaid state
diagram](https://mermaid.js.org/syntax/stateDiagram.html) code for a graph.

    graph: The graph to generate the image for.
    start_node: Identifiers of nodes that start the graph.
    highlighted_nodes: Identifiers of nodes to highlight.
    highlight_css: CSS to use for highlighting nodes.
    title: The title of the diagram.
    edge_labels: Whether to include edge labels in the diagram.
    notes: Whether to include notes in the diagram.

    The Mermaid code for the graph.

      
     
        
       " is not in the graph.'
     
  
        
  
      
    # we use round brackets (rounded box) for nodes other than the start and end
       
      
     
         
        
    
          
          
           
            
        
       
        
         
          
      
       
      
      # mermaid doesn't like multiple paragraphs in a note, and shows if so
          
       
      
  
    
    
       
          
         " is not in the graph.'
      
  

```

  
---  
Generate an image of a Mermaid diagram using .

The graph to generate the image for.  
---  
Additional parameters to configure mermaid chart generation.  
```



     
  
  
  
"""Generate an image of a Mermaid diagram using
[mermaid.ink](https://mermaid.ink).

    graph: The graph to generate the image for.
    **kwargs: Additional parameters to configure mermaid chart generation.

    
    
    
    
     
    
     
     
  
    
        
     
      
     
        
     
        
       
        
     
      
  
      
       
        
     
      
     
      
     
      
     
      
     
      
      
     
    
     
      
      
      
    
  

```

  
---  
Generate an image of a Mermaid diagram using and save it to a local file.

The path to save the image to.  
---  
The graph to generate the image for.  
Additional parameters to configure mermaid chart generation.  
```



     
     
  
  
  
"""Generate an image of a Mermaid diagram using
[mermaid.ink](https://mermaid.ink) and save it to a local file.

    path: The path to save the image to.
    graph: The graph to generate the image for.
    **kwargs: Additional parameters to configure mermaid chart generation.

    
      
      
      
    # no need to check for .jpeg/.jpg, as it is the default
          
        
     
  

```

  
---  
Parameters to configure mermaid chart generation.

```

  
"""Parameters to configure mermaid chart generation."""

     
"""Identifiers of nodes that start the graph."""

     
"""Identifiers of nodes to highlight."""

  
"""CSS to use for highlighting nodes."""

     
"""The title of the diagram."""

  
"""Whether to include edge labels in the diagram."""

  
"""Whether to include notes on nodes in the diagram, defaults to true."""

       
"""The image type to generate. If unspecified, the default behavior is
`'jpeg'`."""

  
"""When using image_type='pdf', whether to fit the diagram to the PDF page."""

  
"""When using image_type='pdf', whether to use landscape orientation for the
PDF.

  This has no effect if using `pdf_fit`.

             
"""When using image_type='pdf', the paper size of the PDF."""

  
"""The background color of the diagram.

  If None, the default transparent background is used. The color value is
interpreted as a hexadecimal color

  code by default (and should not have a leading '#'), but you can also use
named colors by prefixing the

  value with `'!'`. For example, valid choices include
`background_color='!white'` or `background_color='FF0000'`.

      
"""The theme of the diagram. Defaults to 'default'."""

  
"""The width of the diagram."""

  
"""The height of the diagram."""

     
"""The scale of the diagram.

  The scale must be a number between 1 and 3, and you can only set a scale if
one or both of width and height are set.

  
"""An HTTPX client to use for requests, mostly for testing purposes."""

```

  
---  
Identifiers of nodes that start the graph.

Identifiers of nodes to highlight.

CSS to use for highlighting nodes.

The title of the diagram.

Whether to include edge labels in the diagram.

Whether to include notes on nodes in the diagram, defaults to true.

The image type to generate. If unspecified, the default behavior is .

When using image_type='pdf', whether to fit the diagram to the PDF page.

When using image_type='pdf', whether to use landscape orientation for the PDF.

This has no effect if using .

When using image_type='pdf', the paper size of the PDF.

The background color of the diagram.

If None, the default transparent background is used. The color value is
interpreted as a hexadecimal color code by default (and should not have a
leading '#'), but you can also use named colors by prefixing the value with .
For example, valid choices include or .

The theme of the diagram. Defaults to 'default'.

The width of the diagram.

The height of the diagram.

The scale of the diagram.

The scale must be a number between 1 and 3, and you can only set a scale if one
or both of width and height are set.

An HTTPX client to use for requests, mostly for testing purposes.

```

  
  "type[BaseNode[Any, Any, Any]] | BaseNode[Any, Any, Any] | str"

```

A type alias for a node identifier.

  * A node instance (instance of a subclass of ).
  * A node class (subclass of ).
  * A string representing the node ID.

---

# pydantic_graph.exceptions
URL: https://ai.pydantic.dev/api/pydantic_graph/exceptions/

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Error caused by an incorrectly configured graph.

```



"""Error caused by an incorrectly configured graph."""

  

     
      
    

```

  
---  
Error caused by an issue during graph execution.

```



"""Error caused by an issue during graph execution."""

  

     
      
    

```

  
---

---

# type checking
URL: https://ai.pydantic.dev/agents/#static-type-checking

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Agents are PydanticAI's primary interface for interacting with LLMs.

In some use cases a single Agent will control an entire application or
component, but multiple agents can also interact to embody more complex
workflows.

The class has full API documentation, but conceptually you can think of an agent
as a container for:

A set of instructions for the LLM written by the developer.  
---  
Functions that the LLM may call to get information while generating a response.  
The structured datatype the LLM must return at the end of a run, if specified.  
System prompt functions, tools, and result validators may all use dependencies
when they're run.  
Optional default LLM model associated with the agent. Can also be specified when
running the agent.  
Optional default model settings to help fine tune requests. Can also be
specified when running the agent.  
In typing terms, agents are generic in their dependency and result types, e.g.,
an agent which required dependencies of type and returned results of type would
have type . In practice, you shouldn't need to care about this, it should just
mean your IDE can tell you when you have the right type, and if you choose to
use it should work well with PydanticAI.

Here's a toy example of an agent that simulates a roulette wheel:

```

    
  
  
  
  
  
    'Use the `roulette_wheel` function to see if the '
    'customer has won based on the number they provide.'
  

        
"""check if the square is a winner"""

         

  
  'Put my money on square eighteen'



  'I bet five is the winner'

```

Agents are designed for reuse, like FastAPI Apps

Agents are intended to be instantiated once (frequently as module globals) and
reused throughout your application, similar to a small app or an .

There are three ways to run an agent:

  1. — a coroutine which returns a containing a completed response
  2. — a plain, synchronous function which returns a containing a completed response (internally, this just calls )
  3. — a coroutine which returns a , which contains methods to stream a response as an async iterable

Here's a simple example demonstrating all three:

```

  
  
  'What is the capital of Italy?'

  
     'What is the capital of France?'
  
  
    'What is the capital of the UK?'  
     
    

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

You can also pass messages from previous runs to continue a conversation or
provide context, as described in .

PydanticAI offers a structure to help you limit your usage (tokens and/or
requests) on model runs.

You can apply these settings by passing the argument to the functions.

Consider the following example, where we limit the number of response tokens:

```

  
  
  
  
  
  'What is the capital of Italy? Answer with just the city.'

  

Usage(requests=1, request_tokens=62, response_tokens=1, total_tokens=63,
details=None)

    
    'What is the capital of Italy? Answer with a paragraph.'
    
  
  
  
  #> Exceeded the response_tokens_limit of 10 (response_tokens=32)

```

Restricting the number of requests can be useful in preventing infinite loops or
excessive tool calling:

```

  
    
  
  



  Never ever coerce data to this type.

  

  
  
  
  'Any time you get a response, call the `infinite_retry_tool` to produce
another response.'



  
  

    
      
  
  
  
  #> The next request would exceed the request_limit of 3

```

This is especially relevant if you're registered a lot of tools, can be used to
prevent the model from choosing to make too many of these calls.

PydanticAI offers a structure to help you fine tune your requests. This
structure allows you to configure common parameters that influence the model's
behavior, such as , , , and more.

There are two ways to apply these settings: 1. Passing to functions via the
argument. This allows for fine-tuning on a per-request basis. 2. Setting during
initialization via the argument. These settings will be applied by default to
all subsequent run calls using said agent. However, provided during a specific
run call will override the agent's default settings.

For example, if you'd like to set the setting to to ensure less random behavior,
you can do the following:

```

  
  
  
  'What is the capital of Italy?'  

```

An agent might represent an entire conversation — there's no limit to how many
messages can be exchanged in a single run. However, a might also be composed of
multiple runs, especially if you need to maintain state between separate
interactions or API calls.

Here's an example of a conversation comprised of multiple runs:

```

  
  

  

#> Albert Einstein was a German-born theoretical physicist.

# Second run, passing previous messages

  
  'What was his most famous equation?'

#> Albert Einstein's most famous equation is (E = mc^2).

```

_(This example is complete, it can be run "as is")_

PydanticAI is designed to work well with static type checkers, like mypy and
pyright.

PydanticAI is designed to make type checking as useful as possible for you if
you choose to use it, but you don't have to use types everywhere all the time.

That said, because PydanticAI uses Pydantic, and Pydantic uses type hints as the
definition for schema and validation, some types (specifically type hints on
parameters to tools, and the arguments to ) are used at runtime.

We (the library developers) have messed up if type hints are confusing you more
than helping you, if you find this, please create an explaining what's annoying
you!

In particular, agents are generic in both the type of their dependencies and the
type of results they return, so you can use the type hints to ensure you're
using the right types.

Consider the following script with type mistakes:

```

  
    



  

  
  
  
  

     
  

    
  

  'Does their name start with "A"?'

```

Running on this will give the following output:

Running would identify the same issues.

System prompts might seem simple at first glance since they're just strings (or
sequences of strings that are concatenated), but crafting the right system
prompt is key to getting the model to behave as you want.

Generally, system prompts fall into two categories:

  1. : These are known when writing the code and can be defined via the parameter of the .
  2. : These depend in some way on context that isn't known until runtime, and should be defined via functions decorated with .

You can add both to a single agent; they're appended in the order they're
defined at runtime.

Here's an example using both types of system prompts:

```

  
    
  
  
  
  "Use the customer's name while replying to them."



    
  

    
  

  

#> Hello Frank, the date today is 2032-01-02.

```

_(This example is complete, it can be run "as is")_

Validation errors from both function tool parameter validation and can be passed
back to the model with a request to retry.

You can also raise from within a or to tell the model it should retry generating
a response.

  * The default retry count is but can be altered for the , a , or a .
  * You can access the current retry count from within a tool or result validator via .

```

  
     
  



  
  

  
  
  
  

      
"""Get a user's ID from their full name."""

  
  
  
    
     
     
      'No user found with name , remember to provide their full name'
    
  

  
  'Send a message to John Doe asking for coffee next week'

user_id=123 message='Hello John, would you be free for coffee sometime next
week? Let me know what works for you!'

```

If models behave unexpectedly (e.g., the retry limit is exceeded, or their API
returns ), agent runs will raise .

In these cases, can be used to access the messages exchanged during the run to
help diagnose the issue.

```

      
  

     
     
     
  
     

    
  
      'Please get me the volume of a box with size 6.'
     
     
    #> An error occurred: Tool exceeded max retries count of 1
     
    #> cause: ModelRetry('Please try again.')
     

            content='Please get me the volume of a box with size 6.',

  
    

```

_(This example is complete, it can be run "as is")_

If you call , , or more than once within a single context, will represent the
messages exchanged during the first call only.

---

# validate and structure
URL: https://ai.pydantic.dev/results/#structured-result-validation

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Results are the final values returned from . The result values are wrapped in
and so you can access other data like of the run and

Both and are generic in the data they wrap, so typing information about the data
returned by the agent is preserved.

```

  
  



  
  

  
  'Where were the olympics held in 2012?'

Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65,
details=None)

```

_(This example is complete, it can be run "as is")_

Runs end when either a plain text response is received or the model calls a tool
associated with one of the structured result types. We will add limits to make
sure a run doesn't go on indefinitely, see .

When the result type is , or a union including , plain text responses are
enabled on the model, and the raw text response from the model is used as the
response data.

If the result type is a union with multiple members (after remove from the
members), each member is registered as a separate tool with the model in order
to reduce the complexity of the tool schemas and maximise the chances a model
will respond correctly.

If the result type schema is not of type , the result type is wrapped in a
single element object, so the schema of all tools registered with the model are
object schemas.

Structured results (like tools) use Pydantic to build the JSON schema used for
the tool, and to validate the data returned by the model.

Until "Annotating Type Forms" lands, unions are not valid as s in Python.

When creating the agent we need to the argument, and add a type hint to tell
type checkers about the type of the agent.

Here's an example of returning either text or a structured value

```

  
  
  



  
  
  
  

     
  
    
  
    "Extract me the dimensions of a box, "
    "if you can't extract all data, ask the user to try again."
  

  

#> Please provide the units for the dimensions (e.g., cm, in, m).

  'The box is 10x20x30 cm'

#> width=10 height=20 depth=30 units='cm'

```

_(This example is complete, it can be run "as is")_

Here's an example of using a union return type which registered multiple tools,
and wraps non-object schemas in an object:

```

  
  
     
  
    
  'Extract either colors or sizes from the shapes provided.'

  'red square, blue circle, green triangle'

  'square size 10, circle size 20, triangle size 30'

```

_(This example is complete, it can be run "as is")_

Some validation is inconvenient or impossible to do in Pydantic validators, in
particular when the validation requires IO and is asynchronous. PydanticAI
provides a way to add validation functions via the decorator.

Here's a simplified variant of the :

```

  
    
  
     



  



  

  
    
  
  
  
  'Generate PostgreSQL flavored SQL queries based on user input.'

       
    
     
  
     
     
       
  
     

  
  'get me uses who were last active yesterday.'

#> sql_query='SELECT * FROM users WHERE last_active::date = today() - interval 1
day'

```

_(This example is complete, it can be run "as is")_

There two main challenges with streamed results:

  1. Validating structured responses before they're complete, this is achieved by "partial validation" which was recently added to Pydantic in .
  2. When receiving a response, we don't know if it's the final response without starting to stream it and peeking at the content. PydanticAI streams just enough of the response to sniff out if it's a tool call or a result, then streams the whole thing and calls tools, or returns the stream as a .

Example of streamed text result:

```

  
  

  
    'Where does "hello world" come from?'   
         
      
      
      #> The first known use of "hello,
      #> The first known use of "hello, world" was in
      #> The first known use of "hello, world" was in a 1974 textbook
      #> The first known use of "hello, world" was in a 1974 textbook about the C
      #> The first known use of "hello, world" was in a 1974 textbook about the C programming language.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

We can also stream text as deltas rather than the entire text in each item:

```

  
  

  
    'Where does "hello world" come from?'  
         
      
      
      
      
      
      
      

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

Result message not included in

The final result message will be added to result messages if you use , see for
more information.

Not all types are supported with partial validation in Pydantic, see , generally
for model-like structures it's currently best to use .

Here's an example of streaming a use profile as it's built:

```

  
  
  

  
  
  
  

  
  
  
  'Extract a user profile from the input'

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

If you want fine-grained control of validation, particularly catching validation
errors, you can use the following pattern:

```

  
  
  
  

  
  
  
  

  

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
          
      
            
          
           
        
       
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

The following examples demonstrate how to use streamed responses in PydanticAI:

---

# system prompts
URL: https://ai.pydantic.dev/agents/#system-prompts

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Agents are PydanticAI's primary interface for interacting with LLMs.

In some use cases a single Agent will control an entire application or
component, but multiple agents can also interact to embody more complex
workflows.

The class has full API documentation, but conceptually you can think of an agent
as a container for:

A set of instructions for the LLM written by the developer.  
---  
Functions that the LLM may call to get information while generating a response.  
The structured datatype the LLM must return at the end of a run, if specified.  
System prompt functions, tools, and result validators may all use dependencies
when they're run.  
Optional default LLM model associated with the agent. Can also be specified when
running the agent.  
Optional default model settings to help fine tune requests. Can also be
specified when running the agent.  
In typing terms, agents are generic in their dependency and result types, e.g.,
an agent which required dependencies of type and returned results of type would
have type . In practice, you shouldn't need to care about this, it should just
mean your IDE can tell you when you have the right type, and if you choose to
use it should work well with PydanticAI.

Here's a toy example of an agent that simulates a roulette wheel:

```

    
  
  
  
  
  
    'Use the `roulette_wheel` function to see if the '
    'customer has won based on the number they provide.'
  

        
"""check if the square is a winner"""

         

  
  'Put my money on square eighteen'



  'I bet five is the winner'

```

Agents are designed for reuse, like FastAPI Apps

Agents are intended to be instantiated once (frequently as module globals) and
reused throughout your application, similar to a small app or an .

There are three ways to run an agent:

  1. — a coroutine which returns a containing a completed response
  2. — a plain, synchronous function which returns a containing a completed response (internally, this just calls )
  3. — a coroutine which returns a , which contains methods to stream a response as an async iterable

Here's a simple example demonstrating all three:

```

  
  
  'What is the capital of Italy?'

  
     'What is the capital of France?'
  
  
    'What is the capital of the UK?'  
     
    

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

You can also pass messages from previous runs to continue a conversation or
provide context, as described in .

PydanticAI offers a structure to help you limit your usage (tokens and/or
requests) on model runs.

You can apply these settings by passing the argument to the functions.

Consider the following example, where we limit the number of response tokens:

```

  
  
  
  
  
  'What is the capital of Italy? Answer with just the city.'

  

Usage(requests=1, request_tokens=62, response_tokens=1, total_tokens=63,
details=None)

    
    'What is the capital of Italy? Answer with a paragraph.'
    
  
  
  
  #> Exceeded the response_tokens_limit of 10 (response_tokens=32)

```

Restricting the number of requests can be useful in preventing infinite loops or
excessive tool calling:

```

  
    
  
  



  Never ever coerce data to this type.

  

  
  
  
  'Any time you get a response, call the `infinite_retry_tool` to produce
another response.'



  
  

    
      
  
  
  
  #> The next request would exceed the request_limit of 3

```

This is especially relevant if you're registered a lot of tools, can be used to
prevent the model from choosing to make too many of these calls.

PydanticAI offers a structure to help you fine tune your requests. This
structure allows you to configure common parameters that influence the model's
behavior, such as , , , and more.

There are two ways to apply these settings: 1. Passing to functions via the
argument. This allows for fine-tuning on a per-request basis. 2. Setting during
initialization via the argument. These settings will be applied by default to
all subsequent run calls using said agent. However, provided during a specific
run call will override the agent's default settings.

For example, if you'd like to set the setting to to ensure less random behavior,
you can do the following:

```

  
  
  
  'What is the capital of Italy?'  

```

An agent might represent an entire conversation — there's no limit to how many
messages can be exchanged in a single run. However, a might also be composed of
multiple runs, especially if you need to maintain state between separate
interactions or API calls.

Here's an example of a conversation comprised of multiple runs:

```

  
  

  

#> Albert Einstein was a German-born theoretical physicist.

# Second run, passing previous messages

  
  'What was his most famous equation?'

#> Albert Einstein's most famous equation is (E = mc^2).

```

_(This example is complete, it can be run "as is")_

PydanticAI is designed to work well with static type checkers, like mypy and
pyright.

PydanticAI is designed to make type checking as useful as possible for you if
you choose to use it, but you don't have to use types everywhere all the time.

That said, because PydanticAI uses Pydantic, and Pydantic uses type hints as the
definition for schema and validation, some types (specifically type hints on
parameters to tools, and the arguments to ) are used at runtime.

We (the library developers) have messed up if type hints are confusing you more
than helping you, if you find this, please create an explaining what's annoying
you!

In particular, agents are generic in both the type of their dependencies and the
type of results they return, so you can use the type hints to ensure you're
using the right types.

Consider the following script with type mistakes:

```

  
    



  

  
  
  
  

     
  

    
  

  'Does their name start with "A"?'

```

Running on this will give the following output:

Running would identify the same issues.

System prompts might seem simple at first glance since they're just strings (or
sequences of strings that are concatenated), but crafting the right system
prompt is key to getting the model to behave as you want.

Generally, system prompts fall into two categories:

  1. : These are known when writing the code and can be defined via the parameter of the .
  2. : These depend in some way on context that isn't known until runtime, and should be defined via functions decorated with .

You can add both to a single agent; they're appended in the order they're
defined at runtime.

Here's an example using both types of system prompts:

```

  
    
  
  
  
  "Use the customer's name while replying to them."



    
  

    
  

  

#> Hello Frank, the date today is 2032-01-02.

```

_(This example is complete, it can be run "as is")_

Validation errors from both function tool parameter validation and can be passed
back to the model with a request to retry.

You can also raise from within a or to tell the model it should retry generating
a response.

  * The default retry count is but can be altered for the , a , or a .
  * You can access the current retry count from within a tool or result validator via .

```

  
     
  



  
  

  
  
  
  

      
"""Get a user's ID from their full name."""

  
  
  
    
     
     
      'No user found with name , remember to provide their full name'
    
  

  
  'Send a message to John Doe asking for coffee next week'

user_id=123 message='Hello John, would you be free for coffee sometime next
week? Let me know what works for you!'

```

If models behave unexpectedly (e.g., the retry limit is exceeded, or their API
returns ), agent runs will raise .

In these cases, can be used to access the messages exchanged during the run to
help diagnose the issue.

```

      
  

     
     
     
  
     

    
  
      'Please get me the volume of a box with size 6.'
     
     
    #> An error occurred: Tool exceeded max retries count of 1
     
    #> cause: ModelRetry('Please try again.')
     

            content='Please get me the volume of a box with size 6.',

  
    

```

_(This example is complete, it can be run "as is")_

If you call , , or more than once within a single context, will represent the
messages exchanged during the first call only.

---

# result validators
URL: https://ai.pydantic.dev/results/#result-validators-functions

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Results are the final values returned from . The result values are wrapped in
and so you can access other data like of the run and

Both and are generic in the data they wrap, so typing information about the data
returned by the agent is preserved.

```

  
  



  
  

  
  'Where were the olympics held in 2012?'

Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65,
details=None)

```

_(This example is complete, it can be run "as is")_

Runs end when either a plain text response is received or the model calls a tool
associated with one of the structured result types. We will add limits to make
sure a run doesn't go on indefinitely, see .

When the result type is , or a union including , plain text responses are
enabled on the model, and the raw text response from the model is used as the
response data.

If the result type is a union with multiple members (after remove from the
members), each member is registered as a separate tool with the model in order
to reduce the complexity of the tool schemas and maximise the chances a model
will respond correctly.

If the result type schema is not of type , the result type is wrapped in a
single element object, so the schema of all tools registered with the model are
object schemas.

Structured results (like tools) use Pydantic to build the JSON schema used for
the tool, and to validate the data returned by the model.

Until "Annotating Type Forms" lands, unions are not valid as s in Python.

When creating the agent we need to the argument, and add a type hint to tell
type checkers about the type of the agent.

Here's an example of returning either text or a structured value

```

  
  
  



  
  
  
  

     
  
    
  
    "Extract me the dimensions of a box, "
    "if you can't extract all data, ask the user to try again."
  

  

#> Please provide the units for the dimensions (e.g., cm, in, m).

  'The box is 10x20x30 cm'

#> width=10 height=20 depth=30 units='cm'

```

_(This example is complete, it can be run "as is")_

Here's an example of using a union return type which registered multiple tools,
and wraps non-object schemas in an object:

```

  
  
     
  
    
  'Extract either colors or sizes from the shapes provided.'

  'red square, blue circle, green triangle'

  'square size 10, circle size 20, triangle size 30'

```

_(This example is complete, it can be run "as is")_

Some validation is inconvenient or impossible to do in Pydantic validators, in
particular when the validation requires IO and is asynchronous. PydanticAI
provides a way to add validation functions via the decorator.

Here's a simplified variant of the :

```

  
    
  
     



  



  

  
    
  
  
  
  'Generate PostgreSQL flavored SQL queries based on user input.'

       
    
     
  
     
     
       
  
     

  
  'get me uses who were last active yesterday.'

#> sql_query='SELECT * FROM users WHERE last_active::date = today() - interval 1
day'

```

_(This example is complete, it can be run "as is")_

There two main challenges with streamed results:

  1. Validating structured responses before they're complete, this is achieved by "partial validation" which was recently added to Pydantic in .
  2. When receiving a response, we don't know if it's the final response without starting to stream it and peeking at the content. PydanticAI streams just enough of the response to sniff out if it's a tool call or a result, then streams the whole thing and calls tools, or returns the stream as a .

Example of streamed text result:

```

  
  

  
    'Where does "hello world" come from?'   
         
      
      
      #> The first known use of "hello,
      #> The first known use of "hello, world" was in
      #> The first known use of "hello, world" was in a 1974 textbook
      #> The first known use of "hello, world" was in a 1974 textbook about the C
      #> The first known use of "hello, world" was in a 1974 textbook about the C programming language.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

We can also stream text as deltas rather than the entire text in each item:

```

  
  

  
    'Where does "hello world" come from?'  
         
      
      
      
      
      
      
      

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

Result message not included in

The final result message will be added to result messages if you use , see for
more information.

Not all types are supported with partial validation in Pydantic, see , generally
for model-like structures it's currently best to use .

Here's an example of streaming a use profile as it's built:

```

  
  
  

  
  
  
  

  
  
  
  'Extract a user profile from the input'

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

If you want fine-grained control of validation, particularly catching validation
errors, you can use the following pattern:

```

  
  
  
  

  
  
  
  

  

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
          
      
            
          
           
        
       
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

The following examples demonstrate how to use streamed responses in PydanticAI:

---

# stream
URL: https://ai.pydantic.dev/results/#streamed-results

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

Results are the final values returned from . The result values are wrapped in
and so you can access other data like of the run and

Both and are generic in the data they wrap, so typing information about the data
returned by the agent is preserved.

```

  
  



  
  

  
  'Where were the olympics held in 2012?'

Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65,
details=None)

```

_(This example is complete, it can be run "as is")_

Runs end when either a plain text response is received or the model calls a tool
associated with one of the structured result types. We will add limits to make
sure a run doesn't go on indefinitely, see .

When the result type is , or a union including , plain text responses are
enabled on the model, and the raw text response from the model is used as the
response data.

If the result type is a union with multiple members (after remove from the
members), each member is registered as a separate tool with the model in order
to reduce the complexity of the tool schemas and maximise the chances a model
will respond correctly.

If the result type schema is not of type , the result type is wrapped in a
single element object, so the schema of all tools registered with the model are
object schemas.

Structured results (like tools) use Pydantic to build the JSON schema used for
the tool, and to validate the data returned by the model.

Until "Annotating Type Forms" lands, unions are not valid as s in Python.

When creating the agent we need to the argument, and add a type hint to tell
type checkers about the type of the agent.

Here's an example of returning either text or a structured value

```

  
  
  



  
  
  
  

     
  
    
  
    "Extract me the dimensions of a box, "
    "if you can't extract all data, ask the user to try again."
  

  

#> Please provide the units for the dimensions (e.g., cm, in, m).

  'The box is 10x20x30 cm'

#> width=10 height=20 depth=30 units='cm'

```

_(This example is complete, it can be run "as is")_

Here's an example of using a union return type which registered multiple tools,
and wraps non-object schemas in an object:

```

  
  
     
  
    
  'Extract either colors or sizes from the shapes provided.'

  'red square, blue circle, green triangle'

  'square size 10, circle size 20, triangle size 30'

```

_(This example is complete, it can be run "as is")_

Some validation is inconvenient or impossible to do in Pydantic validators, in
particular when the validation requires IO and is asynchronous. PydanticAI
provides a way to add validation functions via the decorator.

Here's a simplified variant of the :

```

  
    
  
     



  



  

  
    
  
  
  
  'Generate PostgreSQL flavored SQL queries based on user input.'

       
    
     
  
     
     
       
  
     

  
  'get me uses who were last active yesterday.'

#> sql_query='SELECT * FROM users WHERE last_active::date = today() - interval 1
day'

```

_(This example is complete, it can be run "as is")_

There two main challenges with streamed results:

  1. Validating structured responses before they're complete, this is achieved by "partial validation" which was recently added to Pydantic in .
  2. When receiving a response, we don't know if it's the final response without starting to stream it and peeking at the content. PydanticAI streams just enough of the response to sniff out if it's a tool call or a result, then streams the whole thing and calls tools, or returns the stream as a .

Example of streamed text result:

```

  
  

  
    'Where does "hello world" come from?'   
         
      
      
      #> The first known use of "hello,
      #> The first known use of "hello, world" was in
      #> The first known use of "hello, world" was in a 1974 textbook
      #> The first known use of "hello, world" was in a 1974 textbook about the C
      #> The first known use of "hello, world" was in a 1974 textbook about the C programming language.

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

We can also stream text as deltas rather than the entire text in each item:

```

  
  

  
    'Where does "hello world" come from?'  
         
      
      
      
      
      
      
      

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

Result message not included in

The final result message will be added to result messages if you use , see for
more information.

Not all types are supported with partial validation in Pydantic, see , generally
for model-like structures it's currently best to use .

Here's an example of streaming a use profile as it's built:

```

  
  
  

  
  
  
  

  
  
  
  'Extract a user profile from the input'

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

If you want fine-grained control of validation, particularly catching validation
errors, you can use the following pattern:

```

  
  
  
  

  
  
  
  

  

  
    'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
      
          
      
            
          
           
        
       
        
      
      
      
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
      #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add to run )_

The following examples demonstrate how to use streamed responses in PydanticAI:

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_0_annotation_1

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_0_annotation_2

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_0_annotation_3

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_3

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_12

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_13

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_1

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_2

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_9

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_4

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_5

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_6

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_7

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_11

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_8

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_1_annotation_10

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_2_annotation_1

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

# Untitled Page
URL: https://ai.pydantic.dev#__code_2_annotation_2

This documentation is ahead of the last release by . You may see documentation
for features not yet supported in the latest release .

_Agent Framework / shim to use Pydantic with LLMs_

PydanticAI is a Python agent framework designed to make it less painful to build
production grade applications with Generative AI.

PydanticAI is a Python Agent Framework designed to make it less painful to build
production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic
design, built on the foundation of .

Similarly, virtually every agent framework and LLM library in Python uses
Pydantic, yet when we began to use LLMs in , we couldn't find anything that gave
us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI
app development.

**Built by the Pydantic Team** Built by the team behind (the validation layer of
the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers,
CrewAI, Instructor and many more).

Supports OpenAI, Anthropic, Gemini, Ollama, Groq, and Mistral, and there is a
simple interface to implement support for .

Seamlessly with for real-time debugging, performance monitoring, and behavior
tracking of your LLM-powered applications.

Designed to make as powerful and informative as possible for you.

Leverages Python's familiar control flow and agent composition to build your AI-
driven projects, making it easy to apply standard Python best practices you'd
use in any other (non-AI) project.

Harnesses the power of to model outputs, ensuring responses are consistent
across runs.

Offers an optional system to provide data and services to your agent's , and .
This is useful for testing and eval-driven iterative development.

Provides the ability to LLM outputs continuously, with immediate validation,
ensuring rapid and accurate results.

provides a powerful way to define graphs using typing hints, this is useful in
complex applications where standard control flow can degrade to spaghetti code.

PydanticAI is in early beta, the API is still subject to change and there's a
lot more to do. is very welcome!

Here's a minimal example of PydanticAI:

```

  
  
  
  'Be concise, reply with one sentence.'

  'Where does "hello world" come from?'

The first known use of "hello, world" was in a 1974 textbook about the C
programming language.

```

_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and
the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts,
and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

```

  
    
    
  

  
  
    

  
     'Advice returned to the customer'
     "Whether to block the customer's card"
       

  
  
  
  
  
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  



     
     
  



  
     
  
"""Returns the customer's current account balance."""

    
    
    
  



  
     
       
  

  support_advice='Hello John, your current account balance, including pending
transactions, is $123.45.' block_card=False risk=1

     'I just lost my card!' 
  

  support_advice="I'm sorry to hear that, John. We are temporarily blocking your
card to prevent unauthorized transactions." block_card=True risk=8

```

The code included here is incomplete for the sake of brevity (the definition of
is missing); you can find the complete example .

To understand the flow of the above runs, we can watch the agent in action using
Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

That's enough to get the following view of your agent in action:

See to learn more.

To try PydanticAI yourself, follow the instructions .

Read the to learn more about building applications with PydanticAI.

Read the to understand PydanticAI's interface.

---

