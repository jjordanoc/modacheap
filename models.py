class Usuario(db.Model):
    __tablename__ = 'users'
    _usuario_ = db.Column(db.String(), primary_key=True, nullable=False)
    clave = db.Column(db.String(), primary_key=False, nullable=False)
    nombre = db.Column(db.String(), primary_key=False, nullable=False)
    celular = db.Column(db.Integer, primary_key=False, nullable=False)
    productos = db.relationship("Producto", backref="usuario", lazy=True)

