import pytest

from api_methods import get_hint


# @pytest.fixture(params=[
#     ("Zname", ['Znamenka', 'Znamenskoye']),
#      ("Знак В Память О Пребывании В Омске В 19",
#      ['Знак В Память О Пребывании В Омске В 1926 Году Николая И Елены Рерихов']),
#     ("Katayama", [])
#     #("yama", "Incorrect request!")
# ])
# def value_validation(request):
#     return request.param

@pytest.mark.parametrize("input, expected_output", [("Zname", ['Znamenka', 'Znamenskoye']),
                                                    ("Знак В Память О Пребывании В Омске В 19",
                                                     ['Знак В Память О Пребывании В Омске В 1926 Году Николая И Елены Рерихов']),
                                                    ("Katayama", [])])
def test_make_hint_list(input, expected_output):
    result = get_hint.make_hint_list(input)
    print("output: {0}, expected: {1}".format(result, expected_output))
    assert result == expected_output


# @pytest.fixture(params=[
#     ("Znamenka", True),
#     ("Знак В Память О Пребывании В Омске В 19", True),
#     ("Katayama", True)
#     #("yama", "Incorrect request!")
# ])
# def request_validation(request):
#     return request.param

@pytest.mark.parametrize("input", ["Znamenka", "Знак В Память О Пребывании В Омске В 19", "Katayama"])
def test_request_validation(input):
    # (request, expected_output) = request_validation
    result = get_hint.request_validation(input)
    # print("output: {0}, expected: {1}".format(result, expected_output))
    # assert result == expected_output
    assert result == True
