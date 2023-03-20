# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for, flash
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)
import json
from apps import db, login_manager
from apps.configuration import blueprint
from apps.configuration.models import *

# importing forms
from apps.configuration.forms import *
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()
# routes for groupement


@blueprint.route('/groupement')
@login_required
def list_groupement():
    try:
        content = db.session.query(Groupement).all()
        return render_template('configuration/list-groupement.html', segment='configuration-groupement', content=content)
    except Exception as e:
        print('> Error: /configuration-groupement: index Exception: ' + str(e))


@blueprint.route('/groupement/edit/<id>', methods=['GET'])
@login_required
def editGroupement(id):
    try:
        content = db.session.query(Groupement).get(id)
        village = db.session.query(Village).all()

        return render_template('configuration/edit-groupement.html', segment='configuration-groupement', id=id, content=content, village=village)
    except Exception as e:
        print('> Error: /configuration-groupement: index Exception: ' + str(e))


@blueprint.route('/groupement/update', methods=['GET'])
@login_required
def updateGroupement():
    try:
        id = request.args.get('id')
        Gtype = request.args.get('type')
        code = request.args.get('code')
        groupement = request.args.get('groupement')
        village = request.args.get('village')

        content = db.session.query(Groupement).get(id)
        content.type = Gtype
        content.code = code
        content.name = groupement
        content.villageId = village
        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /configuration-groupement: index Exception: ' + str(e))
        return str(e)

#  end of routes for districts


@blueprint.route('/season')
@login_required
def list_campagne():
    try:
        content = db.session.query(Season).all()
        return render_template('configuration/list-campagne.html', segment='configuration-season', content=content)
    except Exception as e:
        print('> Error: /configuration-season: index Exception: ' + str(e))

# routes for districts


@blueprint.route('/district')
@login_required
def list_district():
    try:
        content = db.session.query(District).all()
        return render_template('configuration/list-district.html', segment='configuration-district', content=content)
    except Exception as e:
        print('> Error: /configuration-district: index Exception: ' + str(e))


@blueprint.route('/district/edit/<id>', methods=['GET'])
@login_required
@csrf.exempt
def editDistrict(id):
    try:
        form = EditDistrictForm()
        content = db.session.query(District).get(id)

        if form.validate_on_submit():
            flash(f'District ' + str(id) + ' updated successfully', 'success')
            return redirect('/configuration/district')
        return render_template('configuration/edit-district.html', segment='configuration-district', form=form, id=id, content=content)
    except Exception as e:
        print('> Error: /configuration-district: index Exception: ' + str(e))


@blueprint.route('/district/update/<id>', methods=['GET'])
@login_required
def updateDistrict(id):
    try:
        code = request.args.get('code')
        name = request.args.get('name')

        content = db.session.query(District).get(id)
        content.code = code
        content.name = name
        db.session.commit()
        flash(f'District ' + str(id) + ' updated successfully', 'success')
        return redirect('/configuration/district')
    except Exception as e:
        print('> Error: /configuration-district: index Exception: ' + str(e))
        return str(e)
#  end of routes for districts

#  routes for village


@blueprint.route('/village')
@login_required
def list_village():
    try:
        content = db.session.query(Village).all()
        return render_template('configuration/list-village.html', segment='configuration-village', content=content)
    except Exception as e:
        print('> Error: /configuration-village: index Exception: ' + str(e))


@blueprint.route('/village/edit/<id>', methods=['GET'])
@login_required
def editVillage(id):
    try:
        content = db.session.query(Village).get(id)
        fokontany = db.session.query(Fokontany).all()

        return render_template('configuration/edit-village.html', segment='configuration-village', id=id, content=content, fokontany=fokontany)
    except Exception as e:
        print('> Error: /configuration-village: index Exception: ' + str(e))


@blueprint.route('/village/update', methods=['GET'])
@login_required
def updateVillage():
    try:
        id = request.args.get('id')
        code = request.args.get('code')
        name = request.args.get('name')
        fokontany = request.args.get('fokontany')

        content = db.session.query(Village).get(id)
        content.code = code
        content.name = name
        content.fokontanyId = fokontany
        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /configuration-fokontany: index Exception: ' + str(e))
        return str(e)

#  end of routes for village

#  routes for fokontany


@blueprint.route('/fokontany')
@login_required
def list_fokontany():
    try:
        content = db.session.query(Fokontany).all()
        return render_template('configuration/list-fokontany.html', segment='configuration-fokontany', content=content)
    except Exception as e:
        print('> Error: /configuration-fokontany: index Exception: ' + str(e))


@blueprint.route('/fokontany/edit/<id>', methods=['GET'])
@login_required
def editFokontant(id):
    try:
        content = db.session.query(Fokontany).get(id)
        commune = db.session.query(Commune).all()

        return render_template('configuration/edit-fokontany.html', segment='configuration-fokontany', id=id, content=content, commune=commune)
    except Exception as e:
        print('> Error: /configuration-fokontany: index Exception: ' + str(e))


@blueprint.route('/fokontany/update', methods=['GET'])
@login_required
def updateFokontant():
    try:
        id = request.args.get('id')
        code = request.args.get('code')
        name = request.args.get('name')
        commune = request.args.get('commune')

        content = db.session.query(Fokontany).get(id)
        content.code = code
        content.name = name
        content.communeId = commune
        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /configuration-fokontany: index Exception: ' + str(e))
        return str(e)
#  end of routes for fokontany

#  routes for commune


@blueprint.route('/commune')
@login_required
def list_commune():
    try:
        content = db.session.query(Commune).all()
        return render_template('configuration/list-commune.html', segment='configuration-commune', content=content)
    except Exception as e:
        print('> Error: /configuration-commune: index Exception: ' + str(e))


@blueprint.route('/commune/edit/<id>', methods=['GET'])
@login_required
def editCommune(id):
    try:
        content = db.session.query(Commune).get(id)
        district = db.session.query(District).all()

        return render_template('configuration/edit-commune.html', segment='configuration-commune', id=id, content=content, district=district)
    except Exception as e:
        print('> Error: /configuration-commune: index Exception: ' + str(e))


@blueprint.route('/commune/update', methods=['GET'])
@login_required
def updateCommune():
    try:
        id = request.args.get('id')
        code = request.args.get('code')
        name = request.args.get('name')
        district = request.args.get('district')

        content = db.session.query(Commune).get(id)
        content.code = code
        content.name = name
        content.districtId = district
        db.session.commit()
        return json.dumps({'status': 'true'})
    except Exception as e:
        print('> Error: /configuration-commune: index Exception: ' + str(e))
        return str(e)
#  end of routes for commune


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
