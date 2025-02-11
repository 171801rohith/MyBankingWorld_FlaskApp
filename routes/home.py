from flask import render_template, session
from app import app, mongodb
from WTForms.homePage import Options

from WTForms.userOptions import UserOptions


@app.route("/")
def index():
    return render_template("layout.html", options=Options())


@app.route("/userOptionsIndex")
def userOptionsIndex():
    if "emailID" in session:
        return render_template(
            "userOptions.html",
            email=session.get("emailID"),
            userOptions=UserOptions(),
        )