import pytest
import re

from api_methods import get_compare
from db.database_declaration import Info


@pytest.fixture()
def comparison_validation():
    id_1 = 462339
    id_2 = 462340

    item_1 = Info.query.filter_by(geonameid=id_1).first()
    item_2 = Info.query.filter_by(geonameid=id_2).first()

    def params_lst():
        params = [([None, item_2]), ([item_1, item_2])]
        return params

    return params_lst()


def test_get_comparison(comparison_validation):
    for tup in comparison_validation:
        (geo_1, geo_2) = tup
        result = get_compare.get_comparison(geo_1, geo_2)
        assert result is None or re.match(r'[-]?[0-9]{1,2}\.*[0-9]{0,2}$|0|"Undefinded"',
                                          str(result['Timezones_difference'])) and \
               re.match(r'[-]?[0-9]{1,3}\.*[0-9]{0,5}$', str(result['Northern latitude'])) and \
               result['Northern geo'] != "" and result['Northern geo'] is not None


def test_chose_item():
    max_population_id = 1
    result = get_compare.chose_item(Info.query.all())
    assert result.id == max_population_id


@pytest.mark.parametrize("input, expected_output", [("Знаменка", [462335, 462336, 462337, 462338, 462339, 462340]),
                                                    ("Отсутствующее название", [])])
def test_find_all_ids(input, expected_output):
    result = get_compare.find_all_ids(input)
    assert result == expected_output


@pytest.fixture()
def items_by_ids_validation():
    id_1 = 462335
    id_2 = 462336

    item_1 = Info.query.filter_by(geonameid=id_1).first()
    item_2 = Info.query.filter_by(geonameid=id_2).first()

    def params_lst():
        params = [([id_1, id_2], [item_1, item_2]),
                  ([], [])]
        return params

    return params_lst()


def test_get_items_by_id(items_by_ids_validation):
    for tup in items_by_ids_validation:
        (request, expected_output) = tup
        result = get_compare.get_items_by_id(request)
        assert result == expected_output
