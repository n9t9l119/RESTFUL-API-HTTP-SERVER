import re
from flask import abort, jsonify, Response
from typing import List

from db.database_declaration import NameId


def hint(request: str) -> Response:
    if request_validation(request):
        return jsonify(make_hint_list(request))


def request_validation(request: str) -> bool:
    if re.match(r'[\wА-Яа-я\d]', request) is None:
        abort(400)
    return True


def make_hint_list(request: str) -> List[str]:
    hint_list = []
    all_names = NameId.query.all()
    for item in all_names:
        if re.match(request, item.name) is not None:
            if item.name not in hint_list:
                hint_list.append(item.name)
    return hint_list
