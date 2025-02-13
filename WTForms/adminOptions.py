from flask_wtf import FlaskForm
from wtforms import SubmitField


class AdminOptions(FlaskForm):
    privilegeVal = SubmitField("Change Privileges Value")
    trans = SubmitField("View All Transactions")
    acc = SubmitField("View All Accounts")