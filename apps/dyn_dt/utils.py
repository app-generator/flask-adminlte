# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import importlib
from sqlalchemy import or_
from sqlalchemy import DateTime, func
from apps import db 

class PageItems(db.Model):
    __tablename__ = 'page_items'
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.String(255), nullable=True)
    items_per_page = db.Column(db.Integer, default=25)


class HideShowFilter(db.Model):
    __tablename__ = 'hide_show_filter'
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.String(255), nullable=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Boolean, default=False)


class ModelFilter(db.Model):
    __tablename__ = 'model_filter'
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.String(255), nullable=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255), nullable=False)


def get_model_fk_values(aModelClass):
    fk_values = {}

    current_table_name = aModelClass.__tablename__

    for relationship in aModelClass.__mapper__.relationships:
        if relationship.direction.name == 'MANYTOONE':
            related_model = relationship.mapper.class_
            foreign_key_column = list(relationship.local_columns)[0]
            referenced_table_name = list(foreign_key_column.foreign_keys)[0].column.table.name

            if referenced_table_name != current_table_name:
                field_name = relationship.key
                related_instances = related_model.query.all()
                fk_values[field_name] = related_instances

    return fk_values


def get_model_field_names(model, field_type):
    """Returns a list of field names based on the given field type in SQLAlchemy."""
    return [
        column.name for column in model.__table__.columns
        if isinstance(column.type, field_type)
    ]


def name_to_class(name: str):
    try:
        module_name = '.'.join(name.split('.')[:-1])
        class_name = name.split('.')[-1]

        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    except Exception as e:
        print(f"Error importing {name}: {e}")
        return None


def user_filter(request, query, fields, fk_fields=[]):
    value = request.args.get('search')

    if value:
        dynamic_filter = []

        for field in fields:
            if field not in fk_fields:
                dynamic_filter.append(getattr(query.column_descriptions[0]['entity'], field).ilike(f"%{value}%"))

        query = query.filter(or_(*dynamic_filter))

    return query


def exclude_auto_gen_fields(aModelClass):
    exclude_fields = [
        field.name for field in aModelClass.__table__.columns 
        if isinstance(field.type, DateTime) and (
            field.default is not None or
            field.server_default is not None or
            field.onupdate is not None or
            isinstance(field.default, func) or
            isinstance(field.onupdate, func)
        )
    ]
    return exclude_fields
