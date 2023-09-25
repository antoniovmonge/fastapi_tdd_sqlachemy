import os
from typing import Any, AsyncGenerator

from fastapi import FastAPI
import pytest
from starlette.testclient import TestClient

from src import main
# from src.config import get_settings, Settings
# from src.config import Config

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# config = Config()

# def get_settings_override():
#     # return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))
#     return config



@pytest.fixture(scope="module")
def test_app():
    # set up
    # main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down

@pytest.fixture(scope="module")
def test_app_with_db() -> FastAPI:
    """
    Fixture for creating FastAPI app.

    :return: fastapi app with mocked dependencies.
    """
    app = main.app
    # application.dependency_overrides[get_db_session] = lambda: dbsession
    # return application  # noqa: WPS331
    with TestClient(app) as test_client:

        # testing
        yield test_client
