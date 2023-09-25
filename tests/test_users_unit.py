import json

import pytest


def test_create_user(test_app_with_db):
    response = test_app_with_db.post(
        "/api/v1/users/", content=json.dumps({"full_name": "Mr.Test"})
    )

    assert response.status_code == 201
    # assert response.json()["url"] == "/users/1"


def test_create_user_invalid_json(test_app_with_db):
    response = test_app_with_db.post("/api/v1/users/", content=json.dumps({}))

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "full_name"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.3/v/missing",
            }
        ]
    }
