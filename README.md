## Mastering AI Agents and MCP: Build Enterprise Agentic Apps
# Agentic App Quickstart

This repo contains code examples, templates and assignments for the [Mastering AI Agents and MCP: Build Enterprise Agentic Apps](https://maven.com/rafael-pierre/building-agentic-ai-apps-with-mcp) [Maven](https://www.maven.com) course.

## 🚀 Quick Start

### Use this template

This repo is a Github Template. You can quickly use it by creating on the "Use Template" button on top right. You can then create a clone of this repo in your own organization or profile. If you're not familiar with Templates, this is a nice guide: [link](https://dev.to/jajera/how-to-create-and-use-a-github-repository-template-2g7l)

### Option 1: GitHub Codespaces (Recommended)

1. Click the "Code" button on this repository
2. Select "Codespaces" tab
3. Click "Create codespace on main"
4. Wait for the environment to set up automatically

Need more details? Check out this [link](https://docs.github.com/en/enterprise-cloud@latest/codespaces/developing-in-a-codespace/creating-a-codespace-from-a-template).

### Option 2: Local Development Container

**Prerequisites:**
- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**Steps:**
1. Clone this repository
2. Open in VS Code
3. When prompted, click "Reopen in Container" or use the command palette (`Cmd+Shift+P`) and select "Dev Containers: Reopen in Container"
4. Wait for the container to build and set up

### Option 3: Other IDEs

You are free to use PyCharm, Cursor, Windsurf, Zed, etc. Flow is mostly similar to running VSCode locally.

## 🛠️ What's Included

The development environment comes pre-configured with:

- **Python 3.13**
- **[uv](https://github.com/astral-sh/uv)** - Modern, fast Python package manager
- **[openai-agents](https://openai.github.io/openai-agents-python/)** - Core library for agentic applications
- **[marimo](https://marimo.io/)** - Modern, interactive development notebooks
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern web framework for APIs
- **Development tools** - ruff, pytest

## GPT API Keys

Make sure that the following is part of your `.env` file at the root of this folder:

```
# OpenAI API Configuration
OPENAI_API_ENDPOINT="https://api.hexflow.ai"
OPENAI_API_KEY="your_openai_api_key_here"
OPENAI_AGENTS_DISABLE_TRACING=1
```

ℹ️ If you're experiencing connection issues (e.g. SSL Handshake Issues)
1. Try using mobile data instead of WiFi
2. Use this alternative URL: https://hexflow-g9bqfbexhmfyazat.z03.azurefd.net

🔴 **IMPORTANT**: `.env` is already included in `.gitignore`, so it won't be pushed to your Github Repo. Don't remove it from there and don't store these credentials elsewhere, otherwise the will be publicly available!

## OpenAI Agents SDK Setup & Troubleshooting

### Configuring models

An OpenAI model is already configured for you in the `examples/helpers.py` module.

If you prefer to include model configuration in your custom modules, you can simply copy this excerpt:

```python

from openai import AsyncOpenAI
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
import os
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
```

### Errors

If you get errors like this one when running the examples:

```bash
Error code: 401 - {'error': {'message': 'Incorrect API key provided: your_ope************here. You can find your API key at https://platform.openai.com/account/api-keys.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}}
```

This indicates that [tracing](https://openai.github.io/openai-agents-python/tracing/) is probably enabled. Make sure that the following line is part of your `.env` file:

```
OPENAI_AGENTS_DISABLE_TRACING=1
```

## Troubleshooting & Support

- Questions? Bugs? Please reach out in the #help Slack Channel for this course!
