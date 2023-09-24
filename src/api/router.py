from fastapi.routing import APIRouter

from src.api import users, ping

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(ping.router, prefix="/ping", tags=["ping"])
