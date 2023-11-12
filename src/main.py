"""File with main endpoints routers and app creating"""

__author__      = "Boytsov V.M."

from typing import List

from fastapi import FastAPI, Body

from utils import get_form_template
from db_utils import get_db_data

app = FastAPI(
    title="GetFormApp",
    summary="App for defining a form template"
)


@app.post("/get_form")
def get_form(form_query: dict = Body(...)) -> dict:
    """Returns the name of the found template or typed fields if the template is not found"""

    return get_form_template(form_query)


@app.get("/db")
def get_db() -> List[dict]:
    """Returns all documents in the working collection of a database (list of dicts)"""

    return get_db_data()
