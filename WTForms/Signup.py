from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import Email, DataRequired, InputRequired, Regexp


class SignupForm(FlaskForm):
    name = StringField(
        "NAME :",
        validators=[
            DataRequired(),
            Regexp(r"^[a-zA-Z\s]+$", message="Only letters and spaces are allowed."),
        ],
    )
    emailID = EmailField("EMAIL ID :", validators=[DataRequired(), Email()])
    password = PasswordField("PASSWORD :", validators=[InputRequired()])
    submit = SubmitField("SUBMIT")
