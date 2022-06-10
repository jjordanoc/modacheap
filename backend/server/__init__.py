import json
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
    
    @app.route("/product", methods=["GET"])
    def get_products():
        product = Product.query.all()
        return jsonify({
            "a": "b"
        })
    
    return app