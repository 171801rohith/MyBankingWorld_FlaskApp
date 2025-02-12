from app import app, mongodb
from admin.admin import admin
from routes import home, login, signin, openAccount, closeAccount,deleteAccount, validations, transactions, transactionHistory

if __name__ == "__main__":
    app.run(debug=True)
