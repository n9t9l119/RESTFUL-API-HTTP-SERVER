from config import db


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    geonameid = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    asciiname = db.Column(db.String(64), unique=False, nullable=False)
    alternatenames = db.Column(db.String(256), unique=False, nullable=True)
    latitude = db.Column(db.String(64), unique=False, nullable=False)
    longitude = db.Column(db.String(256), unique=False)
    feature_class = db.Column(db.String(1), unique=False, nullable=False)
    feature_code = db.Column(db.String(10), unique=False, nullable=False)
    country_code = db.Column(db.String(2), unique=False, nullable=False)
    cc2 = db.Column(db.String(200), unique=False, nullable=False)
    admin1_code = db.Column(db.String(20), unique=False, nullable=False)
    admin2_code = db.Column(db.String(80), unique=False, nullable=False)
    admin3_code = db.Column(db.String(20), unique=False, nullable=False)
    admin4_code = db.Column(db.String(20), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False)
    elevation = db.Column(db.Integer, unique=False)
    dem = db.Column(db.Integer, unique=False)
    timezone = db.Column(db.String(40), unique=False, nullable=False)
    modification_date = db.Column(db.String(40), unique=False, nullable=False)
    id_link = db.relationship('NameId', backref='idlnk', lazy='dynamic')
    timezone_offset = db.relationship('Timezones', backref='timezone', uselist=False)


class NameId(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(384))
    geonameid = db.Column(db.Integer, db.ForeignKey('info.geonameid'))


class Timezones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_zone = db.Column(db.String(40), db.ForeignKey('info.timezone'))
    offset = db.Column(db.Float())



