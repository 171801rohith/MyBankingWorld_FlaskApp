from flask import render_template, flash, redirect, url_for, session, request
from app import app, mongodb
from werkzeug.security import check_password_hash
from repositories.account_repository import AccountRepository

from WTForms.openAccForm import OpenAccountForm


@app.route("/openAccForm", methods=["POST", "GET"])
def openAccForm():
    if "emailID" in session:
        return render_template("openAccForm.html", openAccForm=OpenAccountForm())


@app.route("/accForm", methods=["POST", "GET"])
def accForm():
    openAccForm = OpenAccountForm()
    type = openAccForm.account_type.data
    if type == "savings":
        return render_template("savAccForm.html", savAccForm=openAccForm)
    elif type == "current":
        return render_template("curAccForm.html", curAccForm=openAccForm)
