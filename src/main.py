"""File with main endpoints routers and app creating"""

__author__      = "Boytsov V.M."

from typing import List, Dict

from fastapi import FastAPI, Body, HTTPException, status

from utils import get_form_template
from db_utils import get_db_data
from exceptions import InvalidDataFormatException

app = FastAPI(
    title="GetFormApp",
    summary="App for defining a form template"
)


@app.post("/get_form")
def get_form(form_query: str = Body(...)) -> Dict[str, str]:
    """
        Returns the name of the found template or typed fields if the template is not found.
        If recieved data have invalid format, raise 
    """

    try:
        return get_form_template(form_query)
    except InvalidDataFormatException as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message) from exc


@app.get("/db")
def get_db() -> List[dict]:
    """Returns all documents in the working collection of a database (list of dicts)"""

    return get_db_data()
