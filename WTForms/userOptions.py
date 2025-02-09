from flask_wtf import FlaskForm
from wtforms import SubmitField


class UserOptions(FlaskForm):
    openAccount = SubmitField("Open Account")
    closeAccount = SubmitField("Close Account")
    deposit = SubmitField("Deposit Funds")
    withdraw = SubmitField("Withdraw Funds")
    transfer = SubmitField("Transfer Funds")