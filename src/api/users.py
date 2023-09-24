from typing import List

from fastapi import APIRouter, Depends

from src.models import User
from src.database import db
from src.schemas import UserSchema, UserSerializer


router = APIRouter(
    prefix="/users",
)


@router.post("/")
async def create_user(
    user: UserSchema, db_session=Depends(db.get_db)
) -> UserSerializer:
    user = await User.create(db_session, **user.model_dump())
    return user


@router.get("/{id}")
async def get_user(id: str, db_session=Depends(db.get_db)) -> UserSerializer:
    user = await User.get(db_session, id)
    return user


@router.get("/")
async def get_all_users(db_session=Depends(db.get_db)) -> List[UserSerializer]:
    users = await User.get_all(db_session)
    return users


@router.put("/{id}")
async def update(
    id: str, user: UserSchema, db_session=Depends(db.get_db)
) -> UserSerializer:
    user = await User.update(db_session, id, **user.model_dump())
    return user


@router.delete("/{id}")
async def delete_user(id: str, db_session=Depends(db.get_db)) -> bool:
    return await User.delete(db_session, id)
