"""
Agent Handoffs Example

This example demonstrates how to implement agent handoffs, where one agent can transfer
a conversation to another specialized agent based on the user's needs. This creates
a multi-agent system where different agents handle different types of requests.

Key concepts:
- Agent Handoffs: Transferring conversation control from one agent to another
- Specialized Agents: Different agents with specific expertise areas
- Handoff Functions: Functions that determine when and how to transfer control
- Multi-agent Workflow: Coordinating multiple agents to handle complex scenarios

Use cases:
- Customer support (general → technical → billing agents)
- E-commerce (product info → order management → support agents)
- Educational platforms (general tutor → subject specialist → assessment agent)
- Healthcare (intake → specialist → follow-up agents)
"""

import asyncio
from agents import Agent, Runner, set_tracing_disabled, function_tool
from agentic_app_quickstart.examples.helpers import get_model

# Disable detailed logging for cleaner output
set_tracing_disabled(True)

# Create specialized agents for different domains

# 1. General Reception Agent - First point of contact
reception_agent = Agent(
    name="ReceptionAgent",
    instructions="""You are a reception agent that helps users with their initial requests.
    You should:
    - Greet users warmly
    - Understand what they need help with
    - Transfer them to the appropriate specialist if needed
    - Handle simple general questions yourself
    
    Available specialists:
    - Technical Support: For technical issues, bugs, troubleshooting
    - Sales: For product information, pricing, purchase questions
    - Billing: For payment issues, invoices, account questions
    
    If a user needs specialized help, use the appropriate handoff function.
    At the start of the conversation, mention which type of agent you are.""",
    model=get_model()
)

# 2. Technical Support Agent - Handles technical issues
tech_support_agent = Agent(
    name="TechnicalSupportAgent",
    instructions="""You are a technical support specialist.
    You help users with:
    - Technical problems and troubleshooting
    - Bug reports and error messages
    - Software configuration and setup
    - Performance optimization
    
    Be thorough, ask detailed questions, and provide step-by-step solutions.
    If the issue is not technical, transfer back to reception.
    At the start of the conversation, mention which type of agent you are.
    """,
    model=get_model()
)

# 3. Sales Agent - Handles product and sales inquiries
sales_agent = Agent(
    name="SalesAgent",
    instructions="""You are a sales specialist.
    You help users with:
    - Product information and features
    - Pricing and package comparisons
    - Purchase recommendations
    - Demo scheduling
    
    Be enthusiastic, informative, and help users make the best choice.
    If the question is not sales-related, transfer back to reception.
    At the start of the conversation, mention which type of agent you are.""",
    model=get_model()
)

# 4. Billing Agent - Handles payment and account issues
billing_agent = Agent(
    name="BillingAgent", 
    instructions="""You are a billing specialist.
    You help users with:
    - Payment issues and failed transactions
    - Invoice questions and billing history
    - Account upgrades and downgrades
    - Refund requests and disputes
    
    Be helpful and professional with financial matters.
    If the question is not billing-related, transfer back to reception.
    At the start of the conversation, mention which type of agent you are.""",
    model=get_model()
)


# Add handoff tools to agents
reception_agent.handoffs = [tech_support_agent, sales_agent, billing_agent]
tech_support_agent.handoffs = [reception_agent]
sales_agent.handoffs = [reception_agent]
billing_agent.handoffs = [reception_agent]

# Agent registry for easy lookup
agents = {
    "reception": reception_agent,
    "tech_support": tech_support_agent,
    "sales": sales_agent,
    "billing": billing_agent
}

async def run_conversation_with_handoffs():
    """
    Main conversation loop that handles agent handoffs.
    
    This function:
    1. Starts with the reception agent
    2. Processes user input
    3. Checks if agent wants to handoff to another agent
    4. Switches agents as needed
    5. Continues the conversation with the new agent
    """
    print("🏢 Welcome to our Multi-Agent Customer Service!")
    print("Our reception agent will help you get started.")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    current_agent_name = "reception"  # Start with reception
    current_agent = agents[current_agent_name]
    
    while True:
        # Show which agent is currently active
        
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Thank you for contacting us. Goodbye! 👋")
            break
        
        try:
            # Run the current agent
            result = await Runner.run(starting_agent=current_agent, input=user_input)
            response = result.final_output
            
            # Display the agent's response
            print(f"Agent: {response}\n")
            
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")
            print("Please try again.\n")

async def main():
    """
    Main function that demonstrates the handoff system.
    
    Try asking questions like:
    - "I'm having trouble logging in" (should transfer to tech support)
    - "What's the price of your premium plan?" (should transfer to sales)  
    - "I was charged twice this month" (should transfer to billing)
    - "Hello, I need some general help" (stays with reception)
    """
    await run_conversation_with_handoffs()

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
