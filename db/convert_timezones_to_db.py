from db.database_declaration import Info, Timezones


def convert_timezones_txt_to_db(timezones_txt):
    timezones_db_lst = []
    timezones_lst = get_timezones()
    for cells in timezones_txt.readlines():
        cells = cells.split('\t')
        timezones_db_lst = append_timezone_to_db(timezones_lst, timezones_db_lst, cells)
    return timezones_db_lst


def append_timezone_to_db(timezones_lst, timezones_db_lst, cells):
    if cells[1] in timezones_lst:
        timezones_db_lst.append(Timezones(time_zone=cells[1], offset=cells[3]))
    return timezones_db_lst


def get_timezones():
    timezones_lst = []
    for item in Info.query.all():
        if item.timezone not in timezones_lst:
            timezones_lst.append(item.timezone)
    return timezones_lst



