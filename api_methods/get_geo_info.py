import re
from flask import abort, Response, jsonify

from db.database_declaration import Info, NameId


def info(geonameid):
    validation = geonameid_validation(geonameid)
    if validation is True:
        return jsonify(get_item_by_geonameid(geonameid))
    return validation


def geonameid_validation(geonameid):
    if re.match(r'[0-9]{6,8}$', geonameid) is not None:
        if 451747 <= int(geonameid) <= 12123288:
            return True
        return Response("Wrong range!\nIt should be no less than 451747 and no more than 12123288", status=404)
    return Response("Id must be a positive number no less than 1 and no more than 8 digits!", status=400)


def get_item_by_geonameid(geonameid):
    item = Info.query.filter_by(geonameid=geonameid).first()
    if item is None:
        # return "Such id does not exist!"
        abort(404)
    else:
        return make_info_dict(item)


def make_info_dict(item):
    if item is None:
         return None
    info_in_dict = {'geonameid': item.geonameid, 'name': item.name, 'asciiname': item.asciiname,
                    'alternatenames': get_alterames(item.geonameid), 'latitude': item.latitude,
                    'longitude': item.longitude,
                    'feature class': item.feature_class, 'feature_code': item.feature_code,
                    'country_code': item.country_code, 'cc2': item.cc2, 'admin1_code': item.admin1_code,
                    'admin2_code': item.admin2_code, 'admin3_code': item.admin3_code,
                    'admin4_code': item.admin4_code, 'population': item.population, 'elevation': item.elevation,
                    'dem': item.dem, 'timezone': item.timezone, 'modification_date': item.modification_date}
    return info_in_dict


def get_alterames(geonameid):
    alternames = NameId.query.filter_by(geonameid=geonameid)
    names = create_alternames_lst(geonameid, alternames)
    if not names:
        return ""
    return names


def create_alternames_lst(geonameid, alternames):
    names = []
    for name in alternames:
        names.append(name.name)
    names.remove(Info.query.filter_by(geonameid=geonameid).first().name)
    return names
