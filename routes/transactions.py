from flask import render_template, flash, redirect, url_for, session
from app import app, mongodb

from services.transaction_manager import TransactionManager

from WTForms.transactionForm import DepositForm, WithdrawForm, TransferFundsForm


@app.route("/depositForm", methods=["POST", "GET"])
def depositForm():
    if "emailID" in session:
        return render_template("depositForm.html", depositForm=DepositForm())
    return redirect(url_for("UserIndex"))


@app.route("/withdrawForm", methods=["POST", "GET"])
def withdrawForm():
    if "emailID" in session:
        return render_template("withdrawForm.html", withdrawForm=WithdrawForm())
    return redirect(url_for("UserIndex"))


@app.route("/transferForm", methods=["POST", "GET"])
def transferForm():
    if "emailID" in session:
        return render_template("transferForm.html", transferForm=TransferFundsForm())
    return redirect(url_for("UserIndex"))


@app.route("/deposit", methods=["POST", "GET"])
def depositAmount():
    depositForm = DepositForm()
    if depositForm.validate_on_submit():
        TransactionManager().deposit_amount(
            depositForm.acc_no.data, depositForm.amount.data
        )
    return redirect(url_for("userOptionsIndex"))


@app.route("/withdraw", methods=["POST", "GET"])
def withdrawAmount():
    withdrawForm = WithdrawForm()
    if withdrawForm.validate_on_submit():
        TransactionManager().withdraw_amount(
            withdrawForm.acc_no.data, withdrawForm.pin_no.data, withdrawForm.amount.data
        )
    else:
        flash("Enter a valid 4 to 6 digits pin.")
        return render_template("withdrawForm.html", withdrawForm=WithdrawForm())
    return redirect(url_for("userOptionsIndex"))


@app.route("/transfer", methods=["POST", "GET"])
def transeferAmount():
    transferForm = TransferFundsForm()
    if transferForm.validate_on_submit():
        TransactionManager().transfer_amount(
            transferForm.acc_no.data,
            transferForm.to_acc_no.data,
            transferForm.pin_no.data,
            transferForm.amount.data,
        )
    else:
        flash("Enter a valid 4 to 6 digits pin.")
        return render_template("transferForm.html", transferForm=TransferFundsForm())
    return redirect(url_for("userOptionsIndex"))
