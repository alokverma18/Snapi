from fastapi import APIRouter, HTTPException
import httpx
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Logging setup
logger = logging.getLogger(__name__)

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
router = APIRouter()

@router.get("/apod")
async def get_apod():
    """Fetch Astronomy Picture of the Day"""
    logger.info("Fetching Astronomy Picture of the Day from NASA API.")
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            logger.error(f"Failed to fetch APOD: {response.status_code}")
            raise HTTPException(status_code=response.status_code, detail="NASA API Error")
        
        logger.info("Successfully fetched APOD data.")
        return response.json()
