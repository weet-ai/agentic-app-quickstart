FROM python:3.13.6-slim

# Run without root access
RUN adduser --disabled-password --gecos '' appuser
WORKDIR /home/appuser

USER appuser

COPY agentic_app_quickstart ./agentic_app_quickstart
COPY pyproject.toml .
COPY uv.lock .
COPY README.md .

# Install / update pip & install uv (https://astral.sh/uv)
RUN python -m venv .venv && .venv/bin/pip install -U pip uv

# uv sync installs dependencies from pyproject.toml
RUN .venv/bin/uv sync --no-cache

ENV PYTHONPATH=/home/appuser/agentic_app_quickstart

# What our app will run
ENTRYPOINT [ \
    ".venv/bin/uv", \
    "run", \
    "streamlit", \
    "run", \
    "agentic_app_quickstart/examples/phoenix/03_streamlit.py", \
    "--server.port", \
    "8000" \
]
