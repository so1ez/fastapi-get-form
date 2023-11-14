"""Database queries functions"""

from itertools import combinations
import json
from typing import List, Dict

from bson import json_util

from database import collection
from models import TemplateTypes


def query_get_form(query: Dict[str, str]) -> Dict[str, str] | None:
    """
        Queries the db to find the name of the form template.
        Returns the result if found, None if not.
    """

    combination_len = len(query)

    result = None
    while result is None and combination_len > 0:
        combs = combinations(query, combination_len)
        for comb in combs:
            q = {key: query[key] for key in comb}
            bson_results = collection.find(q)
            tmp_results = json.loads(json_util.dumps(bson_results))

            for tmp_result in tmp_results:
                tmp_result.pop("_id")
                if tmp_result and len(tmp_result) - 1 <= combination_len:
                    result = {TemplateTypes.NAME: tmp_result[TemplateTypes.NAME]}

        combination_len -= 1

    return result


def get_db_data() -> List[Dict[str, str]]:
    """Query to get all documents from working collection. Returns list if dicts"""
    return json.loads(json_util.dumps(collection.find()))
