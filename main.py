from app import app, mongodb
from admin.admin import admin
from routes import home, login, signin, openAccount, closeAccount, validations

if __name__ == "__main__":
    app.run(debug=True)
