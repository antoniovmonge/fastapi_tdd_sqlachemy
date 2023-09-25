from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import expression as sql

from src.models.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name}, "
            f")>"
        )

    @classmethod
    async def create(cls, db, **kwargs) -> "User":
        query = (
            sql.insert(cls)
            .values(id=str(uuid4()), **kwargs)
            .returning(cls.id, cls.name)
        )
        users = await db.execute(query)
        await db.commit()
        return users.first()

    @classmethod
    async def update(cls, db, id, **kwargs) -> "User":
        query = (
            sql.update(cls)
            .where(cls.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
            .returning(cls.id, cls.name)
        )
        users = await db.execute(query)
        await db.commit()
        return users.first()

    @classmethod
    async def get(cls, db, id) -> "User":
        query = sql.select(cls).where(cls.id == id)
        users = await db.execute(query)
        (user,) = users.first()
        return user

    @classmethod
    async def get_all(cls, db) -> list["User"]:
        query = sql.select(cls)
        users = await db.execute(query)
        users = users.scalars().all()
        return users

    @classmethod
    async def delete(cls, db, id) -> bool:
        query = (
            sql.delete(cls)
            .where(cls.id == id)
            .returning(
                cls.id,
                cls.name,
            )
        )
        await db.execute(query)
        await db.commit()
        return True
