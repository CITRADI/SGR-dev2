from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class InteractionForm(FlaskForm):
    input_text = TextAreaField('Texto de entrada', validators=[DataRequired()])
    submit = SubmitField('Enviar')
