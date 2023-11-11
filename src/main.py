from fastapi import FastAPI

from utils import get_form_template
from db_utils import get_db_data

app = FastAPI()


@app.get("/")
def index():
    return "Hello world!"


@app.post("/get_form")
def get_form(form_query: dict):
    return get_form_template(form_query)


@app.get("/db")
def get_db():
    return get_db_data()
