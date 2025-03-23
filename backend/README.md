# Zoom Transcript Summarizer Backend

This is the backend service for the Zoom Transcript Summarizer application. It provides an API for summarizing meeting transcripts using AI.

## Project Structure

```
backend/
├── app/                    # Application package
│   ├── api/               # API routes and endpoints
│   │   └── errors/       # Error handling
│   │   └── v1/           # Version 1 of the API
│   ├── config/           # Application configuration
│   ├── llm/              # LLM-related functionality
│   ├── services/         # Business logic
├── tests/                # Test files
├── data/                 # Data files
└── logs/                 # Log files
```

## Setup

1. Install dependencies:

```bash
poetry install
```

2. Create a `.secrets.toml` file in `app/config` with your HuggingFace token:

```toml
# .secrets.toml
HUGGINGFACE_TOKEN = "your_token_here"
```

## Running the Application

Development:

```bash
uvicorn app.main:app --reload
```

Production:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Main Features

- Transcript summarization using AI
- File upload handling
- Configurable model settings
- CORS support
- Error handling

## Development

- Code formatting: `black .`
- Type checking: `mypy .`
- Testing: `pytest`
