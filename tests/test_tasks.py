from app.schemas.task import TaskResponse


def test_create_task(client):
    data = {"id": 0, "title": "Task 1", "description": "Description of Task 1"}
    response = client.post("/task/", json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "Task 1"


def test_read_task(client):
    response = client.get("/task/0")
    assert response.status_code == 200
    assert response.json()["title"] == "Task 1"


def test_update_task(client):
    data = {"id": 0, "title": "Updated Task 1", "description": "Updated description"}
    data = TaskResponse(**data)
    response = client.put("/task/0", data=data.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task 1"


def test_delete_task(client):
    response = client.delete("/task/0")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted successfully"}
