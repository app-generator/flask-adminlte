from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, length


class EditDistrictForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()], id='code')
    name = StringField('Name',  validators=[DataRequired()], id='name')

    submit = SubmitField('Save', id='save_district')


class EditCommuneForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()], id='code')
    name = StringField('Name',  validators=[DataRequired()], id='name')
    district = SelectField('District',  validators=[
                           DataRequired()], id='district')

    submit = SubmitField('Save', id='save_commune')


class EditFokontanyForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()], id='code')
    name = StringField('Name',  validators=[DataRequired()], id='name')
    commune = SelectField('Commune',  validators=[
        DataRequired()], id='commune')

    submit = SubmitField('Save', id='save_fokontany')


class EditVillageForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()], id='code')
    name = StringField('Name',  validators=[DataRequired()], id='name')
    fokontany = SelectField('Fokontany',  validators=[
        DataRequired()], id='fokontany')

    submit = SubmitField('Save', id='save_village')


class EditGroupementForm(FlaskForm):
    Gtype = StringField('Gtype', validators=[DataRequired()], id='Gtype')
    code = StringField('Code', validators=[DataRequired()], id='code')
    name = StringField('Name',  validators=[DataRequired()], id='name')
    village = SelectField('Village',  validators=[
        DataRequired()], id='village')

    submit = SubmitField('Save', id='save_groupement')
