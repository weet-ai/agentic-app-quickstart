from phoenix import Client
from phoenix.evals import HallucinationEvaluator
from phoenix.evals import (
    TOXICITY_PROMPT_RAILS_MAP,
    TOXICITY_PROMPT_TEMPLATE,
    OpenAIModel,
    llm_classify,
)
import os

from dotenv import load_dotenv

load_dotenv()

def get_data(project_name: str = "agentic_app_quickstart"):
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
    for _, row in spans_df.iterrows():
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
    )

    return toxic_classifications


def main():

    df = get_data()
    evaluations = evaluate(eval_df = df)
    print(evaluations)

if __name__ == "__main__":

    main()
