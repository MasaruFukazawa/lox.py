FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY . .

# Install Python dependencies using uv if pyproject.toml exists
RUN if [ -f "pyproject.toml" ]; then uv sync; fi

# Default command
CMD ["python", "-c", "print('Lox interpreter container is ready!')"]
