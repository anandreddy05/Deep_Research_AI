from agents import Agent, ModelSettings, function_tool
from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()
@function_tool
def web_search(query: str) -> str:
    """Search DuckDuckGo and return the concise text results."""
    return search_tool.run(query)

INSTRUCTIONS = "You are a research assistant. given a search term, you search the web for that term and \
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 \
words. Capture the main points. Write succintly, no need to have complete sentences or good \
grammar. This will be consumed by someone synthesizing a report, so it's cital you capture the \
essence and ignore any fluff. Do not include any additional commentary other than the summary itself.\
Provide the output in a nice Markdown format"

search_agent = Agent(
    name = "Search agent",
    instructions=INSTRUCTIONS,
    tools = [web_search],
    model='gpt-4o-mini',
    model_settings=ModelSettings(tool_choice='required') # Mandotary to use tools provided
)