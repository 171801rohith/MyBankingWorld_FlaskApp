from flask_wtf import FlaskForm
from wtforms import SubmitField

class Options(FlaskForm):
    admin = SubmitField("Go To Admin Login")
    user = SubmitField("Go To User Login")
    