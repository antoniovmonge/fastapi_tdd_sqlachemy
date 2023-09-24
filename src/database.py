import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from src.config import config

Base = declarative_base()

class Database:
    def __init__(self):
        self.__session = None
        self.__engine = None

    def connect(self, db_config):
        self.__engine = create_async_engine(
            config.SQLALCHEMY_DATABASE_URL,
        )

        self.__session = async_sessionmaker(
            bind=self.__engine,
            autocommit=False,
        )

    async def disconnect(self):
        await self.__engine.dispose()

    async def get_db(self):
        async with db.__session() as session:
            yield session


db = Database()
