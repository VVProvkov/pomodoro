from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/db")
async def ping_db():
    return {"message": "ok"}

@router.get("/app")
async def create_task():
    return {"text": "app is working"}