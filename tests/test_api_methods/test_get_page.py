import pytest

from api_methods import get_page
from db.database_declaration import Info


@pytest.fixture()
def page_items_value_validation():
    max_items_value = len(Info.query.all())

    def params_lst():
        params = [(3, 2),
                  (0, max_items_value)]
        return params

    return params_lst()


def test_input_validation(page_items_value_validation):
    for tup in page_items_value_validation:
        (page_number, items_value) = tup
        result = get_page.input_validation(page_number, items_value)
        assert result == True
