from flask import Flask
from flask_session import Session
from flask_pymongo import PyMongo
from admin.admin import admin
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_FILE_DIR"] = "./flask_session"
app.config["SESSION_KEY_PREFIX"] = "bank_"
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONNLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
mongodb = PyMongo(app).db
Session(app)
