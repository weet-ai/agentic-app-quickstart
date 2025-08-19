from openai import AsyncOpenAI
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
import os
from phoenix.otel import register
from dotenv import load_dotenv


load_dotenv()


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_API_ENDPOINT")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is required. "
            "Please create a .env file with your API key. "
            "See .env.example for reference."
        )

    if not base_url:
        print("Warning: OPENAI_API_ENDPOINT not set, using default OpenAI endpoint")

    return AsyncOpenAI(api_key=api_key, base_url=base_url)


def get_model():
    model = OpenAIChatCompletionsModel(
        model="gpt-4.1",
        openai_client=get_client(),
    )

    return model


def get_tracing_provider(project_name: str = "llm_as_judge_example"):

    tracing_provider = register(
        endpoint=os.getenv("PHOENIX_ENDPOINT"),
        project_name=project_name,
        protocol="http/protobuf",
        auto_instrument=True
    )

    return tracing_provider
