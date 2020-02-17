from api_methods import get_hint
import pytest


@pytest.fixture(params=[
    ("Zname", ['Znamenka', 'Znamenskoye']),
    ("Знак В Память О Пребывании В Омске В 19",
     ['Знак В Память О Пребывании В Омске В 1926 Году Николая И Елены Рерихов']),
    ("Katayama", "There is no hints"),
    ("yama", "Incorrect request!")
])
def value_validation(request):
    return request.param


def test_hint(value_validation):
    (request, expected_output) = value_validation
    result = get_hint.hint(request)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output


@pytest.fixture(params=[
    ("Znamenka", True),
    ("Знак В Память О Пребывании В Омске В 19", True),
    ("Katayama", True),
    ("yama", "Incorrect request!")
])
def request_validation(request):
    return request.param


def test_request_validation(request_validation):
    (request, expected_output) = request_validation
    result = get_hint.request_validation(request)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output
