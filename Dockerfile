FROM python:3.13.6-slim

RUN adduser --disabled-password --gecos '' appuser
WORKDIR /home/appuser

USER appuser

COPY . .
COPY uv.lock .

RUN python -m venv .venv && .venv/bin/pip install -U pip uv
RUN .venv/bin/uv sync --no-cache

ENTRYPOINT [".venv/bin/uv", "run", "python", "agentic_app_quickstart/examples/phoenix/02_gradio.py"]
