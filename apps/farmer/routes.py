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
from apps.farmer import blueprint
from apps.farmer.models import Farmer
from apps.farm.models import Farm
from apps.configuration.models import Groupement, Village

import pandas as pd


@blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    try:
        content = db.session.query(Farmer).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('farmer/list.html', segment='farmer', num=num, content=content)
    except Exception as e:
        print('> Error: /farmer: index Exception: ' + str(e))


@blueprint.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    try:
        if request.method == 'POST':
            file = request.files['upload_file']
            if file:
                data = pd.read_excel(file)
                # get table head from keys
                head = list(data.to_dict('list').keys())
                # get table row from values
                Jdata = list(data.to_dict('list').values())
                i = 0
                for j in Jdata[0]:
                    print('row'+str(i)+''+str(j))
                    i += 1
                print(Jdata[0])
        return render_template('farmer/upload.html', segment='farmer', head=head, data=Jdata)
        content = db.session.query(Farmer).get(id)

        return render_template('farmer/view.html', segment='farmer-view', content=content)
    except Exception as e:
        print('> Error: /farmer: upload Exception: ' + str(e))


@blueprint.route('/view/<id>', methods=['GET'])
@login_required
def view(id):
    try:
        content = db.session.query(Farmer).get(id)

        return render_template('farmer/view.html', segment='farmer-view', content=content)

    except Exception as e:
        print('> Error: /farmer: view Exception: ' + str(e))


@blueprint.route('/edit/<id>', methods=['GET'])
@login_required
def edit_farmer_profile(id):
    try:
        content = db.session.query(Farmer).get(id)
        groupement = db.session.query(Groupement).all()
        village = db.session.query(Village).all()
        return render_template('farmer/edit-farmer.html', segment='farmer-view', content=content, village=village, groupement=groupement)
    except Exception as e:
        print('> Error: /farmer: edit_farmer_profile Exception: ' + str(e))


@blueprint.route('/edit/save/<id>', methods=['GET'])
@login_required
def save_farmer_profile(id):
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

        content = db.session.query(Farmer).get(id)
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
        print('> Error: /farmer: save_farmer_profile Exception: ' + str(e))
        return str(e)


@blueprint.route('/<farmer_id>/farm/edit/<id>', methods=['GET'])
@login_required
def edit_farmer_farm(farmer_id, id):
    try:
        content = db.session.query(Farmer).get(farmer_id)
        farms = content.farms

        for p in farms:
            if str(p.id) == str(id):
                return render_template('farmer/edit-farm.html', segment='farmer-view', content=p, farmer_id=farmer_id, id=id)

    except Exception as e:
        print('> Error: /farmer: Edit farmer Exception: ' + str(e))


# def edit_farmer_farm(id):
#     try:
#         content = db.session.query(Farmer).get(id)
#         print(content)
#         return render_template('farmer/edit-farm.html', segment='farmer-view', content=content)

#     except Exception as e:
#         print('> Error: /farmer: index Exception: ' + str(e))

@blueprint.route('/<farmer_id>/farm/edit/save/<id>', methods=['GET'])
@login_required
def save_farmer_farm(farmer_id, id):
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

        print('nom farm '+nom)

        content = db.session.query(Farmer).get(farmer_id)

        for p in content.farms:
            if str(p.id) == str(id):
                p.nomFarm = nom
                p.descriptionFarm = details
                p.surface = surface
                p.totalPlants = plants
                p.plantsProductives = plantsProductives
                p.ageMoyenPlants = ageMoyen
                p.estimationProduction = productionEstimée
                p.estimation_VRAC = productionEstiméeVrac
                p.statutFarm = statut

        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /farmer-profile-edit-save: index Exception: ' + str(e))
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
