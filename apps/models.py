from datetime import datetime
from sqlalchemy.sql.expression import func, false
from .__init__ import *
from .utility import *


class VDMataReferencementBrut(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(50), unique=True)
    completionDate = db.Column(db.DateTime)
    submissionDate = db.Column(db.DateTime)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)
    deviceid = db.Column(db.String(50))
    devicephonenum = db.Column(db.String(50))
    username = db.Column(db.String(50))
    device_info = db.Column(db.String(150))
    duration = db.Column(db.Integer)
    caseid = db.Column(db.Integer)
    users = db.Column(db.String(50))
    campagne = db.Column(db.String(50))
    dateEnquete = db.Column(db.DateTime)
    consentement = db.Column(db.String(50))
    nouveauAncien = db.Column(db.String(50))
    pgroupement = db.Column(db.String(50))
    producteur = db.Column(db.String(50))
    pCodeProducteur = db.Column(db.String(50))
    pNom = db.Column(db.String(50))
    pPrenom = db.Column(db.String(50))
    pPhoto = db.Column(db.String(500))
    pPoincon = db.Column(db.String(50))
    pGenre = db.Column(db.String(50))
    pCin = db.Column(db.String(50))
    pPhotoCin = db.Column(db.String(500))
    pDateNaissance = db.Column(db.String(50))
    pDistrict = db.Column(db.String(50))
    pCommune = db.Column(db.String(50))
    pFokontany = db.Column(db.String(50))
    pVillage = db.Column(db.String(50))
    coopMembersip = db.Column(db.Integer)
    tempManpower = db.Column(db.String(50))
    permanentManpower = db.Column(db.Integer)
    nombreParcelles = db.Column(db.Integer)
    parcelles_count = db.Column(db.Integer)
    idParcelle_1 = db.Column(db.Integer)
    nomParcelle_1 = db.Column(db.String(50))
    descriptionParcelle_1 = db.Column(db.String(50))
    statutParcelle_1 = db.Column(db.String(50))
    surface_1 = db.Column(db.Float)
    surface_1 = db.Column(db.String(50))
    totalPlants_1 = db.Column(db.Integer)
    plantsProductives_1 = db.Column(db.Integer)
    ageMoyenPlants_1 = db.Column(db.Integer)
    photoParcelle_1 = db.Column(db.String(500))
    estimationProduction_1 = db.Column(db.Integer)
    estimationProduction_last_1 = db.Column(db.Integer)
    estimation_VRAC_1 = db.Column(db.Float)
    GPS_1 = db.Column(db.String(50))
    xsaison_last_1 = db.Column(db.String(50))
    xsaison_last_but_one_1 = db.Column(db.String(50))
    xsaison_last_but_two_1 = db.Column(db.String(50))
    idParcelle_2 = db.Column(db.String(50))
    nomParcelle_2 = db.Column(db.String(50))
    descriptionParcelle_2 = db.Column(db.String(50))
    statutParcelle_2 = db.Column(db.String(50))
    consigneGarmin_2 = db.Column(db.String(50))
    # surface_2 = db.Column(db.String(50))
    surface_2 = db.Column(db.Float)
    totalPlants_2 = db.Column(db.Integer)
    plantsProductives_2 = db.Column(db.Integer)
    ageMoyenPlants_2 = db.Column(db.Integer)
    photoParcelle_2 = db.Column(db.String(500))
    estimationProduction_2 = db.Column(db.Float)
    estimationProduction_last_2 = db.Column(db.Float)
    estimation_VRAC_2 = db.Column(db.Float)
    GPS_2 = db.Column(db.String(50))
    xsaison_last_2 = db.Column(db.String(50))
    xsaison_last_but_one_2 = db.Column(db.String(50))
    xsaison_last_but_two_2 = db.Column(db.String(50))
    instanceID = db.Column(db.String(50))
    formdef_version = db.Column(db.String(50))
    review_quality = db.Column(db.String(50))
    review_status = db.Column(db.String(50))
    processed = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(
        db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

    # TODO: Handle multiple parcelles - Up to 5

    def __init__(self, key, CompletionDate, SubmissionDate, starttime, endtime, deviceid, devicephonenum, username, device_info, duration, caseid, users, campagne, dateEnquete, consentement, NouveauAncien, pgroupement, pNom, pPrenom, pPhoto, pPoincon, pGenre, pCin, pPhotoCin, pDateNaissance, CoopMembersip, TempManpower, PermanentManpower, NombreParcelles, Parcelles_count, NomParcelle_1, DescriptionParcelle_1, StatutParcelle_1, ConsigneGarmin_1, Surface_1, TotalPlants_1, PlantsProductives_1, AgeMoyenPlants_1, PhotoParcelle_1, EstimationProduction_1, EstimationProduction_last_1, Estimation_VRAC_1, GPS_1, xsaison_last_1, xsaison_last_but_one_1, xsaison_last_but_two_1, instanceID, formdef_version, review_quality, review_status, pDistrict=None, pCommune=None, pFokontany=None, pVillage=None, producteur=None, pCodeProducteur=None, id=None, idParcelle_1=None, idParcelle_2=None, NomParcelle_2=None, DescriptionParcelle_2=None, StatutParcelle_2=None, ConsigneGarmin_2=None, Surface_2=None, TotalPlants_2=None, PlantsProductives_2=None, AgeMoyenPlants_2=None, PhotoParcelle_2=None, EstimationProduction_2=None, EstimationProduction_last_2=None, Estimation_VRAC_2=None, GPS_2=None, xsaison_last_but_one_2=None, xsaison_last_2=None, xsaison_last_but_two_2=None, processed=False, pAncienCodeProducteur=None, created_on=None, updated_on=None):
        self.id = id
        self.key = key
        self.completionDate = datetime.strptime(
            str(CompletionDate), '%b %d, %Y %H:%M:%S %p')
        self.submissionDate = datetime.strptime(
            str(SubmissionDate), '%b %d, %Y %H:%M:%S %p')
        self.starttime = datetime.strptime(
            str(starttime), '%b %d, %Y %H:%M:%S %p')
        self.endtime = datetime.strptime(str(endtime), '%b %d, %Y %H:%M:%S %p')
        self.deviceid = deviceid
        self.devicephonenum = devicephonenum
        self.username = username
        self.device_info = device_info
        self.duration = duration
        self.caseid = caseid
        self.users = users
        self.campagne = campagne
        self.dateEnquete = datetime.strptime(str(dateEnquete), '%b %d, %Y')
        self.consentement = consentement
        self.nouveauAncien = NouveauAncien
        self.pgroupement = pgroupement
        self.producteur = producteur
        self.pCodeProducteur = pCodeProducteur
        self.pAncienCodeProducteur = pAncienCodeProducteur
        self.pNom = pNom
        self.pPrenom = pPrenom
        self.pPhoto = pPhoto
        self.pPoincon = pPoincon
        self.pGenre = pGenre
        self.pCin = pCin
        self.pPhotoCin = pPhotoCin
        self.pDateNaissance = pDateNaissance
        self.pDistrict = pDistrict
        self.pCommune = pCommune
        self.pFokontany = pFokontany
        self.pVillage = pVillage
        self.coopMembersip = CoopMembersip
        self.tempManpower = TempManpower
        self.permanentManpower = PermanentManpower
        self.nombreParcelles = NombreParcelles
        self.parcelles_count = Parcelles_count
        self.idParcelle_1 = idParcelle_1
        self.nomParcelle_1 = NomParcelle_1
        self.descriptionParcelle_1 = DescriptionParcelle_1
        self.statutParcelle_1 = StatutParcelle_1
        self.consigneGarmin_1 = ConsigneGarmin_1
        self.surface_1 = Surface_1
        self.totalPlants_1 = TotalPlants_1
        self.plantsProductives_1 = PlantsProductives_1
        self.ageMoyenPlants_1 = AgeMoyenPlants_1
        self.photoParcelle_1 = PhotoParcelle_1
        self.estimationProduction_1 = EstimationProduction_1
        self.estimationProduction_last_1 = EstimationProduction_last_1
        self.estimation_VRAC_1 = Estimation_VRAC_1
        self.GPS_1 = GPS_1
        self.xsaison_last_1 = xsaison_last_1
        self.xsaison_last_but_one_1 = xsaison_last_but_one_1
        self.xsaison_last_but_two_1 = xsaison_last_but_two_1
        self.idParcelle_2 = idParcelle_2
        self.nomParcelle_2 = NomParcelle_2
        self.descriptionParcelle_2 = DescriptionParcelle_2
        self.statutParcelle_2 = StatutParcelle_2
        self.consigneGarmin_2 = ConsigneGarmin_2
        self.surface_2 = Surface_2
        self.totalPlants_2 = TotalPlants_2
        self.plantsProductives_2 = PlantsProductives_2
        self.ageMoyenPlants_2 = AgeMoyenPlants_2
        self.photoParcelle_2 = PhotoParcelle_2
        self.estimationProduction_2 = EstimationProduction_2
        self.estimationProduction_last_2 = EstimationProduction_last_2
        self.estimation_VRAC_2 = Estimation_VRAC_2
        self.GPS_2 = GPS_2
        self.xsaison_last_but_one_2 = xsaison_last_but_one_2
        self.xsaison_last_2 = xsaison_last_2
        self.xsaison_last_but_two_2 = xsaison_last_but_two_2
        self.instanceID = instanceID
        self.formdef_version = formdef_version
        self.review_quality = review_quality
        self.review_status = review_status
        self.created_on = created_on
        self.updated_on = updated_on


campagne_producteur = db.Table('campagne_producteur',
                               db.Column('campagne_id', db.Integer,
                                         db.ForeignKey('campagne.id')),
                               db.Column('producteur_id', db.Integer,
                                         db.ForeignKey('producteur.id'))
                               )


class Campagne(db.Model):
    __tablename__ = "campagne"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name, id=None):
        self.id = id
        self.name = name


# class Producteur(db.Model):
#     __tablename__ = "producteur"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(20), unique=True)
#     nom = db.Column(db.String(50))
#     prenom = db.Column(db.String(50))
#     genre = db.Column(db.String(15))
#     dateNaissance = db.Column(db.DateTime)
#     cni = db.Column(db.String(50))
#     photo_cni = db.Column(db.String(500))
#     photo = db.Column(db.String(500))
#     poincon = db.Column(db.String(50))
#     coopMembersip = db.Column(db.Integer)
#     statusEnregistrement = db.Column(db.String(50))
#     tempManpower = db.Column(db.String(50))
#     permanentManpower = db.Column(db.Integer)
#     ancienCode = db.Column(db.String(20))
#     groupement_id = db.Column(db.Integer, db.ForeignKey(
#         'groupement.id'), nullable=False)
#     village_id = db.Column(db.Integer, db.ForeignKey(
#         'village.id'), nullable=False)
#     parcelles = db.relationship(
#         "Parcelle", backref=db.backref("parcelle"), lazy=True)
#     campagnes = db.relationship(
#         "Campagne", secondary=campagne_producteur, backref=db.backref("campagne"), lazy=True)
#     __table_args__ = (
#         db.UniqueConstraint('nom', 'prenom', 'cni', 'groupement_id'),
#     )

#     def __init__(self, nom, prenom, code, genre, dateNaissance, cni, groupement_id, village_id, photo=None, photo_cni=None, poincon=None, coopMembersip=None, statusEnregistrement='Nouveau', tempManpower=None, permanentManpower=None, ancienCode=None, id=None):
#         self.id = id
#         self.nom = nom
#         self.prenom = prenom
#         self.code = code
#         self.genre = genre
#         self.dateNaissance = datetime.strptime(str(dateNaissance), '%d/%m/%Y')
#         self.photo = photo
#         self.cni = cni
#         self.photo_cni = photo_cni
#         self.groupement_id = groupement_id
#         self.village_id = village_id
#         self.poincon = poincon
#         self.coopMembersip = coopMembersip
#         self.statusEnregistrement = statusEnregistrement
#         self.tempManpower = tempManpower
#         self.permanentManpower = permanentManpower
#         self.ancienCode = ancienCode


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


class Animateur(db.Model):
    __tablename__ = "animateur"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    telephone = db.Column(db.String(50))
    email = db.Column(db.String(50))
    __table_args__ = (
        db.UniqueConstraint('nom', 'prenom'),
    )

    def __init__(self, id, nom, prenom, telephone, email):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email


class Groupement(db.Model):
    __tablename__ = "groupement"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    code = db.Column(db.String(50), unique=True)
    groupement = db.Column(db.String(50), unique=True)
    village_id = db.Column(db.Integer, db.ForeignKey(
        'village.id'), nullable=False)
    gps = db.Column(db.String(50))
    __table_args__ = (
        db.UniqueConstraint('type', 'code', 'village_id'),
    )

    def __init__(self, type, code, groupement, village_id, id=None, gps=None):
        self.id = id
        self.type = type
        self.code = code
        self.groupement = groupement
        self.village_id = village_id
        self.gps = gps


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


def get_last_fetch(session):
    return session.query(func.max(VDMataReferencementBrut.created_on)).scalar()


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


def vDMataReferencementBrut_parcelles(form):

    producteur_parcelles = []

    print("Parcelle Number = " + str(form.parcelles_count), flush=True)

    x = 1

    while x <= form.parcelles_count:

        # print("Parcelle Name: " + str(form.__getattribute__("nomParcelle_" + str(x))), flush=True)

        parcelle_data = dict()

        parcelle_data["nomParcelle"] = form.__getattribute__(
            "nomParcelle_" + str(x))
        parcelle_data["descriptionParcelle"] = form.__getattribute__(
            "descriptionParcelle_" + str(x))
        parcelle_data["statutParcelle"] = form.__getattribute__(
            "statutParcelle_" + str(x))
        parcelle_data["surface"] = form.__getattribute__("surface_" + str(x))
        parcelle_data["totalPlants"] = form.__getattribute__(
            "totalPlants_" + str(x))
        parcelle_data["plantsProductives"] = form.__getattribute__(
            "plantsProductives_" + str(x))
        parcelle_data["ageMoyenPlants"] = form.__getattribute__(
            "ageMoyenPlants_" + str(x))
        parcelle_data["photoParcelle"] = form.__getattribute__(
            "photoParcelle_" + str(x))
        parcelle_data["estimationProduction"] = form.__getattribute__(
            "estimationProduction_" + str(x))
        parcelle_data["estimationProduction_last"] = form.__getattribute__(
            "estimationProduction_last_" + str(x))
        parcelle_data["estimation_VRAC"] = form.__getattribute__(
            "estimation_VRAC_" + str(x))
        parcelle_data["xsaison_last"] = form.__getattribute__(
            "xsaison_last_" + str(x))
        parcelle_data["xsaison_last_but_one"] = form.__getattribute__(
            "xsaison_last_but_one_" + str(x))
        parcelle_data["xsaison_last_but_two"] = form.__getattribute__(
            "xsaison_last_but_two_" + str(x))

        GPS = form.__getattribute__("GPS_" + str(x))

        if GPS:
            coordinates = GPS.split(" ")
            parcelle_data["latitude"] = coordinates[0]
            parcelle_data["longitude"] = coordinates[1]
            parcelle_data["altitude"] = coordinates[2]
        else:
            parcelle_data["latitude"] = parcelle_data["longitude"] = parcelle_data["altitude"] = None

        # print("Parcelle data: " + json.dumps(parcelle), flush=True)

        producteur_parcelles.append(Parcelle(**parcelle_data))

        x += 1

    # print("Parcelle Producteur data: " + json.dumps(producteur_parcelles,  cls=AlchemyEncoder), flush=True)

    return producteur_parcelles


def add_parcelles_to_producteur(session, producteur_id, parcelles, campagne):

    try:

        c = fetch_campagne(session, campagne)

        for p in parcelles:
            if c:
                p.campagne_id = c.id

            p.producteur_id = producteur_id
            session.add(p)

        session.commit()
    except:
        print("An error error occurred while adding parcelles for producteur: " +
              str(producteur_id))
        session.rollback()

    return True
