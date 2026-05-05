FROM python:3.12-slim

WORKDIR /app

# Install system dependencies and uv
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

# Put the project venv outside /app so the bind mount does not shadow it
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install deps first (cached unless pyproject.toml / uv.lock change)
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --all-groups --no-install-project

# Then install the project itself (editable)
COPY src ./src
RUN uv sync --frozen --all-groups

CMD ["python", "-c", "print('Lox interpreter container is ready!')"]
