from tests.conftest import client


def test_main():
    response = client.get("/")
    assert response.status_code == 404
