from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    PasswordField,
    SubmitField,
    RadioField,
    StringField,
    DateField,
    URLField,
    IntegerField,
)
from wtforms.validators import DataRequired, Email, InputRequired, URL, NumberRange


class OpenAccountForm(FlaskForm):
    name = StringField("NAME :", validators=[DataRequired()])
    emailID = EmailField("EMAIL ID :", validators=[DataRequired(), Email()])
    pin_number = PasswordField("PIN NUMBER :", validators=[InputRequired()])
    account_type = RadioField(
        "SELECT ACCOUNT_TYPE :",
        choices=[("savings", "SAVINGS"), ("current", "CURRENT")],
        validators=[DataRequired()],
    )
    gender = RadioField(
        "SELECT GENDER :",
        choices=[("M", "MALE"), ("F", "FEMALE")],
        validators=[DataRequired()],
    )

    privilege = RadioField(
        "SELECT PRIVILEGE :",
        choices=[("premium", "PREMIUM"), ("gold", "GOLD"), ("silver", "SILVER")],
        validators=[DataRequired()],
    )
    date_of_birth = DateField(
        "DATE OF BIRTH :", format="%Y-%m-%d", validators=[DataRequired()]
    )
    age = IntegerField("AGE :", validators=[DataRequired(), NumberRange(min=18)])
    balance = IntegerField(
        "INITIAL BALANCE :", validators=[DataRequired(), NumberRange(min=1000)]
    )
    reg_no = IntegerField("REGISTRATION NUMBER:", validators=[DataRequired()])
    web_url = URLField("WEBSITE URL :", validators=[DataRequired(), URL()])
    submit = SubmitField("SUBMIT")
    next = SubmitField("NEXT")
