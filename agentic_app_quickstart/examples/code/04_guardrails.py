"""
Guardrails Agent Example

This example demonstrates how to implement input guardrails to control what kinds of
requests an agent will process. Guardrails act as safety mechanisms or filters that
check user input before it reaches the main agent.

Key concepts:
- Input Guardrails: Functions that check user input and can block certain requests
- Tripwire: A mechanism that stops processing when certain conditions are met
- Pydantic Models: Used to structure the guardrail's decision output
- Context Wrapper: Provides access to the current conversation context
- Safety & Control: Ensures agents only handle appropriate requests

Use cases:
- Content filtering (block inappropriate content)
- Topic restriction (only allow specific subjects)
- Security checks (prevent malicious inputs)
- Business rules enforcement
- Quality control
"""

import asyncio
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    set_tracing_disabled
)
from agentic_app_quickstart.examples.helpers import get_model
from pydantic import BaseModel

# Disable detailed logging for cleaner output
set_tracing_disabled(True)

# Define the structure for guardrail decisions
# This Pydantic model ensures the guardrail returns consistent, structured output
class MusicQuestionOutput(BaseModel):
    """
    Output structure for the music question guardrail.
    
    This model defines what information the guardrail must provide
    when making its decision about whether to allow or block a request.
    """
    is_music_question: bool  # True if the question is about music, False otherwise
    reasoning: str          # Explanation of why the decision was made

# Create a specialized agent whose job is to act as a guardrail
# This agent will analyze user input and decide if it's music-related
input_guardrail_agent = Agent(
    name="Guardrail Check",
    instructions="A guardrail that ensures that the user is asking questions about Music.",
    model=get_model(),
    output_type=MusicQuestionOutput  # Forces structured output using our Pydantic model
)

# Define the guardrail function
# The @input_guardrail decorator marks this as an input guardrail function
@input_guardrail
async def input_guardrail_music(ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]):
    """
    Input guardrail function that checks if user questions are about music.
    
    This function:
    1. Takes the user's input
    2. Uses the guardrail agent to analyze it
    3. Returns a decision about whether to allow or block the request
    
    Args:
        ctx: The current conversation context
        agent: The main agent (not used in this example)
        input: The user's input to be checked
        
    Returns:
        GuardrailFunctionOutput: Contains the decision and whether to trigger the tripwire
    """
    # Run the guardrail agent to analyze the input
    result = await Runner.run(input_guardrail_agent, input=input, context=ctx)
    
    # Return the guardrail decision
    return GuardrailFunctionOutput(
        output_info=result.final_output,  # The structured decision from our guardrail agent
        tripwire_triggered=(not result.final_output.is_music_question)  # Block if NOT about music
    )

# Create the main agent with the guardrail protection
# This agent will only process inputs that pass the music question guardrail
agent = Agent(
    name="MusicGuruAgent",
    instructions="You are an agent that keeps a conversation with the user around music",
    model=get_model(),
    input_guardrails=[input_guardrail_music]  # Apply the guardrail to all inputs
)

async def main():
    """
    Main function demonstrating guardrail behavior.
    
    Try asking:
    - Music questions: "What's your favorite genre?" ✅ (Will work)
    - Non-music questions: "What's the weather like?" ❌ (Will be blocked)
    
    When a guardrail blocks a request, an InputGuardrailTripwireTriggered
    exception is raised instead of processing the request.
    """
    print("Music Guru Agent with Guardrails")
    print("Try asking music-related questions!")
    print("Non-music questions will be blocked by the guardrail.\n")
    
    while True:
        prompt = input("Your question: ")
        
        # Check if user wants to exit
        if prompt.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
            
        try:
            # Attempt to run the agent
            # The guardrail will check the input first
            result = await Runner.run(starting_agent=agent, input=prompt)
            print(f"\nAgent: {result.final_output}\n")
            
        except InputGuardrailTripwireTriggered as e:
            # This exception is raised when a guardrail blocks the request
            print(f"\n🚫 Guardrail blocked your request!")
            print(f"Details: {str(e)}")
            print("Please ask a music-related question.\n")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
