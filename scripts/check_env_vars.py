import os
from rich.console import Console

console = Console()


def check_env_vars():
    api_key = os.getenv("OPENAI_API_KEY", "")
    base_url = os.getenv("OPENAI_API_ENDPOINT", "")

    if not api_key.startswith("prx_live_"):
        console.print(
            "[bold red]Warning:[/bold red] OPENAI_API_KEY must be set to 'prx_live_<YOUR_API_KEY>'."
        )
        console.print(
            "[bold red]Don't forget to set it up before running the examples 😃"
        )
    else:
        console.print(
            "[bold green]Success:[/bold green] OPENAI_API_KEY is set correctly."
        )
    if not base_url or base_url != "https://api.hexflow.ai":
        console.print(
            "[bold red]Warning:[/bold red] OPENAI_API_ENDPOINT must be set to 'https://api.hexflow.ai'."
        )
        console.print(
            "[bold red]Don't forget to set it up before running the examples 😃"
        )
    else:
        console.print(
            "[bold green]Success:[/bold green] OPENAI_API_ENDPOINT is set correctly."
        )


if __name__ == "__main__":
    check_env_vars()
