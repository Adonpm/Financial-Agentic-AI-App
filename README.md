# Multi-Agent AI System for Financial Analysis
This project demonstrates the use of AI agents for web searching and financial data analysis using the `phi` library. The application is designed to run in a playground environment where multiple AI agents can be utilized for different tasks.

## Project Structure
- **playground.py**: This script sets up a web application using the `Playground` class, which hosts two individual AI agents (web search and financial analysis) and a combined multi-agent system.
- **financial_agent.py**: This script demonstrates the creation of a multi-agent system that combines the capabilities of both the web search and financial analysis agents.

## Prerequisites
- Python 3.x
- `phi` library
- `groq` library
- `dotenv` library

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
4. Create a .env file in the root directory and add your API keys:
   PHI_API_KEY=your_phi_api_key
   GROQ_API_KEY=your_groq_api_key

## Usage
### Running the Playground Application
- Navigate to the project directory.
- Run the playground.py script to start the web application:
  ```bash
  python playground.py
- This will launch a web server hosting the playground application with the web search agent, financial analysis agent, and the combined multi-agent system.

### Running the Financial Agent Script
- Navigate to the project directory.
- Run the financial_agent.py script to execute the multi-agent system:
  ```bash
  python financial_agent.py
- This will execute the multi-agent system, combining the web search and financial analysis capabilities, and print the response to a sample query.

## Features
- Web Search Agent: Searches the web for information using the DuckDuckGo tool.
- Finance AI Agent: Analyzes financial data using the YFinanceTools, providing stock prices, analyst recommendations, stock fundamentals, and company news.
- Multi-Agent System: Combines the capabilities of both agents to provide comprehensive responses to complex queries.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.
