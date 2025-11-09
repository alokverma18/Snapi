# LEARN.md - What You Can Learn from Snapi

## Overview
Snapi is a FastAPI microservice that integrates several public APIs. It's a basic example of building a REST API with external services.

## Technologies Used
- **FastAPI**: For creating the API with auto-generated docs.
- **httpx**: For making async HTTP requests to external APIs.
- **python-dotenv**: For loading environment variables.
- **uvicorn**: To run the server.

## Concepts Covered
- Modular routing with APIRouter.
- CORS middleware for cross-origin requests.
- Basic error handling with HTTPException.
- Logging with Python's logging module.
- Environment variable management for API keys.

## What You'll Learn
- Setting up a simple FastAPI app.
- Fetching data from public APIs asynchronously.
- Handling API responses and errors.
- Organizing code into routes.

## Getting Started
1. Install deps: `pip install -r requirements.txt`
2. Add API keys to .env (e.g., WEATHER_API_KEY, NASA_API_KEY)
3. Run: `python app/main.py`
4. Check docs at http://localhost:8000/docs
