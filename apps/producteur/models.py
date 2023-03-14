# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref

from apps import db, login_manager
from apps.configuration.models import Groupement, Village
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
    groupement = relationship(Groupement, backref=backref('producteurs'))
    village_id = db.Column(db.Integer, db.ForeignKey(
        'village.id'), nullable=False)
    village = relationship(Village, backref=backref('producteurs'))
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


def fetch_producteur(session, producteur_info, campagne):
    producteur = Producteur.query.filter(
        func.lower(Producteur.nom) == func.lower(producteur_info["nom"]),
        func.lower(Producteur.prenom) == func.lower(producteur_info["prenom"]),
        func.lower(Producteur.cni) == func.lower(producteur_info["cni"])
    ).first()
    if producteur:
        # print("Producteur: " + json.dumps(producteur, cls=AlchemyEncoder), flush=True)
        return producteur.id
    else:
        next_code = get_next_producteur_code(
            session, producteur_info["groupement_id"])
        # print("Next Producteur Code: " + next_code, flush=True)
        producteur_info["code"] = next_code
        p = Producteur(**producteur_info)
        c = fetch_campagne(session, campagne)
        p.campagnes.append(c)
        session.add(p)
        session.commit()
        return p.id


def get_next_producteur_code(session, groupement_id):
    groupement = Groupement.query.get(groupement_id)
    try:
        last_groupement_producteur_code = Producteur.query.with_entities(Producteur.code).filter(
            Producteur.code.like("%" + groupement.code + "%")
        ).order_by(
            Producteur.code.desc()
        ).first()

        if not last_groupement_producteur_code:
            print("Oops, no result found for groupement " + groupement.code +
                  ". Returning code: " + groupement.code + "-" + '{0:04}'.format(1))
            return groupement.code + "-" + '{0:04}'.format(1)
        else:
            last_groupement_producteur_number = str(
                last_groupement_producteur_code.code).replace(groupement.code + "-", "")
            return groupement.code + "-" + '{0:04}'.format(int(last_groupement_producteur_number) + 1)
    except:
        print("An error error occurred while fetching for the next producteur groupement code: " + groupement.code)
        raise


# @login_manager.producteur_loader
# def producteur_loader(id):
#     return Producteur.query.filter_by(id=id).first()


# @login_manager.request_loader
# def request_loader(request):
#     username = request.form.get('username')
#     user = Users.query.filter_by(username=username).first()
#     return user if user else None
