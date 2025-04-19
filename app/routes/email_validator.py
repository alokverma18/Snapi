from fastapi import APIRouter, HTTPException, Query
import httpx
import os

router = APIRouter()

ABSTRACT_API_KEY = os.getenv("ABSTRACT_API_KEY", "YOUR_API_KEY_HERE")
ABSTRACT_API_URL = "https://emailvalidation.abstractapi.com/v1/"

@router.get("/validate-email")
async def validate_email(email: str = Query(..., description="Email address to validate")):
    url = f"{ABSTRACT_API_URL}?api_key={ABSTRACT_API_KEY}&email={email}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to validate email")
        
        data = response.json()
        
        return {
            "email": data.get("email"),
            "is_valid_format": data.get("is_valid_format", {}).get("value"),
            "is_mx_found": data.get("is_mx_found"),
            "is_smtp_valid": data.get("is_smtp_valid"),
            "is_disposable": data.get("is_disposable_email"),
            "is_role_email": data.get("is_role_email"),
            "suggestion": data.get("autocorrect")
        }
