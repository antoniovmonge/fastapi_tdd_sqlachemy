from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/ping")
async def pong():
    return {
        "ping": "pong!"
    }
