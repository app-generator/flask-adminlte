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
from apps.configuration import blueprint
from apps.configuration.models import *


@blueprint.route('/groupement')
@login_required
def list_groupement():
    try:
        content = db.session.query(Groupement).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('configuration/list-groupement.html', segment='configuration-groupement', num=num, content=content)
    except Exception as e:
        print('> Error: /configuration-groupement: index Exception: ' + str(e))



@blueprint.route('/campagne')
@login_required
def list_campagne():
    try:
        content = db.session.query(Campagne).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('configuration/list-campagne.html', segment='configuration-campagne', num=num, content=content)
    except Exception as e:
        print('> Error: /configuration-campagne: index Exception: ' + str(e))


@blueprint.route('/district')
@login_required
def list_district():
    try:
        content = db.session.query(District).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('configuration/list-district.html', segment='configuration-district', num=num, content=content)
    except Exception as e:
        print('> Error: /configuration-district: index Exception: ' + str(e))



@blueprint.route('/village')
@login_required
def list_village():
    try:
        content = db.session.query(Village).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('configuration/list-village.html', segment='configuration-village', num=num, content=content)
    except Exception as e:
        print('> Error: /configuration-village: index Exception: ' + str(e))



@blueprint.route('/fokontany')
@login_required
def list_fokontany():
    try:
        content = db.session.query(Fokontany).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('configuration/list-fokontany.html', segment='configuration-fokontany', num=num, content=content)
    except Exception as e:
        print('> Error: /configuration-fokontany: index Exception: ' + str(e))


@blueprint.route('/commune')
@login_required
def list_commune():
    try:
        content = db.session.query(Commune).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('configuration/list-commune.html', segment='configuration-commune', num=num, content=content)
    except Exception as e:
        print('> Error: /configuration-commune: index Exception: ' + str(e))
    

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
