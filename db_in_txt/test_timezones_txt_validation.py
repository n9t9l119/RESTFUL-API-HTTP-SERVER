import re


def test_cells_timezones():
    timezones = open('../db_in_txt/timezones.txt', 'r', encoding="utf8")
    strings = timezones.readlines()[1:]
    for string in strings:
        cells = string.split('\t')
        assert re.match(r'([\w-]*\/){1,2}[\w-]*$', cells[1]) \
               and re.match(r'[-]?[0-9]{1,2}\.[0-9]|0$', cells[3])
