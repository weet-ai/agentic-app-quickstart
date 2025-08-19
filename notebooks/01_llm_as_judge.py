import marimo

__generated_with = "0.14.16"
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
    mo.md(r"""### Step 1: Imports""")
    return


@app.cell
def _():
    from agents import Agent, Runner
    from agentic_app_quickstart.examples.helpers import get_model
    from agents import set_tracing_disabled

    set_tracing_disabled(disabled = True)
    return Agent, Runner


@app.cell
def _():
    from agentic_app_quickstart.examples.helpers import get_trace_provider

    trace_provider = get_trace_provider(project_name = "01_llm_as_judge_example")
    return


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
def _(Agent, Runner, mcp_fetch_server):
    async def pipeline(prompt: str):

        async with mcp_fetch_server:

            instructions = """
                "An agent that tries to fetch data based on user's questions.
                Fetch data from https://weather.com/weather/tenday if needed."
            """

            agent = Agent(
                name = "DataFetcherAgent",
                instructions = instructions,
                mcp_servers = [mcp_fetch_server]
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
