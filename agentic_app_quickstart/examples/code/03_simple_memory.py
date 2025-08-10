"""
Simple Memory Agent Example

This example demonstrates how to give agents memory by using sessions.
With memory, agents can remember previous parts of the conversation and maintain context.

Key concepts:
- Session: A storage mechanism that preserves conversation history
- SQLiteSession: A session implementation using SQLite database for storage
- Persistent conversations: The agent remembers what was said before
- Session ID: A unique identifier to separate different conversations

Without memory: Each interaction is independent, agent forgets previous messages
With memory: Agent remembers the entire conversation history and can reference it

Use cases:
- Multi-turn conversations
- Personal assistants that remember user preferences
- Customer support bots that track conversation context
- Educational tutors that build on previous lessons
"""

from agents import Agent, Runner, SQLiteSession, set_tracing_disabled
import asyncio
from agentic_app_quickstart.examples.helpers import get_model

# Disable detailed logging for cleaner output
set_tracing_disabled(True)

# Create a session to store conversation memory
# SQLiteSession stores the conversation history in a SQLite database
# - If no db_path is specified, it uses an in-memory database (lost when program ends)
# - To persist conversations, specify a path: SQLiteSession(db_path="conversations.db")
# - session_id helps separate different conversations (useful for multiple users)
session = SQLiteSession(session_id=123)

# Create an agent designed for ongoing conversations
agent = Agent(
    name="HelloWorldAgent",
    instructions="You are an agent that keeps a nice conversation with the user",
    model=get_model()  # The underlying AI model
)

async def main():
    """
    Main function that runs a continuous conversation loop.
    
    The agent will:
    1. Remember everything from previous messages in this session
    2. Use that context to provide more relevant responses
    3. Build rapport and continuity across multiple interactions
    
    Try asking follow-up questions or referencing something you said earlier
    to see the memory in action!
    """
    print("Starting conversation with memory-enabled agent...")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        # Get user input
        prompt = input("You: ")
        
        # Check if user wants to exit
        if prompt.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        # Run the agent with the session (memory) included
        # The session parameter is what enables memory - without it, 
        # each interaction would be independent
        result = await Runner.run(
            starting_agent=agent, 
            input=prompt, 
            session=session  # This is the key to enabling memory!
        )
        
        # Print the agent's response
        print(f"\nAgent: {result.final_output}\n")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
