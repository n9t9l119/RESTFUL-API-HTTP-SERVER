import re
from flask import abort, Response, jsonify
from typing import Union, Dict, Any, Tuple, List

from db.database_declaration import Info, NameId


def info(geonameid: str) -> Response:
    validation = geonameid_validation(geonameid)
    if validation is True:
        return jsonify(get_item_by_geonameid(geonameid))
    return validation


def geonameid_validation(geonameid: str) -> Union[bool, Response]:
    if re.match(r'[0-9]{6,8}$', geonameid) is not None:
        if 451747 <= int(geonameid) <= 12123288:
            return True
        return Response("Wrong range!\nIt should be no less than 451747 and no more than 12123288", status=404)
    return Response("Id must be a positive number no less than 1 and no more than 8 digits!", status=400)


def get_item_by_geonameid(geonameid: str) -> Dict[str, Any]:
    item = Info.query.filter_by(geonameid=geonameid).first()
    if item is None:
        abort(404)
    return make_info_dict(item)


def make_info_dict(item: Info) -> Union[None, Dict[str, Any]]:
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


def get_alterames(geonameid: str) -> Union[str, List[str]]:
    alternames = NameId.query.filter_by(geonameid=geonameid)
    names = create_alternames_lst(geonameid, alternames)
    if not names:
        return ""
    return names


def create_alternames_lst(geonameid: str, alternames: List[NameId]) -> List[str]:
    names = []
    for name in alternames:
        names.append(name.name)
    names.remove(Info.query.filter_by(geonameid=geonameid).first().name)
    return names
