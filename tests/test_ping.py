from src import main


def test_ping(test_app):
    response = test_app.get("/api/v1/users/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
