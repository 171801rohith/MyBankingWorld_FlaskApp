from flask import render_template, session, redirect, url_for, flash
from app import app, mongodb

from services.account_manager import AccountManager
from WTForms.userOptions import UserOptions
from WTForms.homePage import Options


@app.route("/")
def index():
    return render_template("layout.html", options=Options())


@app.route("/userOptionsIndex", methods=["POST", "GET"])
def userOptionsIndex():
    if "emailID" in session:
        return render_template(
            "userOptions.html",
            email=session.get("emailID"),
            userOptions=UserOptions(),
        )
    return redirect(url_for("UserIndex"))


@app.route("/viewAcc", methods=["POST", "GET"])
def view_all_my_accounts():
    if "emailID" in session:
        accounts = AccountManager().view_all_my_accounts(session.get("emailID"))
        if accounts is False:
            flash(f"You have no accounts to view. Open an Account.")
        else:
            return render_template("viewAllAccounts.html", accounts=accounts)
    return redirect(url_for("userOptionsIndex"))


@app.route("/logout", methods=["POST", "GET"])
def userLogout():
    if "emailID" in session:
        session.pop("emailID")
        flash("Logged Out Successfully")
    return redirect(url_for("userOptionsIndex"))
