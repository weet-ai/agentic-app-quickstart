"""
Hello World Agent Example

This is the simplest example of using the openai-agents package.
It demonstrates how to create an AI agent that can respond to user requests
by translating "Hello World" into different languages.

Key concepts:
- Agent: An AI assistant with specific instructions and capabilities
- Runner: The execution engine that handles the conversation flow
- Model: The underlying AI model (like GPT-4) that powers the agent
"""

import asyncio
from agents import Agent, Runner, set_tracing_disabled
from agentic_app_quickstart.examples.helpers import get_model

# Disable tracing, since it will try to push data to OpenAI
set_tracing_disabled()

# Create an AI agent with specific instructions
# The agent is like a specialized AI assistant with a defined role
agent = Agent(
    name="HelloWorldAgent",  # A descriptive name for the agent
    instructions="You are an agent that says hello world in the language the user asks for",  # The agent's role and behavior
    model=get_model(),  # The AI model that powers the agent (e.g., GPT-4)
)

async def main():
    """
    Main function that runs the agent conversation.
    
    The Runner.run() method:
    - Takes a starting agent and user input
    - Handles the conversation flow between user and agent
    - Returns the agent's final response
    """
    # Run the agent with user input asking for a language
    input_language = input("Choose a language: ")
    result = await Runner.run(starting_agent=agent, input=input_language)

    # Print the agent's final response
    print(result.final_output)


if __name__ == "__main__":
    # Use asyncio to run the async main function
    # This is required because the openai-agents package uses async/await
    asyncio.run(main())
