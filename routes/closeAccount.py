from flask import render_template, flash, redirect, url_for, session, request
from app import app, mongodb

from services.account_manager import AccountManager
from exceptions.exceptions import BankExceptions
from WTForms.accNoPinNoForm import AccNoPinNoForm


@app.route("/closeAccForm", methods=["POST", "GET"])
def closeAccForm():
    if "emailID" in session:
        return render_template("closeAccForm.html", closeAccForm=AccNoPinNoForm())
    return redirect(url_for("UserIndex"))


@app.route("/closeAcc", methods=["POST", "GET"])
def closeAcc():
    closeAccForm = AccNoPinNoForm()
    if closeAccForm.validate_on_submit():
        AccountManager().close_account(
            closeAccForm.acc_no.data, session.get("emailID"), closeAccForm.pin_no.data
        )
    else:
        flash(BankExceptions.pinLength())
        return render_template("closeAccForm.html", closeAccForm=AccNoPinNoForm())
    return redirect(url_for("userOptionsIndex"))
