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


@blueprint.route('/')
@login_required
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
        content.groupement.id = groupement
        content.village.id = village
        content.poincon = poincon
        content.ancienCode = ancienCode
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
