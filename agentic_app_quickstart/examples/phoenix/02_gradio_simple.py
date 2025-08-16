from agents import Agent, Runner
import gradio as gr
from agentic_app_quickstart.examples.helpers import get_model, get_tracing_provider


tracing_provider = get_tracing_provider()


agent = Agent(
    name="Assistant", instructions="You are a helpful assistant.", model=get_model()
)

# Define the Gradio chat interface function as async
async def chat_with_agent(message, history):
    # Run the agent asynchronously
    result = await Runner.run(agent, message)
    # Return just the agent's response - ChatInterface handles history automatically
    return result.final_output


# Launch Gradio UI
demo = gr.ChatInterface(
    fn=chat_with_agent,
    title="OpenAI Agent Chatbot",
    description="Ask anything, and let the OpenAI agent help you!",
    theme="default",
)

demo.launch(server_name="0.0.0.0", server_port=8000)
