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
    mo.md(r"""<img src="https://github.com/weet-ai/agentic-app-quickstart/blob/main/assets/llm_judge.png?raw=true)" />""")
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Simple LLM as Judge""")
    return


@app.cell
def _():
    from phoenix import Client
    from phoenix.evals import (
        TOXICITY_PROMPT_RAILS_MAP,
        TOXICITY_PROMPT_TEMPLATE,
        OpenAIModel,
        llm_classify,
    )
    import os
    import nest_asyncio

    nest_asyncio.apply()

    def get_data(project_name: str = "01_llm_as_judge_example"):
        client = Client(
            endpoint="https://app.phoenix.arize.com/s/hello6069",  # Replace with real base URL
            api_key=os.getenv("PHOENIX_API_KEY")  # Replace with your Bearer token
        )

        spans_df = client.get_spans_dataframe(
            project_name=project_name,
            limit=100  # or suitable number
        )


        # 2. Convert spans/traces into dataset examples format expected by Phoenix
        dataset_examples = []
        for _, row in spans_df.sample(n=10).iterrows():
            example = {
                "input": row["attributes.input.value"],  # or relevant span input data
                "output": row["attributes.output.value"]
            }
            dataset_examples.append(example)

        return dataset_examples


    def evaluate(eval_df):

        print(f"TEMPLATE: {TOXICITY_PROMPT_TEMPLATE}")
        model = OpenAIModel(
            base_url=os.getenv("OPENAI_API_ENDPOINT"),
            api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-4.1"
        )

        #It will remove text such as ",,," or "..."
        #Will ensure the binary value expected from the template is returned 
        rails = list(TOXICITY_PROMPT_RAILS_MAP.values())
        toxic_classifications = llm_classify(
            data=eval_df,
            template=TOXICITY_PROMPT_TEMPLATE,
            model=model,
            rails=rails,
            provide_explanation=True, #optional to generate explanations for the value produced by the eval LLM
            concurrency=5
        )

        return toxic_classifications


    def run_evaluation():

        df = get_data()
        evaluations = evaluate(eval_df = df)
        return evaluations

    return (run_evaluation,)


@app.cell
def _(run_evaluation):
    result_df = run_evaluation()
    return (result_df,)


@app.cell
def _(result_df):
    result_df.head()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
