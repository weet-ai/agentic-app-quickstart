from agents import Agent, Runner
import gradio as gr
from agentic_app_quickstart.examples.helpers import get_model
from phoenix.otel import register

tracing_provider = register(
    endpoint="https://app.phoenix.arize.com/s/hello6069/v1/traces",
    project_name="gradio",
    protocol="http/protobuf",
    auto_instrument=True,
)

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
