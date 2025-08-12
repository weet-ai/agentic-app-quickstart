#!/bin/bash
# This script is run after the container is created and before the user connects to it.
export OPENAI_AGENTS_DISABLE_TRACING=1 && \
uv run python scripts/check_env_vars.py && \
cp .env.example .env && \
rm -rf .env.example
