from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), db.ForeignKey("usuarios.usuario"), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    talla = db.Column(db.String(3), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    categoria = db.Column(db.String(30), nullable=False)
    distrito = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<Producto id={self.id}>"


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuario = db.Column(db.String(80), primary_key=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    celular = db.Column(db.Integer, nullable=False)
    productos = db.relationship("Producto", backref="usuarios", lazy=True)

    def __repr__(self):
        return f'<Usuario: usuario={self.usuario}>'

    def check_clave(self, clave):
        return check_password_hash(self.clave, clave)

    def set_clave(self, clave):
        self.clave = generate_password_hash(clave)
