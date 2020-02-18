import pytest
import re

from api_methods import get_geo_info
from db.database_declaration import Info


# @pytest.fixture(params=[
#     (str(Info.query.get(1).geonameid), True),
#     (str(Info.query.get(len(Info.query.all())).geonameid), True),
#     ("12123042", True)
#     # ("-5678764", "Id must be a positive number no less than 1 and no more than 8 digits!"),
#     # ("100000", "Wrong range!\nIt should be no less than 451747 and no more than 12123288"),
#     # ("70000000", "Wrong range!\nIt should be no less than 451747 and no more than 12123288")
# ])
# def geonameid_validation(request):
@pytest.fixture()
def geonameid_validation(request):
    first_geonameid = Info.query.get(1).geonameid
    last_geonameid = Info.query.get(len(Info.query.all())).geonameid

    def params_lst():
        params = [(str(first_geonameid), True),
                  (str(last_geonameid), True),
                  ("12123042", True)]
        return params

    return params_lst()


def test_geonameid_validation(geonameid_validation):
    for tup in geonameid_validation:
        (request, expected_output) = tup
        result = get_geo_info.geonameid_validation(request)
        print("output: {0}, expected: {1}".format(result, expected_output))
        assert result == expected_output


# @pytest.fixture(params=[
#     # (12123043, "Such id does not exist!"),
#     (451747, {'admin1_code': '77',
#               'admin2_code': '',
#               'admin3_code': '',
#               'admin4_code': '',
#               'alternatenames': '',
#               'asciiname': 'Zyabrikovo',
#               'cc2': '',
#               'country_code': 'RU',
#               'dem': 204,
#               'elevation': '',
#               'feature class': 'P',
#               'feature_code': 'PPL',
#               'geonameid': 451747,
#               'latitude': '56.84665',
#               'longitude': '34.7048',
#               'modification_date': '2011-07-09',
#               'name': 'Zyabrikovo',
#               'population': 0,
#               'timezone': 'Europe/Moscow'})
#
# ])
# def get_item_validation(request):
#     return request.param


@pytest.fixture()
def get_item_validation(request):
    first_item = Info.query.get(1).geonameid
    atypical_item =8456277

    def params_lst():
        params = (first_item, atypical_item)
        return params

    return params_lst()




def test_get_item_by_geonameid(get_item_validation):
    for request in get_item_validation:
        result = get_geo_info.get_item_by_geonameid(request)
        assert re.match(r'[0-9]{6,8}$', str(result['geonameid'])) \
               and re.match(r'[-]?[0-9]{1,3}\.*[0-9]{0,5}$', str(result['latitude'])) \
               and re.match(r'[-]?[0-9]{1,3}\.*[0-9]{0,5}$', str(result['longitude'])) \
               and re.match(r'[A-Z\d]{2,5}$', str(result['feature_code'])) \
               and re.match('RU', str(result['country_code'])) \
               and re.match(r'[0-9\w]{2}|^$', str(result['admin1_code'])) \
               and re.match(r'[0-9]*$', str(result['population'])) \
               and re.match(r'[-]?[0-9]*$', str(result['dem'])) \
               and re.match(r'[\w-]*/[\w-]*|^$', str(result['timezone'])) \
               and re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}$', str(result['modification_date']))
        # and re.match(r'[A-Z]{1,4}$',  str(result['feature class']) )\


@pytest.fixture(params=[
    ("451747", ""),
    ("462336", ['Zaderikhi', 'Zadirikhi', 'Знаменка'])
])
def get_alternames_validation(request):
    return request.param


def test_get_alterames(get_alternames_validation):
    (request, expected_output) = get_alternames_validation
    result = get_geo_info.get_alterames(request)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output
