from flask_login import UserMixin

from apps import db, login_manager
from apps.models import *


class Season(db.Model):
    __tablename__ = "season"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    default = db.Column(db.Boolean, default=False)
    __table_args__ = (
        db.UniqueConstraint('name', 'default'),
    )


class Animateur(db.Model):
    __tablename__ = "animateur"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    telephone = db.Column(db.String(50))
    email = db.Column(db.String(50))
    __table_args__ = (
        db.UniqueConstraint('nom', 'prenom'),
    )

    def __init__(self, id, firstName, lastName, telephone, email):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.telephone = telephone
        self.email = email


class Groupement(db.Model):
    __tablename__ = "groupement"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    villageId = db.Column(db.Integer, db.ForeignKey(
        'village.id'), nullable=False)
    
    certification = db.Column(db.String(20))
    certificationDate = db.Column(db.Date)
    
    latitude = db.Column(db.Numeric(11, 8))
    longitude = db.Column(db.Numeric(11, 8))
    altitude = db.Column(db.Float)
    accuracy = db.Column(db.Float)


    __table_args__ = (
        db.UniqueConstraint('type', 'code', 'villageId'),
    )

    def __init__(self, type, code, name, villageId, certification, certificationDate, latitude, longitude, altitude, accuracy, id=None, gps=None):
        self.id = id
        self.type = type
        self.code = code
        self.name = name
        self.villageId = villageId
        self.certification = certification
        self.certificationDate = certificationDate
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.accuracy = accuracy


class District(db.Model):
    __tablename__ = "district"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    communes = db.relationship(
        "Commune", backref=db.backref("commune"), lazy=True)

    def __init__(self, code, name, id=None):
        self.id = id
        self.code = code
        self.name = name


class Commune(db.Model):
    __tablename__ = "commune"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    district_id = db.Column(db.Integer, db.ForeignKey(
        'district.id'), nullable=False)
    fokotanies = db.relationship(
        "Fokontany", backref=db.backref("fokontany"), lazy=True)
    __table_args__ = (
        db.UniqueConstraint('code', 'name', 'district_id'),
    )

    def __init__(self, code, name, district_id, id=None):
        self.id = id
        self.code = code
        self.name = name
        self.district_id = district_id


class Fokontany(db.Model):
    __tablename__ = "fokontany"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    commune_id = db.Column(db.Integer, db.ForeignKey(
        'commune.id'), nullable=False)
    villages = db.relationship("Village", backref=db.backref("village"))
    __table_args__ = (
        db.UniqueConstraint('code', 'name', 'commune_id'),
    )

    def __init__(self, code, name, commune_id, id=None):
        self.id = id
        self.code = code
        self.name = name
        self.commune_id = commune_id


class Village(db.Model):
    __tablename__ = "village"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    fokontany_id = db.Column(db.Integer, db.ForeignKey(
        'fokontany.id'), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('code', 'name', 'fokontany_id'),
    )

    def __init__(self, code, name, fokontany_id, id=None):
        self.id = id
        self.code = code
        self.name = name
        self.fokontany_id = fokontany_id



def fetch_district(session, name):
    district = District.query.filter_by(name=name.upper()).first()
    if district:
        return district.id
    else:
        d = District(name.upper(), name.upper())
        session.add(d)
        session.commit()
        return d.id


def fetch_commune(session, name, district_id=None):
    commune = Commune.query.filter_by(name=name.upper()).first()
    if commune:
        return commune.id
    else:
        c = Commune(name.upper(), name.upper(), district_id)
        session.add(c)
        session.commit()
        return c.id


def fetch_fokontany(session, name, commune_id=None):
    fokontany = Fokontany.query.filter_by(name=name.upper()).first()
    if fokontany:
        return fokontany.id
    else:
        f = Fokontany(name.upper(), name.upper(), commune_id)
        session.add(f)
        session.commit()
        return f.id


def fetch_village(session, name, fokontany_id=None):
    village = Village.query.filter_by(name=name.upper()).first()
    if village:
        return village.id
    else:
        v = Village(name.upper(), name.upper(), fokontany_id)
        session.add(v)
        session.commit()
        return v.id


def fetch_groupement(session, name, village_id=None, type="COOPERATIVE"):
    groupement = Groupement.query.filter_by(groupement=name.upper()).first()
    if groupement:
        return groupement.id
    else:
        g = Groupement(type, name.upper(), name.upper(), village_id)
        session.add(g)
        session.commit()
        return g.id


def fetch_campagne(session, campagne_name):

    print("Provided campagne name: " + campagne_name, flush=True)
    campagne = Campagne.query.filter_by(name=campagne_name.upper()).first()
    if campagne is not None:
        print("Fetched campagne: " +
              json.dumps(campagne, cls=AlchemyEncoder), flush=True)
        return campagne
    else:
        print("Provided campagne name: '" +
              campagne_name + "' not found", flush=True)
        c = Campagne.query.filter_by(name="2023-2024").first()
        print("Fetched default campagne: " +
              json.dumps(c, cls=AlchemyEncoder), flush=True)
        return c
