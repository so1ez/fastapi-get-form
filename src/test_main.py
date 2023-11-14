"""File with test functions for pytest lib"""

from fastapi.testclient import TestClient

from main import app
from models import TemplateTypes, RequestTypes

client = TestClient(app)


def test_get_matching_form():
    """Get a feedback form template with full matching fields"""

    response = client.post("/get_form", json={
        "feedback": "What a wonderful web-service!", 
        "email": "boytsov_work@mail.ru"
    })
    assert response.status_code == 200
    assert response.json() == {
        TemplateTypes.NAME: "feedback template"
    }


def test_get_date_form():
    """Get a simple date template with full field matching"""

    response = client.post("/get_form", json={
        "created_date": "11.11.2011"
    })
    assert response.status_code == 200
    assert response.json() == {
        TemplateTypes.NAME: "simple date template"
    }


def test_get_date_text_form():
    """Get a logs form template with full matching fields"""

    response = client.post("/get_form", json={
        "created_date": "2012-12-12",
        "info": "log text is here"
    })
    assert response.status_code == 200
    assert response.json() == {
        TemplateTypes.NAME: "logs template"
    }


def test_get_empty_body():
    """Make an empty request. Empty response expected"""

    response = client.post("/get_form", json={})
    assert response.status_code == 200
    assert response.json() == {}


def test_get_all_fields():
    """Get the most suitable form template when sending all possible fields"""

    response = client.post("/get_form", json={
        "username": "boytsoff",
        "phone": "8 800 555 35 35",
        "email": "boytsov_work@mail.ru",
        "created_date": "1.1.2011"
    })
    assert response.status_code == 200
    assert response.json() == {
        TemplateTypes.NAME: "register template"
    }


def test_get_typo_form():
    """Request with a typo in field name"""

    response = client.post("/get_form", json={
        "usernamr": "boytsoff"
    })
    assert response.status_code == 200
    assert response.json() == {
        "usernamr": RequestTypes.TEXT
    }


def test_get_non_existent_form():
    """Request with a non-existent set of fields"""

    response = client.post("/get_form", json={
        "phone": "+7 999 999 99 99",
        "username": "boytsoff"
    })
    assert response.status_code == 200
    assert response.json() == {
        "phone": RequestTypes.PHONE,
        "username": RequestTypes.TEXT
    }


def test_request_with_int_value():
    """Request with int value instead of string"""

    response = client.post("/get_form", json={
        "username": 1234
    })
    assert response.status_code == 422


def test_request_with_json_value():
    """Request with json value instead of string"""

    response = client.post("/get_form", json={
        "username": {
            "first_name": "Vladimir",
            "second_name": "Boytsov"
        }
    })
    assert response.status_code == 422
