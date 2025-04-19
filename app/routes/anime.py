from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/random")
async def get_random_anime_quote():
    url = "https://api.animechan.io/v1/quotes/random"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch anime quote")
        return response.json()
