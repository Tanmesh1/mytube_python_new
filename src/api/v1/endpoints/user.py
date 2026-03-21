from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from src.api.deps import get_db


router = APIRouter()

# @router.get("/test-db")
# async def test_db(db: AsyncSession = Depends(get_db)):
#     try:
#     result = await db.execute(text("SELECT 1"))
#     return {"db_status": result.scalar()}

@router.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"db_status": result.scalar()}
    except Exception as e:
        return{
            "status": "failed",
            "error" : str(e)
        }