import os

from dotenv import load_dotenv
from pydantic import PostgresDsn, validator
from pydantic_settings import BaseSettings


load_dotenv(".envs/.env_db")

class Settings(BaseSettings):
    db_user: str = os.getenv("DB_USER", "postgres")
    db_password: str = os.getenv("DB_PASSWORD", "postgres")
    db_host: str = os.getenv("DB_HOST", "localhost:5555")
    db_name: str = os.getenv("DB_NAME", "postgres")
    db_dsn: PostgresDsn = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}/{db_name}"
    sql_alchemy_database_url: str = os.getenv("DATABASE_URL")

    @validator("db_dsn", pre=True)
    def assemble_db_dsn(cls, v, values):
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("db_user"),
            password=values.get("db_password"),
            host=values.get("db_host"),
            path=f"/{values.get('db_name') or ''}",
        )


settings = Settings()
