import pytest
import re

from api_methods import get_compare
from db.database_declaration import Info


# @pytest.fixture(params=[
#     (None, Info.query.filter_by(geonameid=462339).first(), None),
#     (Info.query.filter_by(geonameid=462339).first(), Info.query.filter_by(geonameid=462340).first(),
#      {'Northern geo': 'Znamenka',
#       'Northern latitude': '54.41729',
#       'Timezones_difference': 2.0})
# ])
# def comparison_validation(request):
#     return request.param

@pytest.fixture()
def comparison_validation(request):
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


# @pytest.fixture(params=[
#     ("Знаменка", [462335, 462336, 462337, 462338, 462339, 462340]),
#     ("Отсутствующее название", [])
# ])
# def ids_by_name_validation(request):
#     return request.param

@pytest.mark.parametrize("input, expected_output", [("Знаменка", [462335, 462336, 462337, 462338, 462339, 462340]),
                                                    ("Отсутствующее название", [])])
def test_find_all_ids(input, expected_output):
    result = get_compare.find_all_ids(input)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output


# @pytest.fixture(params=[
#     (
#             [462335, 462336],
#             [Info.query.filter_by(geonameid=462335).first(), Info.query.filter_by(geonameid=462336).first()]),
#     ([], [])
# ])
# def items_by_ids_validation(request):
#     return request.param

@pytest.fixture()
def items_by_ids_validation(request):
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
        print("output: {0}, expected: {1}".format(result, expected_output))
        assert result == expected_output

# @pytest.fixture(params=[
#     ("Знаменка", "Национальный парк Хибины", {'compares': {'Northern geo': 'Khibiny National Park',
#                                                            'Northern latitude': '67.7252',
#                                                            'Timezones_difference': 0},
#                                               'geo_1': {'admin1_code': '51',
#                                                         'admin2_code': '',
#                                                         'admin3_code': '',
#                                                         'admin4_code': '',
#                                                         'alternatenames': ['Знаменка'],
#                                                         'asciiname': 'Znamenka',
#                                                         'cc2': '',
#                                                         'country_code': 'RU',
#                                                         'dem': 132,
#                                                         'elevation': '',
#                                                         'feature class': 'P',
#                                                         'feature_code': 'PPL',
#                                                         'geonameid': 462335,
#                                                         'latitude': '55.3298',
#                                                         'longitude': '42.7586',
#                                                         'modification_date': '2012-01-17',
#                                                         'name': 'Znamenka',
#                                                         'population': 0,
#                                                         'timezone': 'Europe/Moscow'},
#                                               'geo_2': {'admin1_code': '49',
#                                                         'admin2_code': '',
#                                                         'admin3_code': '',
#                                                         'admin4_code': '',
#                                                         'alternatenames': ["Nacional'nyj park Khibiny",
#                                                                            'Национальный парк Хибины'],
#                                                         'asciiname': 'Khibiny National Park',
#                                                         'cc2': '',
#                                                         'country_code': 'RU',
#                                                         'dem': 1075,
#                                                         'elevation': '',
#                                                         'feature class': 'L',
#                                                         'feature_code': 'PRK',
#                                                         'geonameid': 12122507,
#                                                         'latitude': '67.7252',
#                                                         'longitude': '33.4738',
#                                                         'modification_date': '2020-01-20',
#                                                         'name': 'Khibiny National Park',
#                                                         'population': 0,
#                                                         'timezone': 'Europe/Moscow'}}),
#     ("Неизместное имя 2", "Неизместное имя 2", {'compares': None, 'geo_1': None, 'geo_2': None})
# ])
# def info_comparison_validation(request):
#     return request.param
#
#
# def test_info_comparison(info_comparison_validation):
#     (geo_1, geo_2, expected_output) = info_comparison_validation
#     result = get_compare.info_comparison(geo_1, geo_2)
#     print("output: {0}, expected: {1}".format(result, expected_output))
#     assert result == expected_output
