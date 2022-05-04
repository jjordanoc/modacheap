from app import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), db.ForeignKey("users.username"), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    talla = db.Column(db.String(3), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    categoria = db.Column(db.String(30), nullable=False)
    distrito = db.Column(db.String(80), nullable=False)

    def __repr__(self) -> str:
        return f"<Producto id={id}>"



