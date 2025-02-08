from flask import render_template
from app import app, mongodb
from WTForms.homePage import Options


@app.route("/login", methods=["POST", "GET"])
def UserLogin():
    return "<h1>Log</h1>"
