import pytest
import re

from api_methods import get_geo_info
from db.database_declaration import Info
from tests.test_txt_validation import test_ru_txt_validation


def test_get_item_by_geonameid(get_item_validation):
    for request in get_item_validation:
        result = get_geo_info.get_item_by_geonameid(request)
        match_dict(result)


def match_dict(dct):
    for count, key in enumerate(dct):
        if test_ru_txt_validation.Patterns.lst[count] != '':
            assert re.match(test_ru_txt_validation.Patterns.lst[count], str(dct[key]))


@pytest.fixture()
def geonameid_validation():
    first_geonameid = Info.query.get(1).geonameid
    last_geonameid = Info.query.get(len(Info.query.all())).geonameid

    def params_list():
        params = [(str(first_geonameid), True),
                  (str(last_geonameid), True),
                  ("12123042", True)]
        return params

    return params_list()


def test_geonameid_validation(geonameid_validation):
    for tup in geonameid_validation:
        (request, expected_output) = tup
        result = get_geo_info.geonameid_validation(request)
        assert result == expected_output


@pytest.fixture()
def get_item_validation():
    first_item = Info.query.get(1).geonameid
    atypical_item = 8456277

    def params_list():
        params = (first_item, atypical_item)
        return params

    return params_list()


@pytest.mark.parametrize("input, expected_output", [("451747", ""), ("462336", ['Zaderikhi', 'Zadirikhi', 'Знаменка'])])
def test_get_alterames(input, expected_output):
    result = get_geo_info.get_alterames(input)
    assert result == expected_output
