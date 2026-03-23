from fastapi import FastAPI
from src.api.v1.router import api_router
from src.app import add_cors_middleware

app = FastAPI(
    title="Production Backend",
    version="1.0.0"

)

add_cors_middleware(app)

@app.get("/")
async def root():
    return {"message":"API is running"}

app.include_router(api_router,prefix="/api/v1")

