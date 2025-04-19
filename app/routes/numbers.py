from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/{number}")
async def get_number_trivia(number: int):
    url = f"http://numbersapi.com/{number}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch trivia")
        return {"trivia": response.text}
