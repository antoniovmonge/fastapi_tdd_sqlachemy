import os

import pytest
from starlette.testclient import TestClient

from src import main
from src.config import get_settings, Settings
from src.config import config


def get_settings_override():
    # return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))
    return Settings(testing=1, database_url=os.environ.get("DATABASE_URL"))



@pytest.fixture(scope="module")
def test_app():
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down
