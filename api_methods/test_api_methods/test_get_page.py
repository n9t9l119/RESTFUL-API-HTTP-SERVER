from api_methods import get_page
from db.database_declaration import Info
import pytest


@pytest.fixture(params=[
    (0, 1, True),
    (0, -1, "'Page' and 'Items_value' must be a positiv number no less than 1 and no more than 6 digits!")
])
def page_items_value_validation(request):
    return request.param


def test_input_validation(page_items_value_validation):
    (page_number, items_value, expected_output) = page_items_value_validation
    result = get_page.input_validation(page_number, items_value)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output


@pytest.fixture(params=[
    (0, len(Info.query.all()) + 1, "There is not so many values in database!"),
    (0, len(Info.query.all()), True),
    (3, 0, "That page is empty!"),
    (len(Info.query.all()), 1, "That page is empty!")
])
def numerical_range_validation(request):
    return request.param


def test_numerical_range_validation(numerical_range_validation):
    (page_number, items_value, expected_output) = numerical_range_validation
    result = get_page.numerical_range_validation(page_number, items_value)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output


@pytest.fixture(params=[
    (2, 1, [{'admin1_code': '69',
             'admin2_code': '',
             'admin3_code': '',
             'admin4_code': '',
             'alternatenames': ['Zaderikhi', 'Zadirikhi', 'Знаменка'],
             'asciiname': 'Znamenka',
             'cc2': '',
             'country_code': 'RU',
             'dem': 231,
             'elevation': '',
             'feature class': 'P',
             'feature_code': 'PPLQ',
             'geonameid': 462336,
             'latitude': '55.21398',
             'longitude': '32.1047',
             'modification_date': '2012-01-17',
             'name': 'Znamenka',
             'population': 0,
             'timezone': 'Europe/Moscow'}]),
])
def page_validation(request):
    return request.param


def test_page(page_validation):
    (page_number, items_value, expected_output) = page_validation
    result = get_page.page(page_number, items_value)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output
