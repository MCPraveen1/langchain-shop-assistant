# AI Shop Assistant

An AI-powered shopping assistant built using **Groq**, **Tool Calling**, and **Gradio**. The assistant can answer product pricing queries by intelligently deciding when to use a Python tool to retrieve product information.

## Project Overview

This project demonstrates the core concepts of **AI Agents**:

* Tool Calling
* Function Execution
* Agent Reasoning
* LLM Integration
* Interactive Web Interface

Unlike a traditional chatbot that only generates text, this assistant can access external tools (Python functions) to retrieve product prices and provide accurate responses.

## Features

* Ask product pricing questions in natural language
* AI Agent decides when to call a tool
* Retrieves real product prices from a Python dictionary
* Performs simple calculations when multiple products are requested
* Interactive Gradio-based web interface
* Powered by Groq's Llama 3.3 70B model

## Technologies Used

* Python
* Groq API
* Llama 3.3 70B Versatile
* Gradio
* Python Dotenv

## Project Structure

```text
AI_Shop_Assistant/
│
├── agent.py
├── app.py
├── README.md
├── requirements.txt
└── screenshot.png
```

## How It Works

```text
User Question
      ↓
AI Agent
      ↓
Tool Decision
      ↓
get_price()
      ↓
Price Retrieved
      ↓
Final Response
```

Example:

**User:**

```
How much are the shoes and hat?
```

**Agent:**

```
Shoes cost ₹799
Hat costs ₹399
Total cost = ₹1198
```

## Application Screenshot

![AI Shop Assistant](screenshot.png)

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI_Shop_Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:7860
```

## Learning Outcomes

Through this project I learned:

* Building AI Agents
* Tool Calling Concepts
* Function Execution via LLMs
* LangChain Fundamentals
* Groq API Integration
* Gradio Application Development

## Future Improvements

* Product inventory management
* Multiple tools support
* Shopping cart functionality
* Product recommendation engine
* Database integration

---

Built as part of my AI Engineering learning journey.
