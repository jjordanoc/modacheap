# Imports
from crypt import methods
import json
import sys
from urllib import response
from flask import Flask, redirect, request, render_template, jsonify, abort, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
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



# Controllers
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            data = request.json
            username = data["username"]
            password = data["password"]
            user = Usuario(usuario=username)
            print(user)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            load_user(user.usuario)
            return redirect(url_for("index"))
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(500)
        finally:
            db.session.close()

    return render_template("register.html")


#Cambiar route
@app.route("/producto/create" , methods=['POST'])
#Cambiar def
def create_ropa():
    error = False
    response = {}
    try:
        id = request.get_json()['id']
        usuario = request.get_json()['usuario']
        precio = request.get_json()['precio']
        descripcion = request.get_json()['descripcion']
        talla = request.get_json()['talla']
        sexo = request.get_json()['sexo']
        categoria = request.get_json()['categoria']
        distrito = request.get_json()['distrito']
        productos = Producto (
            id = id,
            usuario = usuario,
            precio = precio,
            descripcion = descripcion,
            talla = talla,
            sexo = sexo,
            categoria = categoria,
            distrito = distrito
        )
        db.session.add(productos)
        db.session.commit()
        response = {
            'id' : id,
            'usuario' : usuario,
            'precio' : precio,
            'descripcion' : descripcion,
            'talla' : talla,
            'sexo' : sexo,
            'categoria' : categoria,
            'distrito' : distrito
        }
    except Exception as e :
        error=True
        print(e)
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(response)




# Run
if __name__ == "__main__":
    app.run(debug=True, port=5000)