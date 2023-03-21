# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for,flash
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
from apps.farmer.forms import *

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
        return render_template('farmer/list.html', segment='producteur', num=num, content=content)
    except Exception as e:
        print('> Error: /farmer: index Exception: ' + str(e))

# uploading excell file function


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
                jdata = data.to_dict('records')

        return render_template('farmer/upload.html', segment='producteur-upload', data=jdata, head=head)
    except Exception as e:
        print('> Error: /farmer: upload Exception: ' + str(e))


@ blueprint.route('/view/<id>', methods=['GET'])
@ login_required
def view(id):
    try:
        content = db.session.query(Farmer).get(id)

        return render_template('farmer/view.html', segment='producteur-view', content=content)

    except Exception as e:
        print('> Error: /farmer: view Exception: ' + str(e))


@blueprint.route('/edit/<id>', methods=['GET'])
@login_required
def edit_farmer_profile(id):
    try:
        form = EditProfileForm()
        content = db.session.query(Farmer).get(id)

        form.village.choices = [(village.id, village.name)
                                for village in db.session.query(Village).all()]
        form.groupement.choices = [(groupement.id, groupement.code)
                                   for groupement in db.session.query(Groupement).all()]

        form.village.default = content.villageId
        form.groupement.default = content.groupementId
        form.genre.default = content.gender
        form.process()
        return render_template('farmer/edit-farmer.html', segment='producteur-view', content=content, form=form)
    except Exception as e:
        print('> Error: /farmer: edit_farmer_profile Exception: ' + str(e))


@blueprint.route('/edit/save/<id>', methods=['GET'])
@login_required
def save_farmer_profile(id):
    try:
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
        content.firstName = nom
        content.lastName = prenom
        content.gender = genre
        content.birthdate = date
        content.idNumber = cni
        content.groupementId = groupement
        content.villageId = village
        content.stamp = poincon
        content.ancienCode = ancienCode
        db.session.commit()
        flash(f'Farmer Profile updated successfully', 'success')
        return redirect('/farmer/view/'+str(id))
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
                return render_template('farmer/edit-farm.html', segment='producteur-view', content=p, farmer_id=farmer_id, id=id)

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
            # print(p.id)
            if str(p.id) == str(id):
                p.name = nom
                p.description = details
                p.overallSize = surface
                p.totalPlants = plants
                p.productivePlants = plantsProductives
                p.averageAge = ageMoyen
                p.estimatedProduction = productionEstimée
                p.estimated_VRAC = productionEstiméeVrac
                if str(statut) == 'True':
                    p.inspected = 1
                else:
                    p.inspected = 0

        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /farmer-profile-edit-save: index Exception: ' + str(e))
        return str(e)

# Errors


@ login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@ blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@ blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@ blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
