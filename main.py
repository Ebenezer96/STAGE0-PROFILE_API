from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
from datetime import datetime, timezone

app = FastAPI()

@app.get("/me")
async def get_profile():
    # Try to fetch a cat fact
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("https://catfact.ninja/fact")
            response.raise_for_status()
            cat_fact = response.json().get("fact", "No fact available at the moment.")
    except Exception as e:
        cat_fact = "Could not fetch cat fact right now. Please try again later."

    # Build response
    data = {
        "status": "success",
        "user": {
            "email": "ebenezeramakato96@gmail.com",
            "name": "Ebenezer Amakato",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JSONResponse(content=data)
