from flask_wtf import FlaskForm
from wtforms import PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class CloseAccForm(FlaskForm):
    acc_no = IntegerField(
        "ACCOUNT NUMBER :", validators=[DataRequired(), NumberRange(min=10000)]
    )
    pin_no = PasswordField("PIN NUMBER :", validators=[InputRequired()])
    confirm = SubmitField("CONFIRM")
