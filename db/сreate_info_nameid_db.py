from db.database_declaration import *


def convert_ru_txt_to_db(file):
    db.create_all()
    table = []
    for string in file.readlines():
        cells = make_cells(string)
        table = append_str_to_db(table, cells)
    add_to_db(table)


def make_cells(string):
    cells = string.split('\t')
    cells[-1] = cells[-1].replace("\n", "")
    return cells


def append_str_to_db(table, cells):
    item = convert_str_to_info(cells)
    table.append(item)
    table.extend(convert_str_to_nameid(cells, item))
    return block_commit(table)


def convert_str_to_info(cells):
    info_string = Info(
        geonameid=cells[0],
        name=cells[1],
        asciiname=cells[2],
        alternatenames=cells[3],
        latitude=cells[4],
        longitude=cells[5],
        feature_class=cells[6],
        feature_code=cells[7],
        country_code=cells[8],
        cc2=cells[9],
        admin1_code=cells[10],
        admin2_code=cells[11],
        admin3_code=cells[12],
        admin4_code=cells[13],
        population=cells[14],
        elevation=cells[15],
        dem=cells[16],
        timezone=cells[17],
        modification_date=cells[18])
    return info_string


def convert_str_to_nameid(cells, item):
    all_str_names_to_db = []
    names = all_names_in_str(cells)
    for name in names:
        all_str_names_to_db.append(NameId(name=name, idlnk=item))
    return all_str_names_to_db


def all_names_in_str(cells):
    names = [cells[1]]
    if names[0] != cells[2]:
        names.append(cells[2])
    if cells[4] != "":
        alternatenames = cells[3].split(',')
        for alternatename in alternatenames:
            if alternatename not in names and alternatename != '':
                names.append(alternatename)
    return names


def block_commit(table):
    if len(table) >= 600000:
        add_to_db(table)
        print("Database creation is in progress...")
        return []
    return table


def add_to_db(items):
    db.session.add_all(items)
    db.session.commit()
