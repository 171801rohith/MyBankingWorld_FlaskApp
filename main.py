from app import app, mongodb
from routes import home, login
from admin.admin import admin

if __name__ == "__main__":
    app.run(debug=True)
