from pydantic import BaseModel
from agents import Agent

SEARCHES = 3

INSTRUCTIONS = f"You are a helpful research assistant. Given a query, come up with a set of web searches \
to provide the best answer to the query. Provide only {SEARCHES} outputs"

# Structured Output
class WebSearchItem(BaseModel):
    reason: str
    """Your reasoning for why this search is important to the query."""
    query: str
    """The search term to use for the web search"""

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """A list of web searchs to provide the best answer to the query"""
    
planner_agent = Agent(
    name="Planner Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan
)