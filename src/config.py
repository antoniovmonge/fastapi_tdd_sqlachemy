import os

from dotenv import load_dotenv

load_dotenv(".envs/.env_db")


class Settings:
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost:5555")
    DB_NAME = os.getenv("DB_NAME", "postgres")
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings
