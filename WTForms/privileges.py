from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired 

class PrivilegesForm(FlaskForm):
    gold = IntegerField("GOLD", validators=[DataRequired()])
    premium = IntegerField("PREMIUM", validators=[DataRequired()])
    silver = IntegerField("SILVER", validators=[DataRequired()])
    confirm = SubmitField("Confirm Changes", validators=[DataRequired()])