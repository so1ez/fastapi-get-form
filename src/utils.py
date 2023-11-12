"""Data process functions"""

import re

from db_utils import query_get_form
from models import RequestTypes

class RegEx:
    """Class with regex for typing strings"""

    date_pattern: str = (
        r"^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$"
        r"|^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$"
    )
    phone_pattern: str = \
        r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$"
    email_pattern: str = \
        r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,3}$"


def get_form_template(raw_data: dict) -> dict:
    """Process recieved data (dict). Returns name of found template or None if not found"""

    typed_data = _typing_dict(raw_data)
    template_name = query_get_form(typed_data)

    return template_name if template_name is not None else typed_data


def _typing_dict(data: dict) -> dict:
    """Types the values of the received data (dict). Returns updated dict"""

    for key, value in data.items():
        if re.match(RegEx.date_pattern, value):
            data[key] = RequestTypes.DATE
        elif re.match(RegEx.phone_pattern, value):
            data[key] = RequestTypes.PHONE
        elif re.match(RegEx.email_pattern, value):
            data[key] = RequestTypes.EMAIL
        else:
            data[key] = RequestTypes.TEXT

    return data
