"""Data process functions"""

import re
from typing import Dict
from operator import methodcaller

from db_utils import query_get_form
from models import RequestTypes
from exceptions import InvalidDataFormatException

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


def get_form_template(raw_data: str) -> Dict[str, str]:
    """
        Process recieved data (str).
        Returns {} if recieved data is empty.
        Returns name of found template or None if not found
    """

    if not raw_data:
        return {}

    dict_data = _str_to_dict(raw_data)
    typed_data = _typing_dict(dict_data)
    template_name = query_get_form(typed_data)

    return template_name or typed_data


def _str_to_dict(raw_str: str) -> Dict[str, str]:
    """
        Converts a string to a dictionary
        "f_name1=value1&f_name2=value2" to {f_name1: value1, f_name2: value2}
    """

    pairs_list = raw_str.split("&")
    try:
        dict_data = dict(map(methodcaller("split", "="), pairs_list))
    except ValueError as exc:
        raise InvalidDataFormatException from exc

    return dict_data


def _typing_dict(data: Dict[str, str]) -> Dict[str, str]:
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
