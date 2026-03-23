from fastapi import FastAPI
from src.api.v1.router import api_router
from src.app import add_cors_middleware
from fastapi.staticfiles import StaticFiles
from core.GlobalErrorHandler import register_exception_handlers

app = FastAPI(
    title="Production Backend",
    version="1.0.0"

)

register_exception_handlers(app)

app.mount("/static", StaticFiles(directory="public"), name="static")

add_cors_middleware(app)

@app.get("/")
async def root():
    return {"message":"API is running"}

app.include_router(api_router,prefix="/api/v1")

