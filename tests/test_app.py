import pytest
from app import app, create_table


@pytest.fixture
def client(tmp_path, monkeypatch):
    database = tmp_path / "test_students.db"
    monkeypatch.setattr("app.DATABASE", str(database))
    create_table()
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Management" in response.data


def test_add_student_page(client):
    response = client.get("/add")
    assert response.status_code == 200
    assert b"Add a student" in response.data


def test_add_student(client):
    response = client.post("/add", data={
        "name": "Rahul",
        "email": "rahul@example.com",
        "course": "Python",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Rahul" in response.data


def test_delete_student(client):
    client.post("/add", data={
        "name": "Asha",
        "email": "asha@example.com",
        "course": "Flask",
    })
    response = client.get("/")
    assert b"Asha" in response.data
