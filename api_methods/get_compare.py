from db.database_declaration import *
from api_methods.get_geo_info import make_info_dict
from transliterate import translit
import re


def info_comparison(geo_1, geo_2):
    validation = input_validation(geo_1, geo_2)
    if validation is True:
        return make_compare_dict(geo_1, geo_2)
    return validation


def make_compare_dict(geo_1, geo_2):
    geo_1, geo_2 = get_obj_by_name(geo_1), get_obj_by_name(geo_2)
    lt = {'geo_1': make_info_dict(geo_1), 'geo_2': make_info_dict(geo_2),
          'compares': get_comparison(geo_1, geo_2)}
    return lt


def input_validation(geo_1, geo_2):
    if re.match(r'[А-Яа-я0-9\s]*$', geo_1) \
            and re.match(r'[А-Яа-я0-9\s]*$', geo_2) is not None:
        return True
    return "Names can only contain cyrillic letters and numbers!"


def translit_request(geo_1, geo_2):
    geo_1 = translit(geo_1, reversed=True)
    geo_2 = translit(geo_2, reversed=True)
    return geo_1, geo_2


def get_obj_by_name(name):
    ids = find_all_ids(name)
    items = get_items_by_id(ids)
    return chose_item(items)


def chose_item(items):
    if items is not None:
        chosen_item = items[0]
        for item in items:
            if item.population > chosen_item.population:
                chosen_item = item
        return chosen_item
    return None


def get_items_by_id(ids):
    if len(ids) > 0:
        items = []
        for id in ids:
            item = Info.query.filter_by(geonameid=id).first()
            if item is not None:
                items.append(item)
        return items
    return None


def find_all_ids(name):
    ru_ids = get_ids_by_name(name)
    name = translit(name, reversed=True)
    alt_ids = get_ids_by_name(name)
    for id in ru_ids:
        if id not in alt_ids:
            alt_ids.append(id)
    return alt_ids


def get_ids_by_name(name):
    items = NameId.query.filter_by(name=name).all()
    if len(items) > 0:
        ids = []
        for item in items:
            ids.append(item.geonameid)
        return ids
    return []


def get_comparison(geo_1, geo_2):
    if geo_1 is not None and geo_2 is not None:
        northern_item = compare_geo(geo_1, geo_2)
        compare_dct = {'Northern geo': northern_item.name,
                       'Northern latitude': northern_item.latitude,
                       'Timezones_difference': compare_timezone(geo_1, geo_2)}
        return compare_dct
    return None


def compare_geo(geo_1, geo_2):
    if geo_1.latitude > geo_2.latitude:
        return geo_1
    return geo_2


def compare_timezone(geo_1, geo_2):
    if geo_1.timezone == geo_2.timezone:
        return 0
    return timezones_difference(geo_1.timezone, geo_2.timezone)


def timezones_difference(timezone_1, timezone_2):
    time_1 = Timezones.query.filter_by(time_zone=timezone_1).first().offset
    time_2 = Timezones.query.filter_by(time_zone=timezone_2).first().offset
    return time_1 - time_2


