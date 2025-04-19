import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging
from app.routes import nasa, weather, joke, quote, numbers, anime, forex, email_validator

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Snapi - Snap into the world of public APIs!", 
              version="1.0.0", 
              description="A playground for free public APIs: NASA, Quotes, Numbers, Anime and more.",
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the routes
app.include_router(nasa.router, prefix="/api/nasa", tags=["NASA API"])
app.include_router(weather.router, prefix="/api/weather", tags=["Weather API"])
app.include_router(joke.router, prefix="/api/joke", tags=["Joke API"])
app.include_router(quote.router, prefix="/api/quote", tags=["Quote API"])
app.include_router(numbers.router, prefix="/api/numbers", tags=["Numbers Trivia"])
app.include_router(anime.router, prefix="/api/anime", tags=["Anime Quotes"])
app.include_router(forex.router, prefix="/api/forex", tags=["Exchange Rates"])
app.include_router(email_validator.router, prefix="/api/email", tags=["Email Validator"])

# Automatically run the server if this script is executed directly
if __name__ == "__main__":
    uvicorn.run( "app.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=False)
    logger.info("FastAPI server started successfully.")