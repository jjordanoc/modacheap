import json
import os
from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from models import Product, User, setup_db

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app, origins=['http://localhost:3000'], max_age=10)
    setup_db(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorizations, true")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS")
        return response
    
    @app.route("/register", methods=["POST"])
    def register_user():
        body = request.get_json()
        email = body.get("email", None)
        password = body.get("password", None)
        name = body.get("name", None)
        phone = body.get("phone", None)
        if not email or not password or not name or not phone or User.query.filter(User.email == email).one_or_none() or User.query.filter(User.phone == phone).one_or_none():
            abort(422)
        user = User(email=email, name=name, phone=phone)
        user.set_password(password)
        user_id = user.create()

        return jsonify({
            "success" : True,
            "user_id" : user_id,
            "user" : user.JSONSerialize()
        })
    
    @app.route("/login", methods=["POST"])
    def login_user():
        body = request.get_json()
        email = body.get("email", None)
        password = body.get("password", None)
        if not email or not password:
            abort(422)
        user = User.query.filter(User.email == email).one_or_none()
        if not user or not user.check_password(password):
            abort(401)
        # login logic (oauth or another kind of login)

        return jsonify({
            "success" : True,
            "user_id" : user.id
        })
    
    @app.route("/products", methods=["GET"])
    def get_products():
        products = Product.query.all()
        return jsonify({
            "success" : True,
            "products" : [product.JSONSerialize() for product in products],
            "count" : len(products)
        })
    
    @app.route("/products", methods=["POST"])
    def create_product():
        body = request.get_json()
        user_id = body.get("user_id", None)
        price = body.get("price", None)
        name = body.get("name", None)
        description = body.get("description", None)
        size = body.get("size", None)
        sex = body.get("sex", None)
        category = body.get("category", None)
        city = body.get("city", None)
        if not user_id or not price or not name or not description or not size or not sex or not category or not city:
            abort(404)

        product = Product(user_id=user_id, price=price, name=name, description=description, size=size, sex=sex, category=category, city=city)
        product_id = product.create()

        return jsonify({
            "success" : True,
            "product_id" : product_id
        })
    
    @app.route("/products/<product_id>", methods=["DELETE"])
    def delete_product(product_id):
        product = Product.query.filter(Product.id == product_id).one_or_none()
        product.delete()
        return jsonify({
            "success" : True,
            "product_id" : product_id
        })
    
    @app.route("/products/<product_id>", methods=["PATCH"])
    def update_product(product_id):
        product = Product.query.filter(Product.id == product_id).one_or_none()
        body = request.get_json()
        if "price" in body:
            product.price = body.get("price")
        if "name" in body:
            product.name = body.get("name")
        if "description" in body:
            product.description = body.get("description")
        if "size" in body:
            product.size = body.get("size")
        if "sex" in body:
            product.sex = body.get("sex")
        if "category" in body:
            product.category = body.get("category")
        if "city" in body:
            product.city = body.get("city")
        product.update()
        return jsonify({
            "success" : True,
            "product_id" : product_id
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "status": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "status": 500,
            "message": "internal server error"
        }), 500
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "status": 405,
            "message": "method not allowed"
        }), 405
    

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "status": 422,
            "message": "unprocessable entity"
        }), 422
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "status": 401,
            "message": "unauthorized"
        }), 401
    
    return app