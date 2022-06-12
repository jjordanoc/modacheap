import json
from math import prod
import os
from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from models import db, Product
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER")
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app, origins=['http://localhost:3000'], max_age=10)
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorizations, true")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS")
        return response
    
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

        product.create()

        return jsonify({
            "success" : True,
            "product" : product.JSONSerialize()
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
    
    return app