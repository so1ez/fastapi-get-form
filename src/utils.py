"""data process functions"""

import re

from settings import SETTINGS
from db_utils import query_get_form


def get_form_template(raw_data: dict) -> dict | None:
    """process data and call a query function"""

    data = _validate_string(raw_data)
    result = query_get_form(data)

    return result if result else data

def _validate_string(data: dict) -> dict:
    """updates value based on string type"""

    for key, value in data.items():
        upd = {}
        if re.match(SETTINGS.date_pattern, value):
            upd = {key: "date"}
        elif re.match(SETTINGS.phone_pattern, value):
            upd = {key: "phone"}
        elif re.match(SETTINGS.email_pattern, value):
            upd = {key: "email"}
        else:
            upd = {key: "text"}

        data.update(upd)

    return data
