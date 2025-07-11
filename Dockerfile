FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies and uv
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install uv

# Copy project files
COPY . .

# Install Python dependencies using uv if pyproject.toml exists
RUN if [ -f "pyproject.toml" ]; then uv sync; fi

# Default command
CMD ["python", "-c", "print('Lox interpreter container is ready!')"]
