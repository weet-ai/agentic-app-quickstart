"""
Function Calling Agent Example

This example demonstrates how agents can use custom functions (tools) to extend their capabilities.
The agent can access real-time information like the current date and time by calling Python functions.

Key concepts:
- Function Tools: Python functions that agents can call to perform specific tasks
- @function_tool decorator: Marks a function as available for the agent to use
- Tools parameter: List of functions provided to the agent during creation

Use cases:
- Accessing real-time data (weather, time, stock prices)
- Performing calculations
- Interacting with APIs or databases
- File operations
"""

import asyncio
from agents import Agent, Runner, set_tracing_disabled, function_tool
from agentic_app_quickstart.examples.helpers import get_model
import datetime

# Disable detailed logging for cleaner output
set_tracing_disabled(True)

# Function tools definitions
# These are Python functions that the agent can call when needed

@function_tool
def function_get_date_time():
    """
    A tool function that returns the current date and time.
    
    The @function_tool decorator makes this function available to the agent.
    When the agent needs current time information, it can call this function
    automatically as part of its response generation.
    
    Returns:
        str: Current date and time in ISO format
    """
    return datetime.datetime.now().isoformat()

# Create an agent with access to the date/time function
agent = Agent(
    name="HelloWorldAgent",
    instructions="You are an agent that says hello world in the language the user asks for, and tells the current date and time.",
    model=get_model(),  # The underlying AI model
    tools=[function_get_date_time]  # List of tools/functions the agent can use
)

async def main():
    """
    Main function that demonstrates function calling.
    
    The agent will:
    1. Receive the user's language choice
    2. Say "Hello World" in that language
    3. Automatically call the function_get_date_time() function to get current time
    4. Include the current date/time in its response
    """
    # Get user input for which language to use
    language = input("Choose a language: ")
    
    # Run the agent - it will automatically use the function tool when needed
    result = await Runner.run(starting_agent=agent, input=language)
    
    # Print the agent's response (will include both greeting and current time)
    print(result.final_output)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
