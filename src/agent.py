from langchain.llms import OpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
import os

# Initialize LLM
llm = OpenAI(temperature=0, api_key=os.getenv("OPENAI_API_KEY"))

# Define tools (import your functions here)
tools = []  # Populate with your tool functions

# Create agent
agent = AgentExecutor.from_agent_and_tools(
    agent=create_react_agent(llm, tools), tools=tools, memory=ConversationBufferMemory()
)
