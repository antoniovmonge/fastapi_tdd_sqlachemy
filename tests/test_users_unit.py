import json

# CREATE USER TESTS


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


# READ ALL USERS TESTS


def test_read_all_users(test_app_with_db):
    response = test_app_with_db.post(
        "/api/v1/users/", content=json.dumps({"name": "Mr. Test List"})
    )
    assert response.status_code == 201

    response = test_app_with_db.get("/api/v1/users/")
    assert response.status_code == 200

    response_list = response.json()

    assert response_list[-1]["name"] == "Mr. Test List"


# READ SINGLE USER TESTS


def test_read_user(test_app_with_db):
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


def test_read_user_incorrect_id(test_app_with_db):
    response = test_app_with_db.get(
        "/api/v1/users/62e3cb01-347e-4ca8-9c6c-ca47eb673609/"
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


# DELETE USER TESTS


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


def test_remove_user_incorrect_id(test_app_with_db):
    response = test_app_with_db.delete(
        "/api/v1/users/62e3cb01-347e-4ca8-9c6c-ca47eb673609/"
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


# UPDATE USER TESTS


def test_update_user(test_app_with_db):
    response = test_app_with_db.post(
        "/api/v1/users/",
        content=json.dumps({"name": "Mr. Update"}),
    )
    user_id = response.json()["id"]

    response = test_app_with_db.put(
        f"/api/v1/users/{user_id}/",
        content=json.dumps({"name": "Mr. Updated"}),
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Mr. Updated"


def test_update_user_incorrect_id(test_app_with_db):
    response = test_app_with_db.put(
        "/api/v1/users/62e3cb01-347e-4ca8-9c6c-ca47eb673609/",
        content=json.dumps({"name": "Mr. Updated"}),
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_update_user_invalid_json(test_app_with_db):
    response = test_app_with_db.post(
        "/api/v1/users/",
        content=json.dumps({"name": "Mr. Update Invalid"}),
    )
    user_id = response.json()["id"]

    response = test_app_with_db.put(
        f"/api/v1/users/{user_id}/",
        content=json.dumps({}),
    )
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
