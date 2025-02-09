from flask import Blueprint, render_template, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

from WTForms.login import LoginForm
from WTForms.signup import SignupForm
from WTForms.privileges import PrivilegesForm

admin = Blueprint(
    "admin", __name__, static_folder="static", template_folder="templates"
)
admin.permanent_session_lifetime = timedelta(minutes=30)


@admin.route("/", methods=["POST", "GET"])
def adminIndex():
    return render_template("adminLogin.html", adminLoginForm=LoginForm())


@admin.route("/signup", methods=["POST", "GET"])
def adminSignup():
    return render_template("adminSignup.html", adminSignupForm=SignupForm())


@admin.route("/signin", methods=["POST", "GET"])
def adminSignin():
    from app import mongodb

    adminSignupForm = SignupForm()
    if adminSignupForm.validate_on_submit():
        name = adminSignupForm.name.data
        emailID = adminSignupForm.emailID.data
        password = generate_password_hash(adminSignupForm.password.data)

        adminSignupForm.name.data = ""
        adminSignupForm.emailID.data = ""
        adminSignupForm.password.data = ""
        
        if mongodb.Admins.find_one({"EmailID": emailID}):
            flash("EmailID Already Exists. Try to Login with your Password.")
            return redirect(url_for("admin.adminIndex"))
        else:
            mongodb.Admins.insert_one(
                {"Name": name, "EmailID": emailID, "Password": password}
            )
            flash(f"Admin Added Successfully. Your EmailID - {emailID}.")
            return redirect(url_for("admin.adminIndex"))


@admin.route("/login", methods=["POST", "GET"])
def adminLogin():
    from app import mongodb

    adminLoginForm = LoginForm()
    if adminLoginForm.validate_on_submit():
        emailID = adminLoginForm.emailID.data
        password = adminLoginForm.password.data

        adminLoginForm.emailID.data = ""
        adminLoginForm.password.data = ""

        adminUser = mongodb.Admins.find_one({"EmailID": emailID})
        if adminUser and check_password_hash(adminUser["Password"], password):
            session.permanent = True
            session["emailID"] = emailID
            return render_template("adminOptions.html")
        else:
            flash(
                f"Your EmailID - {emailID} not found in Database or Recheck your Password."
            )
            return redirect(url_for("admin.adminIndex"))


@admin.route("/privilege", methods=["POST", "GET"])
def privilege():
    return render_template("changePrivilege.html", privilegesForm=PrivilegesForm())


@admin.route("/changePrivilege", methods=["POST", "GET"])
def changePrivilegeValues():
    from app import mongodb

    privilegesForm = PrivilegesForm()
    if privilegesForm.validate_on_submit():
        premium = privilegesForm.premium.data
        gold = privilegesForm.gold.data
        silver = privilegesForm.silver.data

        mongodb.Privileges.update_one(
            {},
            {"$set": {"GOLD": gold, "SILVER": silver, "PREMIUM": premium}},
            upsert=False,
        )
        flash(f"Privileges Updated Successfully.")

    return render_template("adminOptions.html")
