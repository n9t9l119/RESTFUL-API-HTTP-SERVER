import pytest

from api_methods import get_hint


@pytest.mark.parametrize("input, expected_output", [("Zname", ['Znamenka', 'Znamenskoye']),
                                                    ("Знак В Память О Пребывании В Омске В 19",
                                                     [
                                                         'Знак В Память О Пребывании В Омске В 1926 Году Николая И Елены Рерихов']),
                                                    ("Katayama", [])])
def test_make_hint_list(input, expected_output):
    result = get_hint.make_hint_list(input)
    assert result == expected_output


@pytest.mark.parametrize("input", ["Znamenka", "Знак В Память О Пребывании В Омске В 19", "Katayama"])
def test_request_validation(input):
    result = get_hint.request_validation(input)
    assert result == True
