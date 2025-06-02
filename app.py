import os
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
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
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Alwayes include sources"],
    show_tool_calls=False,
    markdown=True
)

# Creating financial agent (2nd agent)
finance_agent = Agent(
    name = "Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=False,
    markdown=True
)

# Creating multi ai agent (Combining both AI agents)
multi_ai_agent = Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Alwayes include sources","Use tables to display the data"],
    show_tool_calls=False,
    markdown=True
)

# Initialising FastAPI
app = FastAPI()

# Setting up Jinja2 templates for rendering HTML
templates = Jinja2Templates(directory="templates")

# Setting up static files for CSS and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

class QueryRequest(BaseModel):
    query: str

# Home page
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Query route
@app.post("/query")
async def run_query(query: QueryRequest):
    response = multi_ai_agent.run(query.query)
    response = response.content if hasattr(response, "content") else str(response)
    return {"response": response}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
