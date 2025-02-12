from flask_wtf import FlaskForm
from wtforms import PasswordField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class DepositForm(FlaskForm):
    acc_no = IntegerField(
        "ACCOUNT NUMBER :", validators=[DataRequired(), NumberRange(min=10000)]
    )
    amount = FloatField("AMOUNT : ₹", validators=[DataRequired(), NumberRange(min=1)])
    confirm = SubmitField("CONFIRM")


class WithdrawForm(DepositForm):
    pin_no = PasswordField("PIN NUMBER :", validators=[InputRequired()])


class TransferFundsForm(WithdrawForm):
    to_acc_no = IntegerField(
        "TO ACCOUNT NUMBER :", validators=[DataRequired(), NumberRange(min=10000)]
    )
