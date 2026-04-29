FROM python:3.12-slim

WORKDIR /app

# Install system dependencies and uv
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

# Install Python deps system-wide (no .venv)
ENV UV_SYSTEM_PYTHON=1

# Copy source so editable install + hatch can resolve the package
COPY . .

# Install the project (editable) plus dev tooling into the system Python
RUN uv pip install --no-cache -e . pytest ruff pre-commit

CMD ["python", "-c", "print('Lox interpreter container is ready!')"]
