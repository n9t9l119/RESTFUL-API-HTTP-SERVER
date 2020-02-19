import re
from flask import Response, jsonify
from typing import Union, List, Dict, Any

from api_methods.get_geo_info import make_info_dict
from db.database_declaration import Info


def page(page_number: int, items_value: int) -> Response:
    validation = input_validation(page_number, items_value)
    if validation is True:
        start_id = items_value * page_number + 1
        return jsonify(make_items_lst(items_value, start_id))
    return validation


def input_validation(page_number: int, items_value: int) -> Union[bool, Response]:
    if re.match(r'[0-9]{1,6}$', str(page_number)) \
            and re.match(r'[0-9]{1,6}$', str(items_value)) is not None:
        return numerical_range_validation(page_number, items_value)
    return Response("'Page' and 'Items_value' must be a positiv number no less than 1 and no more than 6 digits!",
                    status=400, mimetype='text/plain')


def numerical_range_validation(page_number: int, items_value: int) -> Union[bool, Response]:
    max_value = len(Info.query.all())
    if items_value > max_value:
        return Response("There is not so many values in database!", status=404, mimetype='text/plain')
    if (page_number + 1) * items_value > max_value or items_value == 0:
        return Response("That page is empty!", status=400, mimetype='text/plain')
    return True


def make_items_lst(items_value: int, start_id: int) -> List[Dict[str, Any]]:
    items = []
    for value in range(items_value):
        items.append(make_info_dict(Info.query.get(start_id + value)))
    return items
