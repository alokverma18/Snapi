from fastapi import APIRouter, HTTPException, Query
import httpx
import os

router = APIRouter()

FOREX_API_KEY = os.getenv("FOREX_API_KEY", "DEMO_KEY")
base_url = f"https://v6.exchangerate-api.com/v6/{FOREX_API_KEY}"

@router.get("/latest")
async def get_latest_exchange_rates(base: str = Query("USD", description="Base currency, e.g., USD")):
    url = f"{base_url}/latest/{base.upper()}"
    print(f"Fetching URL: {url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch rates")
        return response.json()

@router.get("/convert")
async def convert_currency(
    from_currency: str = Query("USD"),
    to_currency: str = Query("INR"),
    amount: float = Query(1.0)
):
    url = f"{base_url}/pair/{from_currency.upper()}/{to_currency.upper()}/{amount}"
    print(f"Fetching URL: {url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Conversion failed")
        return response.json()
