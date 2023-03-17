# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)
import json
from apps import db, login_manager
from apps.producteur import blueprint
from apps.producteur.models import Producteur
from apps.configuration.models import Groupement
from apps.configuration.models import Village

import pandas as pd


@blueprint.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    try:
        content = db.session.query(Producteur).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('producteur/list.html', segment='producteur', num=num, content=content)
    except Exception as e:
        print('> Error: /producteur: index Exception: ' + str(e))


@blueprint.route('/upload', methods=['GET', 'POST'])
# @login_required
def upload():
    try:
        if request.method == 'POST':
            file = request.files['upload_file']
            if file:
                data = pd.read_excel(file)

        return render_template('producteur/upload.html', segment='producteur', data=data.to_dict('list'))
    except Exception as e:
        print('> Error: /producteur: index Exception: ' + str(e))


@blueprint.route('/view/<id>', methods=['GET'])
@login_required
def view(id):
    try:
        content = db.session.query(Producteur).get(id)

        return render_template('producteur/view.html', segment='producteur-view', content=content)
    except Exception as e:
        print('> Error: /producteur: index Exception: ' + str(e))


@blueprint.route('/profile/edit/<id>', methods=['GET'])
@login_required
def edit_producteur_profile(id):
    try:
        content = db.session.query(Producteur).get(id)
        groupement = db.session.query(Groupement).all()
        village = db.session.query(Village).all()
        return render_template('producteur/edit-profile.html', segment='producteur-view', content=content, village=village, groupement=groupement)
    except Exception as e:
        print('> Error: /producteur: index Exception: ' + str(e))


@blueprint.route('/profile/edit/save/<id>', methods=['GET'])
@login_required
def save_producteur_profile(id):
    try:
        # id = request.args.get('id')
        nom = request.args.get('nom')
        prenom = request.args.get('prenom')
        genre = request.args.get('genre')
        date = request.args.get('date')
        cni = request.args.get('cni')
        groupement = request.args.get('groupement')
        village = request.args.get('village')
        poincon = request.args.get('poincon')
        ancienCode = request.args.get('ancienCode')

        content = db.session.query(Producteur).get(id)
        content.nom = nom
        content.prenom = prenom
        content.genre = genre
        content.date = date
        content.cni = cni
        content.groupement_id = groupement
        content.village_id = village
        content.poincon = poincon
        content.ancienCode = ancienCode
        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /producteur-profile-edit-save: index Exception: ' + str(e))
        return str(e)


@blueprint.route('/<prod_id>/parcelle/edit/<id>', methods=['GET'])
@login_required
def edit_producteur_parcelle(prod_id, id):
    try:
        content = db.session.query(Producteur).get(prod_id)
        parcelles = content.parcelles

        for p in parcelles:
            if str(p.id) == str(id):
                return render_template('producteur/edit-parcelle.html', segment='producteur-view', content=p, producteur_id=prod_id, id=id)

    except Exception as e:
        print('> Error: /producteur: index Exception: ' + str(e))


@blueprint.route('/<prod_id>/parcelle/edit/save/<id>', methods=['GET'])
@login_required
def save_producteur_parcelle(prod_id, id):
    try:
        nom = request.args.get('nom')
        details = request.args.get('details')
        surface = request.args.get('surface')
        plants = request.args.get('plants')
        plantsProductives = request.args.get('plantsProductives')
        ageMoyen = request.args.get('ageMoyen')
        productionEstimée = request.args.get('productionEstimée')
        productionEstiméeVrac = request.args.get('productionEstiméeVrac')
        statut = request.args.get('statut')

        print('nom parcelle '+nom)

        content = db.session.query(Producteur).get(prod_id)

        for p in content.parcelles:
            if str(p.id) == str(id):
                p.nomParcelle = nom
                p.descriptionParcelle = details
                p.surface = surface
                p.totalPlants = plants
                p.plantsProductives = plantsProductives
                p.ageMoyenPlants = ageMoyen
                p.estimationProduction = productionEstimée
                p.estimation_VRAC = productionEstiméeVrac
                p.statutParcelle = statut

        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /producteur-profile-edit-save: index Exception: ' + str(e))
        return str(e)

# Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
