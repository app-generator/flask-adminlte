# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from ..models import *
from apps import create_app, db
from sqlalchemy import select


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/district/view')
@login_required
def viewDistrict():
    content = db.session.query(District).all()
    num = 0
    for c in content:
        num += 1
    print(num)
    return render_template('home/list-district.html', segment='index', num=num, content=content)


@blueprint.route('/district/edit', methods=['GET'])
@login_required
def editDistrict():
    id = request.args.get('id')
    content = db.session.query(District).get(id)
    return render_template('home/edit-district.html', segment='index', id=id, content=content)


@blueprint.route('/district/saveUpdate', methods=['GET'])
@login_required
def updateDistrict():
    id = request.args.get('id')
    code = request.args.get('code')
    name = request.args.get('name')

    content = db.session.query(District).get(id)
    content.code = code
    content.name = name
    db.session.commit()
    return json.dumps({'status': 'ok'})


@blueprint.route('/<template>')
@login_required
def route_template(template):
    page = template.split('.')
    print(page[0])

    if page[0] == 'list-commune':
        content = db.session.query(Commune).all()
    if page[0] == 'list-fokontany':
        content = db.session.query(Fokontany).all()
    if page[0] == 'list-village':
        content = db.session.query(Village).all()
    if page[0] == 'list-groupement':
        content = db.session.query(Groupement).all()
    if page[0] == 'list-producteur':
        content = db.session.query(Producteur).all()
    if page[0] == 'list-campagne':
        content = db.session.query(Campagne).all()
    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, num=num, content=content)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
