import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""## Hello World!""")
    return


@app.cell
def _():
    from agents import Agent, Runner, set_tracing_disabled
    from agentic_app_quickstart.examples.helpers import get_model
    import marimo as mo

    set_tracing_disabled(True)
    return Agent, Runner, get_model, mo


@app.cell
def _(Agent, get_model):
    agent = Agent(
        name = "My hello world agent",
        model=get_model()
    )
    return (agent,)


@app.cell
async def _(Runner, agent):
    result = await Runner.run(starting_agent = agent, input = "hello")
    return (result,)


@app.cell
def _(result):
    result.final_output
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
