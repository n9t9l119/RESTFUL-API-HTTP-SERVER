import re
from random import randint
from db.database_declaration import NameId



def hint(request):
    validation = request_validation(request)
    if validation is True:
        hint_list = make_hint_list(request)
        if not hint_list:
            return "There is no hints"
        else:
            return hint_list
    else:
        return validation


def request_validation(request):
    if re.match(r'[A-ZА-Я\d]', request) is not None:
        return True
    else:
        return "Incorrect request!"


def make_hint_list(request):
    hint_list = []
    all_names = NameId.query.all()
    for item in all_names:
        if re.match(request, item.name) is not None:
            if item.name not in hint_list:
                hint_list.append(item.name)
    return hint_list

