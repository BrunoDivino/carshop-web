from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, BooleanField, SelectField

class FormClient(FlaskForm):
    cpf = StringField('CPF', [validators.DataRequired(), validators.Length(11)])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=100)])
    is_opportunity = BooleanField('Is Opportunity?', default="checked")
    save = SubmitField('Save')

class FormCar(FlaskForm):
    id = StringField('ID', [validators.DataRequired(), validators.Length(min=1, max=8)])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    owner_cpf = StringField("Owner's CPF", [validators.DataRequired(), validators.Length(11)])
    color = SelectField('Color', choices=[('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Gray', 'Gray')])
    model = SelectField('Model', choices=[('Hatch', 'Hatch'), ('Sedan', 'Sedan'), ('Convertible', 'Convertible')])
    save = SubmitField('Save')
