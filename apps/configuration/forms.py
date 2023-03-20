from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class EditDistrictForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()], id='code')
    name = StringField('Name',  validators=[DataRequired()], id='name')
    submit = SubmitField('Save', id='save_district')
