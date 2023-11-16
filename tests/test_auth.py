import pytest

from tests.conftest import client


@pytest.fixture
def test_user():
    return {
        "username": "test@example.com",
        "password": "password"
    }


def test_register(test_user):
    response = client.post("/auth/jwt/register", json=test_user)
    assert response.status_code == 201


def test_login(test_user):
    response = client.post("/auth/jwt/login", data=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_logout(test_user):
    # First, authenticate the user and get the access token
    login_response = client.post("/auth/jwt/register", data=test_user)
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    # Use the access token to make a request to the logout endpoint
    logout_response = client.post("/auth/jwt/logout", headers={"Authorization": f"Bearer {access_token}"})
    assert logout_response.status_code == 200
    assert logout_response.json() == {"message": "Logged out successfully"}


def test_logout_unauthorized():
    # Try to logout without providing an access token
    response = client.post("/auth/jwt/logout")
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}
