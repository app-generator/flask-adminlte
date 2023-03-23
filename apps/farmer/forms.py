# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField, FileField
from wtforms.validators import DataRequired


class EditFarmerForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()], id='nom')
    prenom = StringField('Prenon', id='prenon')
    genre = SelectField('Commune', id='genre', choices=[
                        ('male', 'Male'), ('female', 'FEMALE')])
    date = DateField('Date de Naissance', id='date')
    cni = StringField('CNI', id='cni')
    groupement = SelectField('Groupement', id='groupement')
    village = SelectField('Village', id='village')
    poincon = StringField('Poincon', id='poincon')
    ancienCode = StringField('Ancien Code', id='ancienCode')

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
