# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager
from apps.models import *


class Producteur(db.Model):
    __tablename__ = "producteur"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20), unique=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    genre = db.Column(db.String(15))
    dateNaissance = db.Column(db.DateTime)
    cni = db.Column(db.String(50))
    photo_cni = db.Column(db.String(500))
    photo = db.Column(db.String(500))
    poincon = db.Column(db.String(50))
    coopMembersip = db.Column(db.Integer)
    statusEnregistrement = db.Column(db.String(50))
    tempManpower = db.Column(db.String(50))
    permanentManpower = db.Column(db.Integer)
    ancienCode = db.Column(db.String(20))
    groupement_id = db.Column(db.Integer, db.ForeignKey(
        'groupement.id'), nullable=False)
    village_id = db.Column(db.Integer, db.ForeignKey(
        'village.id'), nullable=False)
    parcelles = db.relationship(
        "Parcelle", backref=db.backref("parcelle"), lazy=True)
    campagnes = db.relationship(
        "Campagne", secondary=campagne_producteur, backref=db.backref("campagne"), lazy=True)
    __table_args__ = (
        db.UniqueConstraint('nom', 'prenom', 'cni', 'groupement_id'),
    )

    def __init__(self, nom, prenom, code, genre, dateNaissance, cni, groupement_id, village_id, photo=None, photo_cni=None, poincon=None, coopMembersip=None, statusEnregistrement='Nouveau', tempManpower=None, permanentManpower=None, ancienCode=None, id=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.code = code
        self.genre = genre
        self.dateNaissance = datetime.strptime(str(dateNaissance), '%d/%m/%Y')
        self.photo = photo
        self.cni = cni
        self.photo_cni = photo_cni
        self.groupement_id = groupement_id
        self.village_id = village_id
        self.poincon = poincon
        self.coopMembersip = coopMembersip
        self.statusEnregistrement = statusEnregistrement
        self.tempManpower = tempManpower
        self.permanentManpower = permanentManpower
        self.ancienCode = ancienCode


# @login_manager.producteur_loader
# def producteur_loader(id):
#     return Producteur.query.filter_by(id=id).first()


# @login_manager.request_loader
# def request_loader(request):
#     username = request.form.get('username')
#     user = Users.query.filter_by(username=username).first()
#     return user if user else None
