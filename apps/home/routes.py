# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, current_app
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps import db
import jwt
import time


@blueprint.route('/index')
@login_required
def index():

    payload = {
        "resource": {"dashboard": 3},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(
        payload, current_app.config["METABASE_SECRET_KEY"], algorithm="HS256")

    iframeUrl = current_app.config["METABASE_SITE_URL"] + \
        "/embed/dashboard/" + token + "#bordered=true&titled=true"
    return render_template('home/dashboard-campagne.html', segment='index', iframeUrl=iframeUrl)


@blueprint.route('/dashboard/campagne')
@login_required
def dashboard_campagne():

    payload = {
        "resource": {"dashboard": 3},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(
        payload, current_app.config["METABASE_SECRET_KEY"], algorithm="HS256")

    iframeUrl = current_app.config["METABASE_SITE_URL"] + \
        "/embed/dashboard/" + token + "#bordered=true&titled=true"

    return render_template('home/dashboard-campagne.html', segment='index', iframeUrl=iframeUrl)


@blueprint.route('/dashboard/producteur')
@login_required
def dashboard_producteur():

    payload = {
        "resource": {"dashboard": 4},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(
        payload, current_app.config["METABASE_SECRET_KEY"], algorithm="HS256")

    iframeUrl = current_app.config["METABASE_SITE_URL"] + \
        "/embed/dashboard/" + token + "#bordered=true&titled=true"
    return render_template('home/dashboard-producteur.html', segment='index', iframeUrl=iframeUrl)


@blueprint.route('/dashboard/bio')
@login_required
def dashboard_list_bio():

    payload = {
        "resource": {"question": 4},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(
        payload, current_app.config["METABASE_SECRET_KEY"], algorithm="HS256")

    iframeUrl = current_app.config["METABASE_SITE_URL"] + \
        "/embed/question/" + token + "#bordered=true&titled=true"
    return render_template('home/dashboard-liste-bio.html', segment='index', iframeUrl=iframeUrl)
