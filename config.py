from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

db_path = '/sqlite/geo_info_ru.db'
test_db_path = '/tests/test_geo_info_ru.db'
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + test_db_path

ru_txt_path = '../db_in_txt/RU.txt'
timezones_txt_path = '../db_in_txt/timezones.txt'
test_ru_txt_path = '../tests/test_txt_validation/test_ru.txt'
#
# class BaseConfig(object):
#     db_path = '/sqlite/geo_info_ru.db'
#
#     app.config['JSON_SORT_KEYS'] = False
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + db_path
#
#     ru_txt_path = '../db_in_txt/RU.txt'
#     timezones_txt_path = '../db_in_txt/timezones.txt'
#     test_ru_txt_path = '../db_in_txt/test_ru.txt'


# class TestConfig(BaseConfig):
#     test_db_path = '/sqlite/test_geo_info_ru.db'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + test_db_path



db = SQLAlchemy(app)
