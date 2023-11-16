from app.schemas.task import TaskResponse
from tests.conftest import client


def test_create_task():
    data = {"id": 0, "title": "Task 1", "description": "Description of Task 1"}
    response = client.post("/task/", json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "Task 1"


def test_read_task():
    response = client.get("/task/0")
    assert response.status_code == 200
    assert response.json()["title"] == "Task 1"


def test_update_task():
    data = {"id": 0, "title": "Updated Task 1", "description": "Updated description"}
    data = TaskResponse(**data)
    response = client.put("/task/0", data=data.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task 1"


def test_delete_task():
    response = client.delete("/task/0")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted successfully"}
