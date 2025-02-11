from flask import render_template, flash, redirect, url_for, session, request
from app import app, mongodb

from services.account_manager import AccountManager

from WTForms.accNoPinNoForm import AccNoPinNoForm


@app.route("/deleteAccForm", methods=["POST", "GET"])
def deleteAccForm():
    if "emailID" in session:
        return render_template("deleteAccForm.html", deleteAccForm=AccNoPinNoForm())
    return redirect(url_for("UserIndex"))


@app.route("/deleteAcc", methods=["POST", "GET"])
def deleteAcc():
    deleteAccForm = AccNoPinNoForm()
    if deleteAccForm.validate_on_submit():
        AccountManager().delete_account(
            deleteAccForm.acc_no.data, deleteAccForm.pin_no.data
        )
    return redirect(url_for("userOptionsIndex"))
