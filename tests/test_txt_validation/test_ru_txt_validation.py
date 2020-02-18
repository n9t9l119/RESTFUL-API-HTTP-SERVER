import re


def test_cells_info():
    ru = open('../../db_in_txt/RU.txt', 'r', encoding="utf8")
    for string in ru.readlines():
        cells = string.split('\t')
        assert re.match(r'[0-9]{6,8}$', cells[0]) \
               and re.match(r'[A-Z]*', cells[2]) \
               and re.match(r'[-]?[0-9]{1,3}\.*[0-9]{0,5}$', cells[4]) \
               and re.match(r'[-]?[0-9]{1,3}\.*[0-9]{0,5}$', cells[5]) \
               and re.match(r'[A-Z]{1,4}$', cells[6]) \
               and re.match(r'[A-Z\d]{2,5}$', cells[7]) \
               and re.match('RU', cells[8]) \
               and re.match(r'[0-9\w]{2}|^$', cells[10]) \
               and re.match(r'[0-9]*$', cells[14]) \
               and re.match(r'[-]?[0-9]*$', cells[16]) \
               and re.match(r'[\w-]*/[\w-]*|^$', cells[17]) \
               and re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}$', cells[18])

