from flask import render_template, flash, redirect, url_for, session
from app import app, mongodb
from services.account_manager import AccountManager

from WTForms.isActive import IsActiveForm


@app.route("/checkActive", methods=["POST", "GET"])
def isActForm():
    if "emailID" in session:
        return render_template("activityForm.html", isActiveForm=IsActiveForm())
    return redirect(url_for("UserIndex"))


@app.route("/isActive", methods=["POST", "GET"])
def isAct():
    isActiveForm = IsActiveForm()
    if isActiveForm.validate_on_submit():
        if (
            AccountManager().isActive(isActiveForm.acc_no.data, session.get("emailID"))
            is True
        ):
            flash(f"Your Account - {isActiveForm.acc_no.data} is Active.")
        elif (
            AccountManager().isActive(isActiveForm.acc_no.data, session.get("emailID"))
            is False
        ):
            flash(f"Your Account - {isActiveForm.acc_no.data} is Inactive.")

        isActiveForm.acc_no.data = ""
    return redirect(url_for("userOptionsIndex"))
