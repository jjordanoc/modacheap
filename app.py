# Imports
from cmath import e
import json
import sys
import os
import uuid
from flask import Flask, redirect, request, render_template, jsonify, abort, url_for
from models import db, Producto, Usuario, Imagen
from flask_migrate import Migrate
from flask_login import login_required, LoginManager, login_user, current_user, logout_user
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import unittest
import requests
# Config
load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER")
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/usuario/login"


# Models
@login_manager.user_loader
def load_user(correo):
    return Usuario.query.get(correo)

@app.route("/usuario/login", methods=["GET", "POST"])
def usuario_login():
    res = {}
    if request.method == "POST":
        try:
            data = request.json
            correo = data["correo"]
            clave = data["clave"]
            usuario = load_user(correo)
            print(usuario)
            if not usuario or not usuario.check_clave(clave):
                return redirect(url_for("usuario_login"))
            login_user(usuario, remember=True)
            res["status"] = "success"
            return jsonify(res)
        except Exception as e:
            print(e)
            abort(500)

    return render_template("login.html")

@app.route("/usuario/logout")
def usuario_logout():
    logout_user()
    return redirect(url_for("usuario_login"))

# Controllers
@app.route("/")
@login_required
def index():
    return render_template("index.html", productos=Producto.query.all(), usuario=current_user)

def test2(self):
    API_URL = "http://127.0.0.1:5000"
    REGISTER_URL = "{}/producto/crear".format(API_URL)
    r = request.get(REGISTER_URL)
    self.assertEqual("HOal"!=r)
    print("la")

@app.route("/usuario/registrar", methods=["GET", "POST"])
def usuario_registrar():
    if request.method == "POST":
        try:
            data = request.get_json()
            correo = data["correo"]
            clave = data["clave"]
            nombre = data["nombre"]
            celular = data["celular"]
            user = Usuario(correo=correo, nombre=nombre, celular=celular)
            print(user)
            user.set_clave(clave)
            db.session.add(user)
            db.session.commit()
            login_user(user.correo)
            res["status"] = "success"
            return jsonify(res)
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(500)
        finally:
            db.session.close()

    return render_template("register.html")


@app.route("/producto/crear" , methods=['POST'])
def producto_crear():

    error = False
    response = {}
    try:
        data = request.get_json()
        id = data['id']
        correo = data['correo']
        precio = data['precio']
        descripcion = data['descripcion']
        talla = data['talla']
        sexo = data['sexo']
        categoria = data['categoria']
        distrito = data['distrito']
        imagenes = request.files.getlist("imagenes")
        for imagen in imagenes:
            img_id = uuid.uuid4()
            imagen.save(os.path.join(app.config["UPLOAD_FOLDER"], img_id))
            db.session.add(Imagen(id=img_id))
        producto = Producto (
            id = id,
            correo = correo,
            precio = precio,
            descripcion = descripcion,
            talla = talla,
            sexo = sexo,
            categoria = categoria,
            distrito = distrito
        )
        db.session.add(producto)
        db.session.commit()
        response = {
            'id' : id,
            'correo' : correo,
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


@app.errorhandler(404)
def handle_not_found(error):
    return redirect(url_for("usuario_login"))

# Run
if __name__ == "__main__":
    app.run(debug=True, port=5000)

    
