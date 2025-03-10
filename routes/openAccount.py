from flask import render_template, flash, redirect, url_for, session, request
from app import app, mongodb
from models.savings import Savings
from models.current import Current
from datetime import datetime
from exceptions.exceptions import BankExceptions

from WTForms.openAccForm import (
    SavingsAccountForm,
    CurrentAccountForm,
    AccountTypeForm,
)


@app.route("/openAccForm", methods=["POST", "GET"])
def openAccForm():
    if "emailID" in session:
        return render_template("openAccForm.html", openAccForm=AccountTypeForm())
    return redirect(url_for("UserIndex"))


@app.route("/accForm", methods=["POST", "GET"])
def accForm():
    accountTypeForm = AccountTypeForm()
    if accountTypeForm.validate_on_submit():
        type = accountTypeForm.account_type.data
        if type == "savings":
            return render_template("savAccForm.html", savAccForm=SavingsAccountForm())
        elif type == "current":
            return render_template("curAccForm.html", curAccForm=CurrentAccountForm())


@app.route("/savAccForm", methods=["POST", "GET"])
def savingsAcc():
    savAccForm = SavingsAccountForm()
    if savAccForm.validate_on_submit():
        age = int(datetime.now().strftime("%Y")) - int(
            savAccForm.date_of_birth.data.strftime("%Y")
        )
        if age < 18:
            flash(BankExceptions.ageLimit())
            return render_template("savAccForm.html", savAccForm=SavingsAccountForm())

        savings = Savings(
            savAccForm.name.data,
            session.get("emailID"),
            savAccForm.balance.data,
            savAccForm.pin_number.data,
            savAccForm.privilege.data,
            savAccForm.date_of_birth.data,
            savAccForm.gender.data,
            age,
        )

        savAccForm.name.data = ""
        savAccForm.balance.data = ""
        savAccForm.pin_number.data = ""
        savAccForm.privilege.data = ""
        savAccForm.date_of_birth.data = ""
        savAccForm.gender.data = ""

        if savings.store_in_mongodb():
            flash(
                f"Your Savings Account generated Successfully with Account_number - {savings.account_number}."
            )
            return redirect(url_for("userOptionsIndex"))
        else:
            flash(
                f"Sorry !! Due some reason your Account did not generate. Please Try Again"
            )
    else:
        flash(
            BankExceptions.pinLength()
            + BankExceptions.onlyLetters()
            + BankExceptions.insufficientInitialBalance()
        )
        return render_template("savAccForm.html", savAccForm=SavingsAccountForm())
    return redirect(url_for("userOptionsIndex"))


@app.route("/curAccForm", methods=["POST", "GET"])
def currentAcc():
    curAccForm = CurrentAccountForm()
    if curAccForm.validate_on_submit():
        current = Current(
            curAccForm.name.data,
            session.get("emailID"),
            curAccForm.balance.data,
            curAccForm.pin_number.data,
            curAccForm.privilege.data,
            curAccForm.reg_no.data,
            curAccForm.web_url.data,
        )

        curAccForm.name.data = ""
        curAccForm.balance.data = ""
        curAccForm.pin_number.data = ""
        curAccForm.privilege.data = ""
        curAccForm.web_url.data = ""
        curAccForm.reg_no.data = ""

        if current.store_in_mongodb():
            flash(
                f"Your Current Account generated Successfully with Account_number - {current.account_number}."
            )
            return redirect(url_for("userOptionsIndex"))
        else:
            flash(
                f"Sorry !! Due some reason your Account did not generate. Please Try Again"
            )
    else:
        flash(
            BankExceptions.pinLength()
            + BankExceptions.onlyLetters()
            + BankExceptions.insufficientInitialBalance()
        )
        return render_template("curAccForm.html", curAccForm=CurrentAccountForm())
    return redirect(url_for("userOptionsIndex"))
