from flask import render_template, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash
from app import app, mongodb

from WTForms.signup import SignupForm
from exceptions.exceptions import BankExceptions


@app.route("/signup", methods=["POST", "GET"])
def UserSignupForm():
    return render_template("userSignup.html", userSignupForm=SignupForm())


@app.route("/signin", methods=["POST", "GET"])
def userSignin():
    userSignupForm = SignupForm()
    if userSignupForm.validate_on_submit():
        name = userSignupForm.name.data
        emailID = userSignupForm.emailID.data
        password = generate_password_hash(userSignupForm.password.data)

        userSignupForm.name.data = ""
        userSignupForm.emailID.data = ""
        userSignupForm.password.data = ""

        if mongodb.Admins.find_one({"EmailID": emailID}):
            flash(BankExceptions.emailAlreadyExists())

        else:
            mongodb.Users.insert_one(
                {"Name": name, "EmailID": emailID, "Password": password}
            )
            flash(f"User Added Successfully. Your EmailID - {emailID}.")
    else:
        flash(BankExceptions.onlyLetters())
        return render_template("userSignup.html", userSignupForm=SignupForm())
    return redirect(url_for("UserIndex"))
