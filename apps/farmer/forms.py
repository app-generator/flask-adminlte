# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired


class EditProfileForm(FlaskForm):
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
