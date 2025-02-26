from flask_wtf import FlaskForm
from wtforms import PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp


class AccNoPinNoForm(FlaskForm):
    acc_no = IntegerField(
        "ACCOUNT NUMBER :", validators=[DataRequired(), NumberRange(min=10000)]
    )
    pin_no = PasswordField("PIN NUMBER :", validators=[InputRequired(), Regexp(r"^\d{4,6}$", message="Only 4 to 6 digits are allowed.")])
    confirm = SubmitField("CONFIRM")
