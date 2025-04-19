from fastapi import APIRouter, HTTPException
import httpx
import os
import logging

from dotenv import load_dotenv

load_dotenv()  # Load your .env file

logger = logging.getLogger(__name__)
router = APIRouter()

API_NINJAS_KEY = os.getenv("API_NINJAS_KEY")

@router.get("/random")
async def get_random_quote(category: str = None):
    """Fetch a random quote, optionally filtered by category"""
    if not API_NINJAS_KEY:
        raise HTTPException(status_code=500, detail="API Key not configured")

    url = "https://api.api-ninjas.com/v1/quotes"
    headers = {"X-Api-Key": API_NINJAS_KEY}
    params = {"category": category} if category else {}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Quote API Error")

        quote_data = response.json()[0]
        return {
            "quote": quote_data.get("quote"),
            "author": quote_data.get("author"),
            "category": quote_data.get("category")
        }
