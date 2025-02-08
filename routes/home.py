from flask import render_template
from app import app, mongodb
from WTForms.homePage import Options 

@app.route("/")
def index():
    return render_template("layout.html", options=Options())