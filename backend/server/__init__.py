import json
import os
from flask import Flask, abort, jsonify, request, send_from_directory, send_file
from flask_cors import CORS
from sqlalchemy import desc
from models import Product, User, Image, Comment, setup_db
from dotenv import load_dotenv
from shortuuid import ShortUUID
from werkzeug.utils import secure_filename
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app, origins=['http://localhost:8080'], max_age=10)
    setup_db(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorizations, true")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS")
        return response
    
    # ------------- REGISTER -------------

    @app.route("/register", methods=["POST"])
    def register_user():
        body = request.get_json()
        email = body.get("email", None)
        password = body.get("password", None)
        name = body.get("name", None)
        phone = body.get("phone", None)

        if not email:
            abort(422, description = "No se ha provicionado un correo electrónico.")

        if not password:
            abort(422, description = "No se ha provicionado una contraseña.")

        if not name:
            abort(422, description = "No se ha provicionado un nombre.")

        if not phone:
            abort(422, description = "No se ha provicionado un número telefónico.")

        if len(phone) >= 10:
            abort(422, description = "Se ha provicionado un número telefónico inválido.")

        if User.query.filter(User.email == email).one_or_none() is not None:
            abort(422, description ="El correo electrónico ya está en uso.")

        if User.query.filter(User.phone == phone).one_or_none() is not None:
            abort(422, description="El número telefónico ya está en uso.")  

        user = User(email=email, name=name, phone=phone)
        user.set_password(password)
        user_id = user.create()

        return jsonify({
            "success" : True,
            "user_id" : user_id,
        })
    
    # ------------- LOGIN -------------

    @app.route("/login", methods=["POST"])
    def login_user():
        body = request.get_json()
        email = body.get("email", None)
        password = body.get("password", None)

        if not email:
            abort(422, description = "No se ha provicionado un correo electrónico.")

        if not password:
            abort(422, description = "No se ha provicionado una contraseña.")

        user = User.query.filter(User.email == email).one_or_none()

        if not user or not user.check_password(password):
            abort(401, description = "Lo sentimos, las credenciales que está usando son inválidas.")
        # login logic (oauth or another kind of login)

        return jsonify({
            "success" : True,
            "user_id" : user.id,
            "user" : user.JSONSerialize()
        })
    
    # ------------- PRODUCTS -------------

    @app.route("/products", methods=["GET"])
    def get_products():
        products = Product.query.all()
        return jsonify({
            "success" : True,
            "products" : [product.JSONSerialize() for product in products],
            "count" : len(products)
        })
    
    @app.route("/products/<product_id>", methods=["GET"])
    def get_product(product_id):
        product = Product.query.filter(Product.id == product_id).one_or_none()
        if product is None:
            abort(404, description="No se ha encontrado el producto.")
        return jsonify({
            "success" : True,
            "product" : product.JSONSerialize(),
            "user" : product.user.JSONSerialize(),
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

        if not user_id:
            abort(404, description="No se ha encontrado el usuario.")

        if not price:
            abort(422, description="No se ha provicionado un precio al producto.")

        if not name:
            abort(422, description="No se ha provicionado un nombre al producto.")

        if not description:
            abort(422, description="No se ha provicionado una descripción al producto.")

        if not size:
            abort(422, description="No se ha provicionado una talla al producto.")
        
        if not sex:
            abort(422, description="No se ha provicionado un género al producto.")

        if not category:
            abort(422, description="No se ha provicionado una categoría al producto.")

        if not city:
            abort(422, description="No se ha provicionado una ciudad al producto.")
        
        product = Product(user_id=user_id, price=price, name=name, description=description, size=size, sex=sex, category=category, city=city)
        product_id = product.create()

        return jsonify({
            "success" : True,
            "product_id" : product_id
        })
    
    @app.route("/products/<product_id>", methods=["DELETE"])
    def delete_product(product_id):
        product = Product.query.filter(Product.id == product_id).one_or_none()

        if product is None:
            abort(404, description = "No se ha encontrado el producto.")

        product.delete()
        return jsonify({
            "success" : True,
            "product_id" : product_id
        })
    
    @app.route("/products/<product_id>", methods=["PATCH"])
    def update_product(product_id):
        product = Product.query.filter(Product.id == product_id).one_or_none()

        if product is None:
            abort(404, description = "No se ha encontrado el producto.")

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


    # ------------- USERS -------------

    @app.route("/users", methods=["GET"])
    def get_users():
        users = User.query.all()
        return jsonify({
            "success" : True,
            "users" : [user.JSONSerialize() for user in users],
            "count" : len(users)
        })
    
    @app.route("/users/<user_id>", methods=["GET"])
    def get_user(user_id):
        user = User.query.filter(User.id == user_id).one_or_none()
        if user is None:
            abort(404, description="No se ha encontrado el usuario.")
        return jsonify({
            "success" : True,
            "user" : user.JSONSerialize()
        })


    @app.route("/users/<user_id>",methods=["PATCH"])
    def update_user(user_id):
        error_404 = False
        try:
            user = User.query.filter(User.id == user_id).one_or_none()
            if user is None:
                abort(404)
            body = request.get_json()
            if "email" in body:
                user.email = body.get("email")
            if "password" in body:
                user.password = body.get("password")
            if "name" in body:
                user.name = body.get("name")
            if "phone" in body:
                user.phone = body.get("phone")
            if "products" in body:
                user.products = body.get("products")
            if "comments" in body:
                user.comments = body.get("comments")
            user.update()
            return jsonify({
                "success" : True,
                "user_id" : user_id
            })
        except:
            if error_404:
                abort(404)
            else:
                abort(500)

    @app.route("/users/<user_id>",methods=["DELETE"])
    def delete_user(user_id):
        user = User.query.filter(User.id == user_id).one_or_none()

        if user is None:
            abort(404, description = "No se ha encontrado el usuario.")

        user.delete()
        return jsonify({
            "success": True,
            "product_id" : user_id
        })
        

    # ------------- IMAGES -------------

    @app.route("/images", methods=["GET"])
    def get_images():
        images = Image.query.all()
        return jsonify({
            "success" : True,
            "images" : [image.JSONSerialize() for image in images],
            "count" : len(images)
        })
    
    @app.route("/products/<product_id>/images", methods=["POST"])
    def create_image(product_id):
        if product_id is None:
            abort(404, description = "No se ha encontrado el producto.")

        file = request.files.get("file")
        random_seed = ShortUUID().random(length=50)
        img_id = secure_filename(str(random_seed) + str(file.filename))
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], img_id))

        image = Image(id=img_id, product_id=product_id)
        image.create()

        return jsonify({
            "success" : True,
            "image_id" : img_id
        })
    
    @app.route("/images/<image_id>", methods=["DELETE"])
    def delete_image(image_id):
        image = Image.query.filter(Image.id == image_id).one_or_none()

        if image is None:
            abort(404, description = "No se ha encontrado la imagen.")

        image.delete()
        return jsonify({
            "success" : True,
            "product_id" : image_id
        })
    
    @app.route("/images/<image_id>", methods=["PATCH"])
    def update_image(image_id):
        image = Image.query.filter(Image.id == image_id).one_or_none()

        if image is None:
            abort(404, description = "No se ha encontrado la imagen.")

        body = request.get_json()
        if "product_id" in body:
            image.product_id = body.get("product_id")
        
        image.update()

        return jsonify({
            "success" : True,
            "product_id" : image_id
        })

    @app.route("/static/uploaded/<img_id>")
    def static_uploaded(img_id):
        return send_from_directory("../static/uploaded", img_id)

    # ------------- COMMENTS -------------

    @app.route("/comments", methods=["GET"])
    def get_comments():
        comments = Comment.query.all()
        return jsonify({
            "success" : True,
            "comments" : [comment.JSONSerialize() for comment in comments],
            "count" : len(comments)
        })

    @app.route("/comments/<comment_id>", methods=["GET"])
    def get_comment(comment_id):
        comment = Comment.query.filter(Comment.id == comment_id).one_or_none()
        if comment is None:
            abort(404, description="No se ha encontrado el comentario.")
        return jsonify({
            "success" : True,
            "comment" : comment.JSONSerialize()
        })

    @app.route("/products/<product_id>/comments", methods = ["POST"])
    def create_comment(product_id):

        product = Product.query.filter(Product.id == product_id).one_or_none()

        if product is None:
            abort(404, description = "No se ha encontrado el producto.")

        body = request.get_json()
        user_id = body.get("user_id", None)
        content = body.get("content", None)
        creation_date = body.get("creation_date", None)
        
        comment = Comment(user_id = user_id, product_id = product_id, content = content, creation_date = creation_date)
        comment_id = comment.create()

        return jsonify({
            "success" : True,
            "comment_id" : comment_id
        })

    @app.route("/comments/<comment_id>", methods = ["PATCH"])
    def update_comment(comment_id):
        comment = Comment.query.filter(Comment.id == comment_id).one_or_none()

        if comment is None:
            abort(404, description = "No se ha encontrado el comentario.")

        body = request.get_json()

        if "content" in body:
            comment.content = body.get("content")
        
        comment.update()

        return jsonify({
            "success" : True,
            "comment_id" : comment_id
        })

    @app.route("/comments/<comment_id>", methods = ["DELETE"])
    def delete_comment(comment_id):
        comment = Comment.query.filter(Comment.id == comment_id).one_or_none()

        if comment is None:
            abort(404, description = "No se ha encontrado el comentario.")

        comment.delete()

        return jsonify({
            "success" : True,
            "comment_id" : comment_id
        })

    # ------------- ERROR HANDLRES -------------

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "status": error.code,
            "message": "bad request"
        }), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "status": error.code,
            "message": error.description
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "status": error.code,
            "message": error.description
        }), 404
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "status": error.code,
            "message": "method not allowed"
        }), 405
    

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "status": error.code,
            "message": error.description
        }), 422
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "status": error.code,
            "message": "internal server error"
        }), 500

    return app