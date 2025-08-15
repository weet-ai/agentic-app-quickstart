FROM python:3.13.6-slim

WORKDIR /app

RUN adduser --disabled-password --gecos '' appuser
USER appuser

COPY . .
COPY ../pyproject.toml ./
COPY ../uv.lock ./

RUN python -m venv .venv && .venv/bin/pip install -U pip uv
RUN .venv/bin/uv sync --no-cache

ENV PYTHONPATH=/app/.venv/bin

ENTRYPOINT ["python", "examples/phoenix/02_gradio.py"]
