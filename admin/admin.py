from flask import Blueprint, render_template, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

from WTForms.login import LoginForm
from WTForms.signup import SignupForm
from WTForms.privileges import PrivilegesForm
from WTForms.adminOptions import AdminOptions
from WTForms.accNoPinNoForm import AccNoPinNoForm
from exceptions.exceptions import BankExceptions


admin = Blueprint(
    "admin", __name__, static_folder="static", template_folder="templates"
)
admin.permanent_session_lifetime = timedelta(minutes=30)


@admin.route("/", methods=["POST", "GET"])
def adminIndex():
    return render_template("adminLogin.html", adminLoginForm=LoginForm())


@admin.route("/adminOptionIndex", methods=["POST", "GET"])
def adminOptionsIndex():
    if "adminEmailID" in session:
        return render_template("adminOptions.html", adminOptions=AdminOptions())
    return redirect(url_for("admin.adminIndex"))


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
            flash(BankExceptions.emailAlreadyExists())
        else:
            mongodb.Admins.insert_one(
                {"Name": name, "EmailID": emailID, "Password": password}
            )
            flash(f"Admin Added Successfully. Your EmailID - {emailID}.")
    else:
        flash(BankExceptions.onlyLetters())
        return render_template("adminSignup.html", adminSignupForm=SignupForm())
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
            session["adminEmailID"] = emailID
            return redirect(url_for("admin.adminOptionsIndex"))
        else:
            flash(BankExceptions.emailNotInDB(emailID) + "Or Recheck your Password.")
            return redirect(url_for("admin.adminIndex"))


@admin.route("/privilege", methods=["POST", "GET"])
def privilege():
    if "adminEmailID" in session:
        return render_template("changePrivilege.html", privilegesForm=PrivilegesForm())
    return redirect(url_for("admin.adminOptionsIndex"))


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

    return redirect(url_for("admin.adminOptionsIndex"))


@admin.route("/transactionHistory", methods=["POST", "GET"])
def view_all_transactions():
    from app import mongodb

    if "adminEmailID" in session:
        transactions = list(mongodb.TransactionsHistory.find({}))
        if transactions:
            return render_template("transactionHistory.html", transactions=transactions)
        else:
            flash(f"No transactions available to view")
    return redirect(url_for("admin.adminOptionsIndex"))


@admin.route("/viewAcc", methods=["POST", "GET"])
def view_all_accounts():
    from app import mongodb

    if "adminEmailID" in session:
        accounts = mongodb.Accounts.find({})
        if accounts:
            return render_template("viewAllAccounts.html", accounts=list(accounts))
        else:
            flash(f"No Accounts available to view")
    return redirect(url_for("admin.adminOptionsIndex"))


@admin.route("/accReactivateForm", methods=["POST", "GET"])
def reactivateForm():
    if "adminEmailID" in session:
        return render_template("reactivateForm.html", reactForm=AccNoPinNoForm())
    return redirect(url_for("admin.adminOptionsIndex"))


@admin.route("/accReactivate", methods=["POST", "GET"])
def reactivateAcc():
    from app import mongodb

    reactForm = AccNoPinNoForm()
    acc_no = reactForm.acc_no.data
    pin_no = reactForm.pin_no.data

    if reactForm.validate_on_submit():
        reactForm.acc_no.data = ""
        reactForm.pin_no.data = ""
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        if account and check_password_hash(account["Pin_Number"], pin_no):
            if account["Activity"] == True:
                flash(f"This account - {acc_no} is already active.")
            else:
                mongodb.Accounts.update_one(
                    {"Account_Number": str(acc_no)},
                    {"$set": {"Activity": True, "Close_date": None}},
                )
                flash(f"Account successfully reactivated")
        else:
            flash(BankExceptions.accountNotInDB(acc_no) + BankExceptions.wrongPin())
    else:
        flash("Enter a valid 4 to 6 digits pin.")
        return render_template("reactivateForm.html", reactForm=AccNoPinNoForm())
    return redirect(url_for("admin.adminOptionsIndex"))


@admin.route("/logout", methods=["POST", "GET"])
def adminLogout():
    if "adminEmailID" in session:
        session.pop("adminEmailID")
        flash("Logged Out Successfully")
    return redirect(url_for("admin.adminOptionsIndex"))
