from fastapi import FastAPI
import logging

from src.config import settings
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
        db.connect(settings.sql_alchemy_database_url)

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
