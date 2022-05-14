# Imports
import sys
import os
import uuid
from flask import Flask, redirect, request, render_template, jsonify, abort, url_for
from models import db, Producto, Usuario, Imagen
from flask_migrate import Migrate
from flask_login import login_required, LoginManager, login_user
from dotenv import load_dotenv
from werkzeug.utils import secure_filename



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
login_manager.login_view = "/login"


# Models
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@app.route("/login", methods=["GET", "POST"])
def login_usuario():
    if request.method == "POST":
        data = request.json
        correo = data["correo"]
        clave = data["clave"]
        nombre = data["nombre"]
        celular = data["celular"]
        usuario = load_user(correo)
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

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        try:
            data = request.json
            correo = data["correo"]
            clave = data["clave"]
            user = Usuario(correo=correo)
            print(user)
            user.set_password(clave)
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


@app.route("/producto/crear" , methods=['POST'])
def crear_producto():
    error = False
    response = {}
    try:
        id = request.get_json()['id']
        correo = request.get_json()['correo']
        precio = request.get_json()['precio']
        descripcion = request.get_json()['descripcion']
        talla = request.get_json()['talla']
        sexo = request.get_json()['sexo']
        categoria = request.get_json()['categoria']
        distrito = request.get_json()['distrito']
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




# Run
if __name__ == "__main__":
    app.run(debug=True, port=5000)

    
