from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
from datetime import datetime, timezone
import uvicorn 

app = FastAPI()

@app.get("/me")
async def get_profile():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("https://catfact.ninja/fact")
            response.raise_for_status()
            cat_fact = response.json().get("fact", "No fact available at the moment.")
    except Exception:
        cat_fact = "Could not fetch cat fact right now. Please try again later."


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


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
