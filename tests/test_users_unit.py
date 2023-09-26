import json


def test_create_user(test_app_with_db):
    response = test_app_with_db.post(
        "/api/v1/users/", content=json.dumps({"name": "Mr.Test"})
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
                "loc": ["body", "name"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.3/v/missing",
            }
        ]
    }


def test_get_user(test_app_with_db):
    # create a user for this test and store it in the response variable
    response = test_app_with_db.post(
        "/api/v1/users/",
        content=json.dumps({"name": "Blas"}),
    )

    # get the user_id from the response
    user_id = response.json()["id"]

    response = test_app_with_db.get(f"/api/v1/users/{user_id}/")
    assert response.status_code == 200

    response_dict = response.json()

    assert response_dict["id"] == user_id
    assert response_dict["name"] == "Blas"


def test_get_user_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/api/v1/users/62e3cb01-347e-4ca8-9c6c-ca47eb673609/")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_remove_user(test_app_with_db):
    response = test_app_with_db.post(
        "/api/v1/users/",
        content=json.dumps({"name": "Mr. Delete"}),
    )
    user_id = response.json()["id"]

    response = test_app_with_db.delete(f"/api/v1/users/{user_id}/")
    assert response.status_code == 200
    assert response.json() == {
        "message": f"User id: {user_id:.5}... deleted successfully"
    }
