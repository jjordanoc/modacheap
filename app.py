# Imports
import json
import sys
from flask import Flask, redirect, request, render_template, jsonify, abort, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import login_required, LoginManager, login_user
from models import *

# Config
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jjoc:1234@localhost:5432/modacheap"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


# Models
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@app.route("/login", methods=["GET", "POST"])
def login_usuario():
    if request.method == "POST":
        data = request.json
        nombre_usuario = data["usuario"]
        clave = data["clave"]
        nombre = data["nombre"]
        celular = data["celular"]
        usuario = load_user(nombre_usuario)
        print(usuario)
        if not usuario or not usuario.check_clave(clave):
            return redirect(url_for("login"))
        login_user(usuario, remember=True)
        return redirect(url_for("index"))   

    return render_template("login.html")


# Controllers
@app.route("/")
@login_required
def index():
    return render_template("index.html")



# Run
if __name__ == "__main__":
    app.run(debug=True, port=5000)