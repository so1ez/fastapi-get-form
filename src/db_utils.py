"""database query functions"""

from itertools import combinations
import json

from bson import json_util

from database import collection


def query_get_form(query: dict):
    """execute query to database"""

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
                    result = {"name": tmp_result["name"]}

        combination_len -= 1

    return result

def get_db_data():
    return json.loads(json_util.dumps(collection.find({})))
