import re


class Patterns:
    lst = [r'[0-9]{6,8}$', '', '', '', r'[-]?[0-9]{1,3}\.*[0-9]{0,5}$', r'[-]?[0-9]{1,3}\.*[0-9]{0,5}$',
           r'[A-Z]{1,4}$', r'[A-Z\d]{2,5}$', 'RU', '', r'[0-9\w]{2}|^$', '', '', '', r'[0-9]*$', '', r'[-]?[0-9]*$',
           r'[\w-]*/[\w-]*|^$', r'[0-9]{4}-[0-9]{2}-[0-9]{2}$']


def test_cells_info():
    ru = open('../../db_in_txt/RU.txt', 'r', encoding="utf8")
    for string in ru.readlines():
        cells = string.split('\t')
        match_cells(cells)


def match_cells(cells):
    for count in range(len(Patterns.lst)):
        if Patterns.lst[count] != '':
            assert re.match(Patterns.lst[count], cells[count])
