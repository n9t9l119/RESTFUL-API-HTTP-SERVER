import os.path
from typing import IO

from config import db_path, ru_txt_path, timezones_txt_path
from db.convert_timezones_to_db import convert_timezones_txt_to_db
from db.сreate_info_nameid_db import convert_ru_txt_to_db, add_to_db


def create_db(ru_txt: IO, timezones_txt: IO):
    convert_ru_txt_to_db(ru_txt)
    add_to_db(convert_timezones_txt_to_db(timezones_txt))


if __name__ == '__main__':
    if not os.path.exists('..' + db_path):
        print("Database creation is started")

        ru_txt = open(ru_txt_path, 'r', encoding="utf8")
        timezones_txt = open(timezones_txt_path, 'r', encoding="utf8")

        create_db(ru_txt, timezones_txt)

        print("Database creation was completed successfully")
    else:
        print("Database is already exist!")
