# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager
from apps.models import *


class Parcelle(db.Model):
    __tablename__ = "parcelle"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producteur_id = db.Column(db.Integer, db.ForeignKey(
        'producteur.id'), nullable=False)
    campagne_id = db.Column(
        db.Integer, db.ForeignKey('campagne.id'), nullable=True)
    nomParcelle = db.Column(db.String(50))
    descriptionParcelle = db.Column(db.String(50))
    statutParcelle = db.Column(db.String(50))
    surface = db.Column(db.Float)
    totalPlants = db.Column(db.Integer)
    plantsProductives = db.Column(db.Integer)
    ageMoyenPlants = db.Column(db.Integer)
    photoParcelle = db.Column(db.String(500))
    estimationProduction = db.Column(db.Integer)
    estimationProduction_last = db.Column(db.Integer)
    estimation_VRAC = db.Column(db.Float)
    latitude = db.Column(db.Numeric(11, 8))
    longitude = db.Column(db.Numeric(11, 8))
    altitude = db.Column(db.Float)
    xsaison_last = db.Column(db.String(50))
    xsaison_last_but_one = db.Column(db.String(50))
    xsaison_last_but_two = db.Column(db.String(50))
    __table_args__ = (
        db.UniqueConstraint('producteur_id', 'campagne_id', 'nomParcelle'),
    )

    def __init__(self, nomParcelle, descriptionParcelle, statutParcelle, surface, totalPlants, plantsProductives, ageMoyenPlants, photoParcelle, estimationProduction, estimationProduction_last, estimation_VRAC, latitude, longitude, altitude, xsaison_last, xsaison_last_but_one, xsaison_last_but_two, id=None, producteur_id=None, campagne_id=None):
        self.id = id
        self.producteur_id = producteur_id
        self.campagne_id = campagne_id
        self.nomParcelle = nomParcelle
        self.descriptionParcelle = descriptionParcelle
        self.statutParcelle = statutParcelle
        self.surface = surface
        self.totalPlants = totalPlants
        self.plantsProductives = plantsProductives
        self.ageMoyenPlants = ageMoyenPlants
        self.photoParcelle = photoParcelle
        self.estimationProduction = estimationProduction
        self.estimationProduction_last = estimationProduction_last
        self.estimation_VRAC = estimation_VRAC
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.xsaison_last = xsaison_last
        self.xsaison_last_but_one = xsaison_last_but_one
        self.xsaison_last_but_two = xsaison_last_but_two


