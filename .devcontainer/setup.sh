#!/bin/bash

# Update package manager and install essential tools
apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install uv (modern Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$PATH"

# Add uv to PATH for all sessions
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> /home/vscode/.bashrc
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> /home/vscode/.zshrc
echo 'UV_LINK_MODE=copy' >> /home/vscode/.bashrc
echo 'UV_LINK_MODE=copy' >> /home/vscode/.zshrc
echo 'OPENAI_AGENTS_DISABLE_TRACING=1' >> /home/vscode/.bashrc
echo 'OPENAI_AGENTS_DISABLE_TRACING=1' >> /home/vscode/.zshrc

# Create a virtual environment using uv
uv venv /workspace/.venv && cd /workspace && uv sync

# Make the virtual environment activation automatic
echo 'source /workspace/.venv/bin/activate' >> /home/vscode/.bashrc
echo 'source /workspace/.venv/bin/activate' >> /home/vscode/.zshrc

# Set proper ownership
chown -R vscode:vscode /home/vscode
chown -R vscode:vscode /workspace

echo "✅ Development environment setup complete!"
echo "🚀 Ready to start developing agentic applications!"
