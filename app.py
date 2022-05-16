# Imports
import sys
import os
from shortuuid import ShortUUID
from flask import Flask, redirect, request, render_template, jsonify, abort, url_for, send_from_directory, flash
from models import db, Producto, Usuario, Imagen
from flask_migrate import Migrate
from flask_login import login_required, LoginManager, login_user, current_user, logout_user
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException
from helpers import handle_error, handle_error_db
import unittest

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
login_manager.login_message = "Debe ingresar para acceder a esta pagina."
login_manager.login_message_category = "warning"

# Endpoints
@login_manager.user_loader
def load_user(correo):
    return Usuario.query.get(correo)


@app.route("/usuario/login", methods=["GET", "POST"])
def usuario_login():
    if request.method == "POST":
        res = {}
        try:
            data = request.json
            correo = data["correo"]
            clave = data["clave"]
            usuario = load_user(correo)
            print(usuario)
            if not usuario or not usuario.check_clave(clave):
                raise Exception("Usuario o clave incorrectos.")
            login_user(usuario, remember=True)
            res["status"] = "success"
            res["message"] = "Ingreso con exito."
        except Exception as e:
            res["status"] = "warning"
            res["message"] = "Usuario o clave incorrectos."
            handle_error(e)
        return jsonify(res)

    return render_template("login.html")

@app.route("/usuario/logout")
def usuario_logout():
    logout_user()
    flash("Usted ha cerrado su sesion.", "info")
    return redirect(url_for("usuario_login"))

# Controllers
@app.route("/")
def index():
    return render_template("index.html", productos=Producto.query.all(), usuario=current_user)


@app.route("/usuario/registrar", methods=["GET", "POST"])
def usuario_registrar():
    if request.method == "POST":
        res = {}
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
            login_user(user, remember=True)
            res["status"] = "success"
            res["message"] = "Usuario registrado con exito."
        except Exception as e:
            res["status"] = "warning"
            res["message"] = "No se pudo registrar su usuario."
            handle_error_db(e, db)
        finally:
            db.session.close()
        return jsonify(res)
    return render_template("register.html")

@app.route("/producto/buscar", methods=["GET"])
def producto_buscar():
    buscar = request.args.get("buscar")
    assert buscar is not None
    buscar = buscar.lower()
    filtered_productos = Producto.query.filter(Producto.nombre.like("%{}%".format(buscar))).all()
    if not filtered_productos:
        filtered_productos = Producto.query.all()
    return render_template("index.html", productos=filtered_productos, usuario=current_user)

@app.route("/producto/ver/<producto_id>", methods=["GET"])
def producto_ver(producto_id):
    return render_template("producto.html", producto=Producto.query.get(producto_id))

@app.route("/producto/categoria/<nombre_categoria>")
def producto_categoria(nombre_categoria):
    filtered_productos = Producto.query.filter(Producto.categoria == nombre_categoria).all()
    if not filtered_productos:
        filtered_productos = Producto.query.all()
    return render_template("index.html", productos=filtered_productos)

@app.route("/producto/crear" , methods=["GET", 'POST'])
@login_required
def producto_crear():
    if request.method == "POST":
        res = {}
        try:
            data = request.get_json()
            assert data is not None
            nombre = data['nombre']
            usuario_correo = data['usuario_correo']
            precio = data['precio']
            descripcion = data['descripcion']
            talla = data['talla']
            sexo = data['sexo']
            categoria = data['categoria']
            distrito = data['distrito']
            producto = Producto (
                nombre = nombre,
                usuario_correo = usuario_correo,
                precio = precio,
                descripcion = descripcion,
                talla = talla,
                sexo = sexo,
                categoria = categoria,
                distrito = distrito
            )
            db.session.add(producto)
            db.session.commit()
            res = {
                'id' : producto.id,
                'nombre' : nombre,
                'usuario_correo' : usuario_correo,
                'precio' : precio,
                'descripcion' : descripcion,
                'talla' : talla,
                'sexo' : sexo,
                'categoria' : categoria,
                'distrito' : distrito,
                "status" : "success",
                "message" : "Se creo su producto con exito."
            }
        except Exception as e :
            res["status"] = "warning"
            res["message"] = "No se pudo crear su producto."
            handle_error_db(e, db)
        finally:
            db.session.close()
        return jsonify(res)
    return render_template("vender.html", usuario=current_user)


@app.route("/imagen/crear", methods=["POST"])
@login_required
def imagen_crear():
    res = {}
    try:
        print("reached")
        print(request.files)
        assert "file" in request.files
        file = request.files.get("file")
        random_seed = ShortUUID().random(length=50)
        img_id = secure_filename(str(random_seed) + str(file.filename))
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], img_id))
        producto_id = request.form.get("producto_id")
        imagen = Imagen(id=img_id, producto_id=producto_id)
        db.session.add(imagen)
        db.session.commit()
        res["status"] = "success"
        res["message"] = "Se subio la imagen con exito."
    except Exception as e:
        res["status"] = "warning"
        res["message"] = "No se pudo subir la imagen."
        handle_error_db(e, db)
    finally:
        db.session.close()
    return jsonify(res)


@app.route("/static/uploaded/<img_id>")
def static_uploaded(img_id):
    return send_from_directory("static/uploaded", img_id)

@app.route("/static/resources/<img_id>")
def static_resources(img_id):
    return send_from_directory("static/resources", img_id)

@app.errorhandler(HTTPException)
def handle_http_error(e):
    handle_error(e)
    flash("Ocurrio un error inesperado.", category="danger")
    return redirect(url_for("index"))

@app.errorhandler(AssertionError)
def handle_assertion(e):
    handle_error(e)
    flash("Ocurrio un error inesperado.", category="danger")
    return redirect(url_for("index"))

# Run
if __name__ == "__main__":
    app.run(debug=True, port=5000)

    
