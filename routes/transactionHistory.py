from flask import render_template, flash, redirect, url_for, session
from app import app, mongodb

from services.transaction_manager import TransactionManager

from WTForms.accNoPinNoForm import AccNoPinNoForm


@app.route("/transactionHistForm", methods=["POST", "GET"])
def transacHistForm():
    if "emailID" in session:
        return render_template("transHitForm.html", transHitForm=AccNoPinNoForm())
    return redirect(url_for("UserIndex"))


@app.route("/transactionHistory", methods=["POST", "GET"])
def transHist():
    transHitForm = AccNoPinNoForm()
    if transHitForm.validate_on_submit():
        transactions = TransactionManager().view_all_my_transactions(
            transHitForm.acc_no.data, transHitForm.pin_no.data
        )
        if transactions is False:
            flash(
                f"No transactions done with your Account - {transHitForm.acc_no.data}"
            )
        else:
            return render_template("transactionHistory.html", transactions=transactions)
    else:
        flash("Enter a valid 4 to 6 digits pin.")
        return render_template("transHitForm.html", transHitForm=AccNoPinNoForm())
    return redirect(url_for("userOptionsIndex"))
