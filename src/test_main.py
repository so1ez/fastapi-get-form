"""file with test functions for pytest"""

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_get_matching_form():
    response = client.post("/get_form", json={
        "feedback": "What a wonderful web-service!", 
        "email": "boytsov_work@mail.ru"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "feedback template"
    }

def test_get_date_form():
    response = client.post("/get_form", json={
        "created_date": "11.11.2011"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "simple date template"
    }

def test_get_date_text_form():
    response = client.post("/get_form", json={
        "created_date": "2012-12-12",
        "info": "log text is here"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "logs template"
    }

def test_get_empty_body():
    response = client.post("/get_form", json={})
    assert response.status_code == 200
    assert response.json() == {}


def test_get_all_fields():
    response = client.post("/get_form", json={
        "username": "boytsoff",
        "phone": "8 800 555 35 35",
        "email": "boytsov_work@mail.ru",
        "created_date": "1.1.2011"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "register template"
    }

def test_get_typo_form():
    response = client.post("/get_form", json={
        "usernamr": "boytsoff"
    })
    assert response.status_code == 200
    assert response.json() == {
        "usernamr": "text"
    }

def test_get_non_existent_form():
    response = client.post("/get_form", json={
        "phone": "+7 999 999 99 99",
        "username": "boytsoff"
    })
    assert response.status_code == 200
    assert response.json() == {
        "phone": "phone",
        "username": "text"
    }
