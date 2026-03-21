from fastapi import FastAPI
from src.api.v1.router import api_router

app = FastAPI(
    title="Production Backend",
    version="1.0.0"

)

@app.get("/")
async def root():
    return {"message":"API is running"}

app.include_router(api_router,prefix="/api/v1")