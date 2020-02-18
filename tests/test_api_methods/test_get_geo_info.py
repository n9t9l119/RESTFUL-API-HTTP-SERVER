import pytest
import re

from api_methods import get_geo_info
from db.database_declaration import Info


@pytest.fixture()
def geonameid_validation():
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
        assert result == expected_output


@pytest.fixture()
def get_item_validation():
    first_item = Info.query.get(1).geonameid
    atypical_item = 8456277

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
               and re.match(r'[A-Z]{1,4}$', str(result['feature class'])) \
               and re.match('RU', str(result['country_code'])) \
               and re.match(r'[0-9\w]{2}|^$', str(result['admin1_code'])) \
               and re.match(r'[0-9]*$', str(result['population'])) \
               and re.match(r'[-]?[0-9]*$', str(result['dem'])) \
               and re.match(r'[\w-]*/[\w-]*|^$', str(result['timezone'])) \
               and re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}$', str(result['modification_date']))


@pytest.mark.parametrize("input, expected_output", [("451747", ""), ("462336", ['Zaderikhi', 'Zadirikhi', 'Знаменка'])])
def test_get_alterames(input, expected_output):
    result = get_geo_info.get_alterames(input)
    assert result == expected_output
