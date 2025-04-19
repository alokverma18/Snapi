from fastapi import APIRouter, HTTPException
import httpx
import logging

# Logging setup
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/random_joke")
async def get_random_joke():
    """Fetch a random joke."""
    logger.info("Fetching a random joke")
    url = "https://official-joke-api.appspot.com/random_joke"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            logger.error(f"Failed to fetch joke: {response.status_code}")
            raise HTTPException(status_code=response.status_code, detail="Joke API Error")
        
        logger.info("Successfully fetched joke")
        return response.json()
