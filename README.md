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

Configure the following environment variables in `.env`:

```
# OpenAI API Configuration
OPENAI_API_ENDPOINT="https://api.hexflow.ai"
OPENAI_API_KEY="your_openai_api_key_here"
```

ℹ️ If you're experiencing connection issues (e.g. SSL Handshake Issues)
1. Try using mobile data instead of WiFi
2. Use this alternative URL: https://hexflow-g9bqfbexhmfyazat.z03.azurefd.net

🔴 **IMPORTANT**: `.env` is already included in `.gitignore`, so it won't be pushed to your Github Repo. Don't remove it from there and don't store these credentials elsewhere, otherwise the will be publicly available!

## 📦 Package Management

This template uses [uv](https://github.com/astral-sh/uv) for fast and reliable Python package management:

```bash
# Install dependencies
pip install -U pip uv
uv sync

# Add new packages
uv add package-name
uv venv

# Run commands with uv run
uv run python examples/code/01...
```

## 🔧 Customization

You can customize the development environment by editing:
- `.devcontainer/devcontainer.json` - Container configuration

## 🔒 Security Features

This project includes several security measures to prevent accidental exposure of API keys:

### Pre-commit Hooks
- **API Key Detection**: Automatically checks `.env.example` files for real API keys before commits
- **Code Quality**: Runs `ruff` for linting and formatting
- **General Security**: Detects private keys, large files, and other security issues

### Manual Security Check
You can manually check your `.env.example` file anytime:
```bash
uv run python scripts/check_env_example.py .env.example
```

### CI/CD Security
- GitHub Actions automatically run security checks on all PRs
- Prevents merging code with potential API key leaks

**Remember**: Always use placeholder values in `.env.example` and keep real API keys in `.env` (which is gitignored)!


## Troubleshooting & Support

- Questions? Bugs? Please reach out in the #help Slack Channel for this course!
