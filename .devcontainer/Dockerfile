FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    software-properties-common \
    zsh \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user
RUN groupadd --gid 1000 vscode \
    && useradd --uid 1000 --gid vscode --shell /bin/zsh --create-home vscode

# Install uv as root, then make it accessible to vscode user
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN mv /root/.cargo/bin/uv /usr/local/bin/uv

# Set up Oh My Zsh for vscode user
USER vscode
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Set environment variables for vscode user
RUN echo 'export UV_LINK_MODE=copy' >> /home/vscode/.zshrc && \
    echo 'export OPENAI_AGENTS_DISABLE_TRACING=1' >> /home/vscode/.zshrc

# Set default user and working directory
USER vscode
WORKDIR /workspace
