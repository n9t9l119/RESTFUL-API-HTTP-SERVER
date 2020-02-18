from transliterate import translit
import re
from flask import Response, jsonify
from typing import Union, Dict, Any, Tuple, List

from db.database_declaration import *
from api_methods.get_geo_info import make_info_dict


def info_comparison(geo_1: str, geo_2: str) -> Response:
    validation = input_validation(geo_1, geo_2)
    if validation == True:
        return jsonify(make_compare_dict(geo_1, geo_2))
    return validation


def make_compare_dict(geo_1: str, geo_2: str) -> Dict[str, Any]:
    geo_1, geo_2 = get_obj_by_name(geo_1), get_obj_by_name(geo_2)
    lt = {'geo_1': make_info_dict(geo_1), 'geo_2': make_info_dict(geo_2),
          'compares': get_comparison(geo_1, geo_2)}
    return lt


def input_validation(geo_1: str, geo_2: str) -> Union[bool, Response]:
    if re.match(r'[А-Яа-я0-9\s]*$', geo_1) \
            and re.match(r'[А-Яа-я0-9\s]*$', geo_2) is not None:
        return True
    return Response("Names can only contain cyrillic letters and numbers!", status=400, mimetype='text/plain')


def translit_request(geo_1: str, geo_2: str) -> Tuple[str, str]:
    geo_1 = translit(geo_1, reversed=True)
    geo_2 = translit(geo_2, reversed=True)
    return geo_1, geo_2


def get_obj_by_name(name: str) -> Info:
    ids = find_all_ids(name)
    items = get_items_by_ids(ids)
    return chose_item(items)


def chose_item(items: List[Info]) -> Union[Info, None]:
    if items:
        chosen_item = items[0]
        for item in items:
            if item.population > chosen_item.population:
                chosen_item = item
        return chosen_item
    return None


def get_items_by_ids(ids: List[int]) -> List[Info]:
    if ids:
        items = []
        for id in ids:
            item = Info.query.filter_by(geonameid=id).first()
            if item is not None:
                items.append(item)
        return items
    return []


def find_all_ids(name: str) -> List[int]:
    ru_ids = get_ids_by_name(name)
    name = translit(name, reversed=True)
    alt_ids = get_ids_by_name(name)
    for id in ru_ids:
        if id not in alt_ids:
            alt_ids.append(id)
    return alt_ids


def get_ids_by_name(name: str) -> List[int]:
    items = NameId.query.filter_by(name=name).all()
    if items:
        ids = []
        for item in items:
            ids.append(item.geonameid)
        return ids
    return []


def get_comparison(geo_1: Info, geo_2: Info) -> Union[Dict[str, Any], None]:
    if geo_1 is not None and geo_2 is not None:
        northern_item = compare_geo(geo_1, geo_2)
        compare_dct = {'Northern geo': northern_item.name,
                       'Northern latitude': northern_item.latitude,
                       'Timezones_difference': compare_timezone(geo_1, geo_2)}
        return compare_dct
    return None


def compare_geo(geo_1: Info, geo_2: Info) -> Info:
    if geo_1.latitude > geo_2.latitude:
        return geo_1
    return geo_2


def compare_timezone(geo_1: Info, geo_2: Info) -> float:
    if geo_1.timezone == geo_2.timezone:
        return 0.0
    return timezones_difference(geo_1.timezone, geo_2.timezone)


def timezones_difference(timezone_1: str, timezone_2: str) -> Union[str, float]:
    time_1 = get_timezone(timezone_1)
    time_2 = get_timezone(timezone_2)
    if time_1 == "Timezone is not defined!" or time_2 == "Timezone is not defined!":
        return "Undefinded"
    return time_1 - time_2


def get_timezone(timezone: str) -> Union[str, Timezones]:
    if timezone == "":
        return "Timezone is not defined!"
    else:
        return Timezones.query.filter_by(time_zone=timezone).first().offset



