# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref
import enum

from apps import db, login_manager
from apps.farm.models import *
from apps.configuration.models import *
from datetime import datetime


class FarmerStatus(enum.Enum):
    APPROVED = 'APPROVED'
    EXCLUDED = 'EXCLUDED'
    PENDING = 'PENDING'


class Gender(enum.Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'


class Farmer(db.Model):
    __tablename__ = "farmer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    ancienCode = db.Column(db.String(20))
    registrationStatus = db.Column(db.String(50))

    code = db.Column(db.String(20), unique=True)

    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))

    picture = db.Column(db.String(500))

    stamp = db.Column(db.String(50))

    gender = db.Column(db.Enum(Gender))

    idNumber = db.Column(db.String(50))
    idNumberPicture = db.Column(db.String(500))

    birthdate = db.Column(db.Date)

    inCollaboration = db.Column(db.Boolean, default=False)
    nonCollaboarationReason = db.Column(db.String(250))

    certification = db.Column(db.String(20))

    grpMembership = db.Column(db.String(20))
    grpMembershipDate = db.Column(db.Date)

    tempManpower = db.Column(db.String(50))
    permanentManpower = db.Column(db.Integer)

    hhMembers = db.Column(db.Integer)
    xsaison_last = db.Column(db.String(50))
    xsaison_last_but_one = db.Column(db.String(50))
    xsaison_last_but_two = db.Column(db.String(50))

    farmCount = db.Column(db.Integer)
    status = db.Column(db.Enum(FarmerStatus), default=FarmerStatus.PENDING)
    statusComment = db.Column(db.String(250))

    groupementId = db.Column(db.Integer, db.ForeignKey(
        'groupement.id'), nullable=False)
    groupement = relationship(Groupement, backref=backref('farmers'))

    villageId = db.Column(db.Integer, db.ForeignKey(
        'village.id'), nullable=False)
    village = relationship(Village, backref=backref('farmers'))

    farms = db.relationship(
        "Farm", backref=db.backref("farm"), lazy=True)

    season = db.relationship(
        "Season", secondary=season_farmer, backref=db.backref("season"), lazy=True)

    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(),
                          server_onupdate=db.func.now())

    __table_args__ = (
        db.UniqueConstraint('firstName', 'lastName',
                            'idNumber', 'groupementId'),
    )

    def __init__(self, firstName, lastName, code, gender, birthdate, idNumber, groupementId, villageId, inCollaboration=False, nonCollaboarationReason=None, certification=None, grpMembership=None, grpMembershipDate=None, hhMembers=None, xsaison_last=None, xsaison_last_but_one=None, xsaison_last_but_two=None, farmCount=None, status=FarmerStatus.PENDING, statusComment=None, picture=None, idNumberPicture=None, stamp=None, coopMembersip=None, statusEnregistrement='Nouveau', tempManpower=None, permanentManpower=None, ancienCode=None, id=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.code = code
        self.picture = picture
        self.stamp = stamp
        self.gender = gender
        self.idNumber = idNumber
        self.idNumberPicture = idNumberPicture
        self.birthdate = datetime.strptime(str(birthdate), '%d/%m/%Y')
        self.inCollaboration = inCollaboration
        self.nonCollaboarationReason = nonCollaboarationReason
        self.certification = certification
        self.grpMembership = grpMembership
        self.grpMembershipDate = grpMembershipDate
        self.tempManpower = tempManpower
        self.permanentManpower = permanentManpower
        self.hhMembers = hhMembers
        self.xsaison_last = xsaison_last
        self.xsaison_last_but_one = xsaison_last_but_one
        self.xsaison_last_but_two = xsaison_last_but_two
        self.farmCount = farmCount
        self.status = status
        self.statusComment = statusComment
        self.groupementId = groupementId
        self.villageId = villageId
        self.coopMembersip = coopMembersip
        self.statusEnregistrement = statusEnregistrement
        self.ancienCode = ancienCode


class FarmerMetadata(db.Model):
    __tablename__ = "farmer_metadata"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    farmerId = db.Column(db.Integer, db.ForeignKey(
        'farmer.id'), nullable=False)
    farmers = relationship(
        "Farmer", backref=backref('farmerMetadata'), lazy=True)
    createdBy = db.Column(db.String(50))
    source = db.Column(db.String(50))
    surveyDate = db.Column(db.DateTime, default=db.func.now())
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(),
                          server_onupdate=db.func.now())

    def __init__(self, farmerId, createdBy, source, surveyDate, id=None):
        self.id = id
        self.farmerId = farmerId
        self.createdBy = createdBy
        self.source = source
        self.surveyDate = surveyDate


def fetch_farmer(session, farmer_info, campagne):
    farmer = Farmer.query.filter(
        func.lower(Farmer.nom) == func.lower(farmer_info["nom"]),
        func.lower(Farmer.prenom) == func.lower(farmer_info["prenom"]),
        func.lower(Farmer.cni) == func.lower(farmer_info["cni"])
    ).first()
    if farmer:
        # print("Farmer: " + json.dumps(farmer, cls=AlchemyEncoder), flush=True)
        return farmer.id
    else:
        next_code = get_next_farmer_code(
            session, farmer_info["groupement_id"])
        # print("Next Farmer Code: " + next_code, flush=True)
        farmer_info["code"] = next_code
        p = Farmer(**farmer_info)
        c = fetch_campagne(session, campagne)
        p.campagnes.append(c)
        session.add(p)
        session.commit()
        return p.id


def get_next_farmer_code(session, groupement_id):
    groupement = Groupement.query.get(groupement_id)
    try:
        last_groupement_farmer_code = Farmer.query.with_entities(Farmer.code).filter(
            Farmer.code.like("%" + groupement.code + "%")
        ).order_by(
            Farmer.code.desc()
        ).first()

        if not last_groupement_farmer_code:
            print("Oops, no result found for groupement " + groupement.code +
                  ". Returning code: " + groupement.code + "-" + '{0:04}'.format(1))
            return groupement.code + "-" + '{0:04}'.format(1)
        else:
            last_groupement_farmer_number = str(
                last_groupement_farmer_code.code).replace(groupement.code + "-", "")
            return groupement.code + "-" + '{0:04}'.format(int(last_groupement_farmer_number) + 1)
    except:
        print("An error error occurred while fetching for the next farmer groupement code: " + groupement.code)
        raise
