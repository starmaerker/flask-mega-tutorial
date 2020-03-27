from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateQuestion(FlaskForm):
    question = StringField('Frage', validators=[DataRequired()])
    solution = StringField('Lösung', validators=[DataRequired()])
    submit = SubmitField('Frage erstellen')
