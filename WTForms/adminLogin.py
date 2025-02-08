from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired

class AdminLoginForm(FlaskForm):
    emailID = EmailField("EMAIL ID : ", validators=[DataRequired(), Email()])
    password = PasswordField("PASSWORD : ", validators=[InputRequired()])
    login = SubmitField("LOGIN")
    signup = SubmitField("SIGNUP")