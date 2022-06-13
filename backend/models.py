from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
import os   
from flask_migrate import Migrate


db = SQLAlchemy()

def setup_db(app):
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

def setup_db_test(app):
    db.app = app
    db.init_app(app)
    db.create_all()
    

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    size = db.Column(db.String(3), nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    images = db.relationship("Image", backref="product", lazy=True, cascade="all, delete-orphan")
    comments = db.relationship("Comment", backref="product", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product id={self.id}>"
    
    def JSONSerialize(self):
        return {
            "id": self.id,
            "user_id" : self.user_id,
            "price" : self.price,
            "name" : self.name,
            "description" : self.description,
            "size" : self.size,
            "sex" : self.sex,
            "category" : self.category,
            "city" : self.city
        }
    
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    products = db.relationship("Product", backref="user", lazy=True, cascade="all, delete-orphan")
    comments = db.relationship("Comment", backref="user", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User: id={self.id}>'

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def get_user_id(self):
        return self.id
    
    def JSONSerialize(self):
        return {
            "id": self.id,
            "email" : self.email,
            "password" : self.password,
            "name" : self.name,
            "phone" : self.phone
        }
    
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.String(120), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    def __repr__(self):
        return f'<Image: id={self.id}>'

    def JSONSerialize(self):
        return {
            "id": self.id,
            "product_id": self.product_id
        }
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"<Comment id={self.id}>"
    
    def JSONSerialize(self):
        return {
            "id": self.id,
            "product_id" : self.id,
            "user_id" : self.user_id,
            "content" : self.content,
            "creation_date" : self.creation_date
        }
    
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()