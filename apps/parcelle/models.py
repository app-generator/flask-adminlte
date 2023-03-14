from flask_login import UserMixin

from apps import db, login_manager
from apps.models import *


class Farm(db.Model):
    __tablename__ = "plot"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    farmId = db.Column(db.String(10))
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    status = db.Column(db.String(50))
    crops = db.Column(db.String(50))
    overallSize = db.Column(db.Float)
    productiveSize = db.Column(db.Float)

    totalPlants = db.Column(db.Integer)
    productivePlants = db.Column(db.Integer)

    averageAge = db.Column(db.Integer)

    plotPicture = db.Column(db.String(500))

    estimatedProduction = db.Column(db.Integer)
    estimatedProduction_last = db.Column(db.Integer)
    estimated_VRAC = db.Column(db.Float)

    latitude = db.Column(db.Numeric(11, 8))
    longitude = db.Column(db.Numeric(11, 8))
    altitude = db.Column(db.Float)
    accuracy = db.Column(db.Float)

    xsaison_last = db.Column(db.String(50))
    xsaison_last_but_one = db.Column(db.String(50))
    xsaison_last_but_two = db.Column(db.String(50))

    inspected = db.Column(db.Boolean, default=False)

    inspectionDate = db.Column(db.Date)
    inspectedBy = db.Column(db.String(50))

    farmerId = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    seasonId = db.Column(
        db.Integer, db.ForeignKey('season.id'), nullable=True)

    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

    __table_args__ = (
        db.UniqueConstraint('farmerId', 'seasonID', 'farmID'),
    )

    def __init__(self, farmId, name, description, status, crops, overallSize, productiveSize, totalPlants, productivePlants, averageAge, plotPicture, estimatedProduction, estimatedProduction_last, estimated_VRAC, latitude, longitude, altitude, accuracy, xsaison_last, xsaison_last_but_one, xsaison_last_but_two, inspected, inspectionDate, inspectedBy, id=None, farmerId=None, seasonId=None):
        self.id = id
        self.farmId = farmId
        self.name = name
        self.description = description
        self.status = status
        self.crops = crops
        self.overallSize = overallSize
        self.productiveSize = productiveSize
        self.totalPlants = totalPlants
        self.productivePlants = productivePlants
        self.averageAge = averageAge
        self.plotPicture = plotPicture
        self.estimatedProduction = estimatedProduction
        self.estimatedProduction_last = estimatedProduction_last
        self.estimated_VRAC = estimated_VRAC
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.accuracy = accuracy

        self.xsaison_last = xsaison_last
        self.xsaison_last_but_one = xsaison_last_but_one
        self.xsaison_last_but_two = xsaison_last_but_two

        self.inspected = inspected
        self.inspectionDate = inspectionDate
        self.inspectedBy = inspectedBy

        self.farmerId = farmerId
        self.seasonId = seasonId




class FarmMetadata(db.Model):
    __tablename__ = "farm_metadata"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    farmId = db.Column(db.Integer, db.ForeignKey('far.id'), nullable=False)
    createdBy = db.Column(db.String(50))
    source = db.Column(db.String(50))
    surveyDate = db.Column(db.DateTime, default=db.func.now())
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())