from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

class EditForm(FlaskForm):
  rating = FloatField('Rating', validators=[InputRequired()])
  review = StringField('Review', validators=[InputRequired()])
  submit = SubmitField('Submit')
