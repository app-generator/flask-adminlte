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
from apps.farm import blueprint
from apps.farm.models import Farm


@blueprint.route('/')
@login_required
def index():
    try:
        content = db.session.query(Farm).all()
        num = 0
        for c in content:
            num += 1
        # print(num)
        return render_template('farm/list.html', segment='farm', num=num, content=content)
    except Exception as e:
        print('> Error: /farm: index Exception: ' + str(e))
    

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
