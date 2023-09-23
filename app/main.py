from fastapi import FastAPI
import logging

from app.config import config
from app.database import db

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

    from app.api import router_users

    app.include_router(
        router_users,
        prefix="/api/v1",
    )

    return app


app = init_app()
