from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class FindForm(FlaskForm):
  title = StringField('Title', validators=[InputRequired()])
  submit = SubmitField()
