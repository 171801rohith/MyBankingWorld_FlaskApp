from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange 

class IsActiveForm(FlaskForm):
    acc_no = IntegerField("ACCOUNT NUMBER", validators=[DataRequired(), NumberRange(min=10000)])
    check = SubmitField("CHECK")