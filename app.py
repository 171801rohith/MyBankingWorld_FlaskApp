from flask import Flask
from flask_pymongo import PyMongo
from admin.admin import admin
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")
app.config["MONGO_URI"] = "mongodb://localhost:27017/MyBankingWorld"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.permanent_session_lifetime = timedelta(minutes=30)
mongodb = PyMongo(app).db
