from enum import unique
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()
class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_correo = db.Column(db.String(80), db.ForeignKey("usuarios.correo"), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    talla = db.Column(db.String(3), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    categoria = db.Column(db.String(30), nullable=False)
    distrito = db.Column(db.String(80), nullable=False)
    imagenes = db.relationship("Imagen", backref="producto", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Producto id={self.id}>"


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    correo = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    celular = db.Column(db.Integer, nullable=False, unique=True)
    productos = db.relationship("Producto", backref="usuario", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Usuario: usuario={self.correo}>'

    def check_clave(self, clave):
        return check_password_hash(self.clave, clave)

    def set_clave(self, clave):
        self.clave = generate_password_hash(clave)
    
    def get_id(self):
        return self.correo


class Imagen(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String(120), primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)

    def __repr__(self):
        return f'<Imagen: id={self.id}>'



