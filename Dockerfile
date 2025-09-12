FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

RUN poetry self add poetry-plugin-export

COPY pyproject.toml poetry.lock ./

RUN poetry run poetry export -f requirements.txt --without-hashes -o requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
