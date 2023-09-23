from typing import List

# from fastapi import APIRouter, Depends
from pydantic import BaseModel

# from models import User
# from app.database import db


class UserSchema(BaseModel):
    full_name: str


class UserSerializer(BaseModel):
    id: str
    full_name: str

    class Config:
        from_attributes = True
