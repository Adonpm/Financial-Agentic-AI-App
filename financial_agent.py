import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import groq

from dotenv import load_dotenv
load_dotenv()

# Set the Groq API key
groq.api_key = os.getenv("GROQ_API_KEY")

# Creating websearch agent (1st agent)
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the wen for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Alwayes include sources"],
    show_tool_calls = True,
    markdown=True
)

# Creating financial agent (2nd agent)
finance_agent = Agent(
    name = "Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Creating multi ai agent (Combining both AI agents)
multi_ai_agent = Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Alwayes include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Execting multi ai agent with query given in bracket
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)
