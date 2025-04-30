# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json, csv, io
from flask_login import login_required
from apps.dyn_dt import blueprint
from flask import render_template, request, redirect, url_for, jsonify, make_response
from apps.dyn_dt.utils import get_model_field_names, get_model_fk_values, name_to_class, user_filter, exclude_auto_gen_fields
from apps import db, config
from apps.dyn_dt.utils import *
from sqlalchemy import and_
from sqlalchemy import Integer, DateTime, String, Text
from datetime import datetime

@blueprint.route('/dynamic-dt')
def dynamic_dt():
    context = {
        'routes': config.Config.DYNAMIC_DATATB.keys(),
        'segment': 'dynamic_dt',
        'parent': 'apps'
    }
    return render_template('dyn_dt/index.html', **context)

@blueprint.route('/create_filter/<model_name>', methods=["POST"])
def create_filter(model_name):
    model_name = model_name.lower()
    if request.method == "POST":
        keys = request.form.getlist('key')
        values = request.form.getlist('value')
        
        for key, value in zip(keys, values):
            filter_instance = ModelFilter.query.filter_by(parent=model_name, key=key).first()
            if filter_instance:
                filter_instance.value = value
            else:
                filter_instance = ModelFilter(parent=model_name, key=key, value=value)
            db.session.add(filter_instance)
        
        db.session.commit()
        return redirect(url_for('table_blueprint.model_dt', aPath=model_name))


@blueprint.route('/create_page_items/<model_name>', methods=["POST"])
def create_page_items(model_name):
    model_name = model_name.lower()
    if request.method == 'POST':
        items = request.form.get('items')
        page_items = PageItems.query.filter_by(parent=model_name).first()
        if page_items:
            page_items.items_per_page = items
        else:
            page_items = PageItems(parent=model_name, items_per_page=items)
        db.session.add(page_items)
        db.session.commit()
        return redirect(url_for('table_blueprint.model_dt', aPath=model_name))


@blueprint.route('/create_hide_show_filter/<model_name>', methods=["POST"])
def create_hide_show_filter(model_name):
    model_name = model_name.lower()
    if request.method == "POST":
        data_str = list(request.form.keys())[0]
        data = json.loads(data_str)

        filter_instance = HideShowFilter.query.filter_by(parent=model_name, key=data.get('key')).first()
        if filter_instance:
            filter_instance.value = data.get('value')
        else:
            filter_instance = HideShowFilter(parent=model_name, key=data.get('key'), value=data.get('value'))
        
        db.session.add(filter_instance)
        db.session.commit()

        return jsonify({'message': 'Model updated successfully'})


@blueprint.route('/delete_filter/<model_name>/<int:id>', methods=["GET"])
def delete_filter(model_name, id):
    model_name = model_name.lower()
    filter_instance = ModelFilter.query.filter_by(id=id, parent=model_name).first()
    if filter_instance:
        db.session.delete(filter_instance)
        db.session.commit()
        return redirect(url_for('table_blueprint.model_dt', aPath=model_name))
    return jsonify({'error': 'Filter not found'}), 404


@blueprint.route('/dynamic-dt/<aPath>', methods=['GET', 'POST'])
def model_dt(aPath):
    aModelName = None
    aModelClass = None

    if aPath in config.Config.DYNAMIC_DATATB.keys():
        aModelName = config.Config.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return f'ERR: Getting ModelClass for path: {aPath}', 404

    # db_fields = [field.name for field in aModelClass.__table__.columns]
    db_fields = [field.name for field in aModelClass.__table__.columns if not field.foreign_keys]
    fk_fields = get_model_fk_values(aModelClass)
    db_filters = []
    for f in db_fields:
        if f not in fk_fields.keys():
            db_filters.append( f )

    choices_dict = {}
    for column in aModelClass.__table__.columns:
        if isinstance(column.type, db.Enum):
            choices_dict[column.name] = [(choice.name, choice.value) for choice in column.type.enum_class]

    field_names = []
    for field_name in db_fields:
        field = HideShowFilter.query.filter_by(parent=aPath.lower(), key=field_name).first()
        if field:
            field_names.append(field)
        else:
            field = HideShowFilter(parent=aPath.lower(), key=field_name)
            db.session.add(field)
            db.session.commit()

            field_names.append(field)

    filter_string = []
    filter_instance = ModelFilter.query.filter_by(parent=aPath.lower()).all()
    for filter_data in filter_instance:
        if filter_data.key in db_fields:
            filter_string.append(getattr(aModelClass, filter_data.key).like(f"%{filter_data.value}%"))

    order_by = request.args.get('order_by', 'id')
    if order_by not in db_fields:
        order_by = 'id'

    queryset = aModelClass.query.filter(and_(*filter_string)).order_by(order_by)

    # Pagination
    page_items = PageItems.query.filter_by(parent=aPath.lower()).order_by(PageItems.id.desc()).first()
    p_items = 25
    if page_items:
        p_items = page_items.items_per_page

    page = request.args.get('page', 1, type=int)
    queryset = user_filter(request, queryset, db_fields, fk_fields.keys())
    pagination = queryset.paginate(page=page, per_page=p_items, error_out=False)
    items = pagination.items

    # Read-only and field types
    read_only_fields = ('id', 'user_id', 'date_created', 'date_modified', )
    integer_fields = get_model_field_names(aModelClass, Integer)
    date_time_fields = get_model_field_names(aModelClass, DateTime)
    text_fields = get_model_field_names(aModelClass, Text)
    email_fields = []

    # Context
    context = {
        'page_title': f'Dynamic DataTable - {aPath.lower().title()}',
        'link': aPath,
        'field_names': field_names,
        'db_field_names': db_fields,
        'db_filters': db_filters,
        'items': items,
        'pagination': pagination,
        'page_items': p_items,
        'filter_instance': filter_instance,
        'read_only_fields': read_only_fields,
        'integer_fields': integer_fields,
        'date_time_fields': date_time_fields,
        'email_fields': email_fields,
        'text_fields': text_fields,
        'fk_fields_keys': fk_fields.keys(),
        'fk_fields': fk_fields,
        'segment': 'dynamic_dt',
        'parent': 'apps',
        'choices_dict': choices_dict,
        'exclude_auto_gen_fields': exclude_auto_gen_fields(aModelClass)
    }
    return render_template('dyn_dt/model.html', **context)


@blueprint.route('/create/<aPath>', methods=["POST"])
@login_required
def create(aPath):
    aModelClass = None

    if aPath in config.Config.DYNAMIC_DATATB:
        aModelName = config.Config.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return ' > ERR: Getting ModelClass for path: ' + aPath

    if request.method == 'POST':
        data = {}
        fk_fields = get_model_fk_values(aModelClass)

        for attribute, value in request.form.items():
            if attribute in fk_fields.keys():
                table_name = None
                for product in fk_fields[attribute]:
                    table_name = product.__class__.__tablename__
                if table_name:
                    model_name = config.Config.DYNAMIC_DATATB[table_name]
                    value = name_to_class(model_name).query.filter_by(id=value).first()

            data[attribute] = value if value else ''

        new_item = aModelClass(**data)
        db.session.add(new_item)
        db.session.commit()

    return redirect(request.referrer) 


@blueprint.route('/delete/<aPath>/<id>', methods=["GET"])
@login_required
def delete(aPath, id):
    aModelClass = None

    if aPath in config.Config.DYNAMIC_DATATB:
        aModelName = config.Config.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return ' > ERR: Getting ModelClass for path: ' + aPath
    
    item = aModelClass.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()

    return redirect(request.referrer)


@blueprint.route('/update/<aPath>/<int:id>', methods=["POST"])
@login_required
def update(aPath, id):
    aModelClass = None

    if aPath in config.Config.DYNAMIC_DATATB:
        aModelName = config.Config.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return ' > ERR: Getting ModelClass for path: ' + aPath

    item = aModelClass.query.get(id)
    if not item:
        return 'Item not found', 404

    fk_fields = get_model_fk_values(aModelClass)

    if request.method == 'POST':
        for attribute, value in request.form.items():
            if hasattr(item, attribute) and getattr(item, attribute, value) is not None:
                if attribute in fk_fields.keys():
                    table_name = None
                    for product in fk_fields[attribute]:
                        table_name = product.__class__.__tablename__
                    if table_name:
                        model_name = config.Config.DYNAMIC_DATATB[table_name]
                        value = name_to_class(model_name).query.filter_by(id=value).first()

                setattr(item, attribute, value)
        
        db.session.commit()

    return redirect(request.referrer)


@blueprint.route('/export/<aPath>', methods=['GET'])
def export_csv(aPath):
    aModelName = None
    aModelClass = None

    if aPath in config.Config.DYNAMIC_DATATB:
        aModelName = config.Config.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return ' > ERR: Getting ModelClass for path: ' + aPath, 400

    db_field_names = [column.name for column in aModelClass.__table__.columns]
    fk_fields = get_model_fk_values(aModelClass)

    fields = []
    show_fields = HideShowFilter.query.filter_by(value=False, parent=aPath.lower()).all()
    for field in show_fields:
        if field.key in db_field_names:
            fields.append(field.key)
        else:
            print(f"Field {field.key} does not exist in {aModelClass} model.")


    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(fields)

    # Filtering
    filter_string = {}
    filter_instance = ModelFilter.query.filter_by(parent=aPath.lower()).all()
    for filter_data in filter_instance:
        filter_string[f'{filter_data.key}__icontains'] = filter_data.value

    # Ordering
    order_by = request.args.get('order_by', 'id')
    query = aModelClass.query.filter_by(**filter_string).order_by(order_by)
    items = user_filter(request, query, db_field_names, fk_fields)

    # Write rows to CSV
    for item in items:
        row_data = []
        for field in fields:
            try:
                row_data.append(getattr(item, field))
            except AttributeError:
                row_data.append('')
        writer.writerow(row_data)

    # Prepare response with CSV content
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = f'attachment; filename="{aPath.lower()}.csv"'

    return response


# Template filter

@blueprint.app_template_filter('getattribute')
def getattribute(value, arg):
    try:
        attr_value = getattr(value, arg)
        
        if isinstance(attr_value, datetime):
            return attr_value.strftime("%Y-%m-%d %H:%M:%S")
        
        return attr_value
    except AttributeError:
        return ''
    

@blueprint.app_template_filter('getenumattribute')
def getenumattribute(value, arg):
    try:
        attr_value = getattr(value, arg)
        return attr_value.value
    except AttributeError:
        return ''


@blueprint.app_template_filter('get')
def get(dict_data, key):
    return dict_data.get(key, [])
