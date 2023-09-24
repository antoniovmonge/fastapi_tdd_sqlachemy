from fastapi import FastAPI
import logging

from src.config import config
from src.database import db

logger = logging.getLogger(__name__)

def init_app():
    app = FastAPI(
        title="Users App",
        description="Handling Our User",
        version="1",
    )

    @app.on_event("startup")
    def startup():
        db.connect(config.SQLALCHEMY_DATABASE_URL)

    @app.on_event("shutdown")
    async def shutdown():
        await db.disconnect()

    from src.api.router import api_router

    app.include_router(
        api_router,
        prefix="/api/v1",
    )

    return app


app = init_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/ping")
# async def pong():
#     return {
#         "ping": "pong!",
#     }
