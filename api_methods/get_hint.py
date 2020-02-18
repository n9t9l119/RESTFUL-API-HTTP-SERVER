import re
from flask import abort, jsonify
from db.database_declaration import NameId


def hint(request):
    # validation = request_validation(request)
    if request_validation(request):
        # hint_list = make_hint_list(request)
        return jsonify(make_hint_list(request))
        # if not hint_list:
        #     return "There is no hints"
        # else:
        #     return hint_list
    # else:
    #     return validation


def request_validation(request):
    if re.match(r'[A-ZА-Я\d]', request) is None:
        abort(400)
    return True
    # else:
    #     return "Incorrect request!"


def make_hint_list(request):
    hint_list = []
    all_names = NameId.query.all()
    for item in all_names:
        if re.match(request, item.name) is not None:
            if item.name not in hint_list:
                hint_list.append(item.name)
    return hint_list


