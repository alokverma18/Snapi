from fastapi import APIRouter, HTTPException
import httpx
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Logging setup
logger = logging.getLogger(__name__)

# Get OpenWeather API Key
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "your-api-key-here")

router = APIRouter()

@router.get("")
async def get_weather(city: str):
    """Fetch current weather information for a city."""
    logger.info(f"Fetching weather data for city: {city}")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            logger.error(f"Failed to fetch weather: {response.status_code}")
            raise HTTPException(status_code=response.status_code, detail="Weather API Error")
        
        logger.info(f"Successfully fetched weather data for {city}")
        return response.json()
