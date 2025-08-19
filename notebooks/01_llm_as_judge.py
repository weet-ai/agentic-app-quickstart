import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""## LLM as Judge Example""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    <img src="https://drive.google.com/file/d/1okL1QWYgrKwz1SjfwRNkoohtD9W3YCuu/view?usp=drive_link" />

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Step 1: Imports""")
    return


@app.cell
def _():
    from agents import Agent, Runner
    from agentic_app_quickstart.examples.helpers import get_model, get_tracing_provider
    from dotenv import load_dotenv

    load_dotenv()
    return Agent, Runner, get_model, get_tracing_provider


@app.cell
def _(get_tracing_provider):
    from opentelemetry import trace
    from opentelemetry.trace import NoOpTracerProvider, ProxyTracerProvider

    def activate_tracing():
        current_provider = trace.get_tracer_provider()

        if isinstance(current_provider, NoOpTracerProvider) or isinstance(current_provider, ProxyTracerProvider):
            print("Tracing is NOT enabled with Phoenix.")
            current_provider = get_tracing_provider(project_name = "01_llm_as_judge_example")
        else:
            print("Tracing is enabled.")
            print(f"Trace provider: {current_provider}")
    return (activate_tracing,)


@app.cell
def _():
    from agents.mcp import MCPServerStdio, MCPServerStdioParams

    mcp_fetch_server = MCPServerStdio(
        params = MCPServerStdioParams(
            command = "uvx",
            args = ["mcp-server-fetch"]
        ),
        cache_tools_list = True,
        client_session_timeout_seconds=30
    )
    return (mcp_fetch_server,)


@app.cell
def _(Agent, Runner, activate_tracing, get_model, mcp_fetch_server):
    async def pipeline(prompt: str):

        async with mcp_fetch_server:

            activate_tracing()

            instructions = """
                "An agent that tries to fetch data based on user's questions.
                Fetch data from https://www.meteoblue.com if needed."
            """

            agent = Agent(
                name = "DataFetcherAgent",
                instructions = instructions,
                mcp_servers = [mcp_fetch_server],
                model=get_model()
            )

            result = await Runner.run(starting_agent=agent, input = prompt)
            return result.final_output
    return (pipeline,)


@app.cell
async def _(pipeline):
    user_input = "What's the weather forecast for Amsterdam, NL?"
    result = await pipeline(prompt = user_input)
    print(result)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
