from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import Email, DataRequired, InputRequired


class SignupForm(FlaskForm):
    name = StringField("NAME :", validators=[DataRequired()])
    emailID = EmailField("EMAIL ID :", validators=[DataRequired(), Email()])
    password = PasswordField("PASSWORD :", validators=[InputRequired()])
    submit = SubmitField("SUBMIT")
