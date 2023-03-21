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
        form = EditGroupementForm()
        content = db.session.query(Groupement).get(id)

        form.village.choices = [(village.id, village.name)
                                for village in db.session.query(Village).all()]

        form.village.default = content.villageId
        form.process()
        return render_template('configuration/edit-groupement.html', segment='configuration-groupement', id=id, content=content, form=form)
    except Exception as e:
        print('> Error: /configuration-groupement: index Exception: ' + str(e))


@blueprint.route('/groupement/update/<id>', methods=['GET'])
@login_required
def updateGroupement(id):
    try:
        Gtype = request.args.get('Gtype')
        code = request.args.get('code')
        name = request.args.get('name')
        village = request.args.get('village')

        content = db.session.query(Groupement).get(id)
        content.type = Gtype
        content.code = code
        content.name = name
        content.villageId = village
        db.session.commit()
        flash(f'Groupement ' + str(id) + ' updated successfully', 'success')
        return redirect('/configuration/groupement')
    except Exception as e:
        print('> Error: /configuration-groupement: index Exception: ' + str(e))
        return str(e)

#  end of routes for groupement


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
        form = EditVillageForm()
        content = db.session.query(Village).get(id)

        form.fokontany.choices = [(fokontany.id, fokontany.name)
                                  for fokontany in db.session.query(Fokontany).all()]

        form.fokontany.default = content.fokontanyId
        form.process()

        return render_template('configuration/edit-village.html', segment='configuration-village', id=id, content=content, form=form)
    except Exception as e:
        print('> Error: /configuration-village: index Exception: ' + str(e))


@blueprint.route('/village/update/<id>', methods=['GET'])
@login_required
def updateVillage(id):
    try:
        code = request.args.get('code')
        name = request.args.get('name')
        fokontany = request.args.get('fokontany')

        content = db.session.query(Village).get(id)
        content.code = code
        content.name = name
        content.fokontanyId = fokontany
        db.session.commit()
        flash(f'Village ' + str(id) + ' updated successfully', 'success')
        return redirect('/configuration/village')
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
        form = EditFokontanyForm()
        content = db.session.query(Fokontany).get(id)

        form.commune.choices = [(commune.id, commune.name)
                                for commune in db.session.query(Commune).all()]

        form.commune.default = content.communeId
        form.process()

        return render_template('configuration/edit-fokontany.html', segment='configuration-fokontany', id=id, content=content, form=form)
    except Exception as e:
        print('> Error: /configuration-fokontany: index Exception: ' + str(e))


@blueprint.route('/fokontany/update/<id>', methods=['GET'])
@login_required
def updateFokontant(id):
    try:
        code = request.args.get('code')
        name = request.args.get('name')
        commune = request.args.get('commune')

        content = db.session.query(Fokontany).get(id)
        content.code = code
        content.name = name
        content.communeId = commune
        db.session.commit()
        flash(f'Fokontany ' + str(id) + ' updated successfully', 'success')
        return redirect('/configuration/fokontany')
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
        form = EditCommuneForm()
        content = db.session.query(Commune).get(id)

        form.district.choices = [(district.id, district.name)
                                 for district in db.session.query(District).all()]

        form.district.default = content.districtId
        form.process()
        return render_template('configuration/edit-commune.html', segment='configuration-commune', form=form, id=id, content=content)
    except Exception as e:
        print('> Error: /configuration-commune: index Exception: ' + str(e))


@blueprint.route('/commune/update/<id>', methods=['GET'])
@login_required
def updateCommune(id):
    try:
        code = request.args.get('code')
        name = request.args.get('name')
        district = request.args.get('district')

        content = db.session.query(Commune).get(id)
        content.code = code
        content.name = name
        content.districtId = district
        db.session.commit()
        flash(f'Commune ' + str(id) + ' updated successfully', 'success')
        return redirect('/configuration/commune')
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
