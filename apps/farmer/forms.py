# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField, FileField, TextAreaField
from wtforms.validators import DataRequired
from apps.farmer.models import *


class EditFarmerForm(FlaskForm):
    lastName = StringField('Surname', validators=[DataRequired()], id='lastName')
    firstName = StringField('Firstname', id='firstName')
    gender = SelectField('Gender', id='gender', choices=[
                        Gender.MALE.name, Gender.FEMALE.name])
    birthdate = DateField('Date of Birth', id='birthdate', format='%d/%m/%Y')
    idNumber = StringField('ID Number', id='idNumber')
    groupement = SelectField('Groupement', id='groupement')
    village = SelectField('Village', id='village')
    stamp = StringField('Poincon', id='stamp')
    ancienCode = StringField('Ancien Code', id='ancienCode')

    certification = StringField('Certification', id='certification')

    tempManpower = StringField('Temporary Manpower', id='tempManpower')
    permanentManpower = StringField('Permanent Manpower', id='permanentManpower')

    grpMembershipDate = DateField('Membership Date', id='grpMembershipDate', format='%d/%m/%Y')

    registrationStatus = SelectField('Registration Status', id='registrationStatus', choices=[
                        'Ancien', 'Nouveau'])
    status = SelectField('Status', id='status', choices=[
                        FarmerStatus.PENDING.name, FarmerStatus.EXCLUDED.name, FarmerStatus.APPROVED.name])

    statusComment = TextAreaField('Comment', id='statusComment')

    # inCollaboration = db.Column(db.Boolean, default=False)
    # nonCollaboarationReason = db.Column(db.String(250))

    # grpMembership = db.Column(db.String(20))
    # grpMembershipDate = db.Column(db.Date)

    # hhMembers = db.Column(db.Integer)




    # season = db.relationship(
    #     "Season", secondary=season_farmer, backref=db.backref("season"), lazy=True, uselist=False)

    submit = SubmitField('Save', id='save_farmer_profile')


class EditFarmForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()], id='name')
    description = StringField('Details', id='description')
    overallSize = StringField('Surface en Ha', id='overallSize')
    totalPlants = StringField('Plants', id='totalPlants')
    productivePlants = StringField('Plants Productives', id='productivePlants')
    averageAge = StringField('Age Moyen', id='averageAge')
    estimatedProduction = StringField(
        'Production Estimée', id='estimatedProduction')
    estimated_VRAC = StringField(
        'Production Estimée Vrac', id='estimated_VRAC')
    inspected = StringField('Inspected', id='inspected')

    submit = SubmitField('Save', id='save_farmer_profile')


class UploadFarmerForm(FlaskForm):
    uploadFile = FileField('UploadFile', validators=[
        DataRequired()], id='UploadFile')
