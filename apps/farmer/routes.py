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

from apps import db, login_manager
from apps.farmer import blueprint
from apps.farmer.models import Farmer
from apps.configuration.models import Groupement
from apps.configuration.models import Village


@blueprint.route('/')
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


@blueprint.route('/view/<id>', methods=['GET'])
@login_required
def view(id):
    try:
        content = db.session.query(Farmer).get(id)

        return render_template('farmer/view.html', segment='farmer-view', content=content)
    except Exception as e:
        print('> Error: /farmer: index Exception: ' + str(e))


@blueprint.route('/parcelle/edit/<id>', methods=['GET'])
@login_required
def edit_farmer_parcelle(id):
    try:
        content = db.session.query(Farmer).get(id)
        print(content)
        return render_template('farmer/edit-parcelle.html', segment='farmer-view', content=content)
    except Exception as e:
        print('> Error: /farmer: index Exception: ' + str(e))


@blueprint.route('/profile/edit/<id>', methods=['GET'])
@login_required
def edit_farmer_profile(id):
    try:
        content = db.session.query(Farmer).get(id)
        groupement = db.session.query(Groupement).all()
        village = db.session.query(Village).all()
        return render_template('farmer/edit-profile.html', segment='farmer-view', content=content, village=village, groupement=groupement)
    except Exception as e:
        print('> Error: /farmer: index Exception: ' + str(e))

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
