import os
import phi
import groq
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

#Load env variables from .env file
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

# Creating websearch agent (1st agent)
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the wen for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Alwayes include sources"],
    show_tool_calls = True,
    markdown=True
)

# Creating financial agent (2nd agent)
finance_agent = Agent(
    name = "Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Creating multi ai agent (Combining both AI agents)
multi_ai_agent = Agent(
    name = "Multi AI Agent",
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Alwayes include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

#Building in playground
app=Playground(agents=[multi_ai_agent,finance_agent,web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)
