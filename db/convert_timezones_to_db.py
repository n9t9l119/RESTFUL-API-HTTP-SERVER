from db.database_declaration import Info, Timezones
from typing import List, Union, IO


def convert_timezones_txt_to_db(timezones_txt: IO) -> List[Timezones]:
    timezones_db_lst = []
    timezones_lst = get_timezones()
    for cells in timezones_txt.readlines():
        cells = cells.split('\t')
        timezones_db_lst = append_timezone_to_db(timezones_lst, timezones_db_lst, cells)
    return timezones_db_lst


def append_timezone_to_db(timezones_list: List[str], timezones_db_list: List[Timezones],
                          cells: List[Union[float, str]]) -> List[Timezones]:
    if cells[1] in timezones_list:
        timezones_db_list.append(Timezones(time_zone=cells[1], offset=cells[3]))
    return timezones_db_list


def get_timezones() -> List[str]:
    timezones_list = []
    for item in Info.query.all():
        if item.timezone not in timezones_list:
            timezones_list.append(item.timezone)
    return timezones_list
