import unittest
from server import create_app
import json
from models import Product, User, Image, Comment, setup_db_test
from datetime import datetime

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()
        setup_db_test(self.app)
        # Create a user for testing purposes
        res_user = self.client.post("/register", json={"email" : "test@test.com", "password" : "testpass123", "name" : "Test Com", "phone" : "955108292"})
        user_data = res_user.get_json()
        self.test_user = User.query.get(user_data.get("user_id"))

        self.new_products = {
            "user_id" : self.test_user.id,
            "price" : 100,
            "name" : "Test Product",
            "description" : "This is a long description. Read it carefully.",
            "size" : "M",
            "sex" : "M",
            "category" : "Polos",
            "city" : "SANTIAGO DE SURCO"
        }


    # ------------- REGISTER ------------- 
    def test_user_create_success(self):
        json = {"email" : "test2@test.com", "password" : "testpass123", "name" : "Test Com", "phone" : "955108212"}
        res = self.client.post("/register", json = json)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("user_id"))

    
    def test_user_create_failure(self):
        res = self.client.post("/register", json={})
        data = res.get_json()
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data.get("success"))
        self.assertFalse(data.get("user_id"))


    # ------------- LOGIN -------------

    def test_user_login_success(self):
        json = {"email" : self.test_user.email, "password" : "testpass123"}
        res = self.client.post("/login", json=json)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("user_id"))
    
    def test_user_login_failure(self):
        res = self.client.post("/login", json={})
        data = res.get_json()
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data.get("success"))
        self.assertFalse(data.get("user_id"))
    
    def test_user_login_failure2(self):
        json = {"email" : self.test_user.email, "password" : "nottestpass1234"}
        res = self.client.post("/login", json=json)
        data = res.get_json()
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data.get("success"))
        self.assertFalse(data.get("user_id"))

    # ------------- USERS -------------

    def test_users_get_success(self):
        res = self.client.get("/users")
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("users"))
        self.assertTrue(data.get("count"))

    def test_user_get_success(self):
        res = self.client.get("/users/"+ str(self.test_user.id))
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("user"))
    
    def test_user_get_failure(self):
        res = self.client.get("/users/-1")
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data.get("success"))
        self.assertEqual(data['message'], 'No se ha encontrado el usuario.')

    def test_user_update_success(self):
        json = {"email" : "test@gmail.com", "password" : "pass123", "name" : "Test", "phone" : "924681598"}
        res0 = self.client.post("/register", json = json)
        data0 = res0.get_json()
        updated_id = data0.get("user_id")
        res = self.client.patch("/users/" + str(updated_id), json={"email":"new_email@gmail.com"})
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["user_id"], str(updated_id))

    def test_user_delete_success(self):
        json = {"email" : "test@gmail.com", "password" : "pass123", "name" : "Test", "phone" : "924681598"}
        res = self.client.post("/register", json = json)
        data = res.get_json()
        deleted_id = data.get("user_id")
        res = self.client.delete("/users/" +  str(deleted_id))

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("user_id"))
        
    # ------------- PRODUCTS -------------

    def test_product_get_success(self):
        res = self.client.get("/products")
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        products = data.get("products")
        if len(products) > 0:
            self.assertTrue(products)
            self.assertEqual(len(products), data.get("count"))
            self.assertGreater(len(products), 0)
        else:
            self.assertFalse(products)
            self.assertEqual(len(products), data.get("count"))
            self.assertEqual(len(products), 0)
    
    def test_product_create_success(self):
        res = self.client.post("/products", json=self.new_products)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("product_id"))
    
    def test_product_create_failure(self):
        res = self.client.post("/products", json={})
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data.get("success"))
        self.assertFalse(data.get("product_id"))

    def test_product_create_failure2(self):
        res = self.client.post("/products", json={"user_id":self.test_user.id})
        data = res.get_json()

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data.get("success"))
        self.assertEqual(data.get("message"), "No se ha provicionado un precio al producto.")

    def test_product_delete_success(self):
        res = self.client.post("/products", json=self.new_products)
        data = res.get_json()
        deleted_id = data.get("product_id")
        res = self.client.delete("/products/" +  str(deleted_id))

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("product_id"))

    def test_product_delete_failed(self):
        res = self.client.patch('/products/123',json=self.new_products)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'No se ha encontrado el producto.')
        self.assertEqual(data['success'], False)

    def test_product_update_success(self):

        res0 = self.client.post("/products", json= self.new_products)
        data0 = res0.get_json()
        updated_id = data0.get("product_id")
        res = self.client.patch("/products/" + str(updated_id), json={"description":"This is a new description"})
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["product_id"], str(updated_id))

    def test_product_update_failed(self):

        res = self.client.patch("/products/1000")
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'No se ha encontrado el producto.')

    # ------------- IMAGES -------------

    def test_image_get_success_default(self):
        res = self.client.get("/images")
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        images = data.get("images")
        if len(images) > 0:
            self.assertTrue(images)
            self.assertEqual(len(images), data.get("count"))
            self.assertGreater(len(images), 0)
        else:
            self.assertFalse(images)
            self.assertEqual(len(images), data.get("count"))
            self.assertEqual(len(images), 0)

    # ------------- COMMENTS -------------

    def test_comments_get_success(self):
        res = self.client.get("/comments")
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        comments = data.get("comments")
        if len(comments) > 0:
            self.assertTrue(comments)
            self.assertEqual(len(comments), data.get("count"))
            self.assertGreater(len(comments), 0)
        else:
            self.assertFalse(comments)
            self.assertEqual(len(comments), data.get("count"))
            self.assertEqual(len(comments), 0)

    def test_comment_get_success(self):

        json = {"user_id": self.test_user.id, "content":"This comment is a try", "creation_date": datetime.now()}

        # Create a product for testing purposes     
        res_product = self.client.post("/products", json = self.new_products)
        product_data = res_product.get_json()
        self.test_product = Product.query.get(product_data.get("product_id"))

        # Create a comment for testing purposes
        res_comment = self.client.post("/products/" + str(self.test_product.id) + "/comments", json=json)
        comment_data = res_comment.get_json()
        self.test_comment = Comment.query.get(comment_data.get("comment_id"))

        res = self.client.get("/comments/" + str(self.test_comment.id))
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("comment"))
        
    def test_comment_get_failure(self):
        
        res = self.client.get("/comments/-123")
        data = res.get_json()

        self.assertEqual(res.status_code,404)
        self.assertFalse(data.get("success"))
        self.assertEqual(data.get("message"), "No se ha encontrado el comentario.")


    def test_comment_post_success(self):
        json = {"user_id": self.test_user.id, "content":"This comment is a try", "creation_date": datetime.now()}

        # Create a product for testing purposes     
        res_product = self.client.post("/products", json = self.new_products)
        product_data = res_product.get_json()
        self.test_product = Product.query.get(product_data.get("product_id"))

        res = self.client.post("/products/" + str(self.test_product.id) + "/comments", json=json)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("comment_id"))
        
    def test_comment_post_failure(self):
        res = self.client.post("/products/-12312123/comments", json = {})
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data.get("success"))
        self.assertEqual(data.get("message"),"No se ha encontrado el producto.")

    def test_comment_update_success(self):
        json = {"user_id": self.test_user.id, "content":"This comment is a try", "creation_date": datetime.now()}

        # Create a product for testing purposes     
        res_product = self.client.post("/products", json = self.new_products)
        product_data = res_product.get_json()
        self.test_product = Product.query.get(product_data.get("product_id"))

        # Create a comment for testing purposes
        res_comment = self.client.post("/products/" + str(self.test_product.id) + "/comments", json=json)
        comment_data = res_comment.get_json()
        self.test_comment = Comment.query.get(comment_data.get("comment_id"))

        res = self.client.patch("/comments/"+str(self.test_comment.id), json={"content":"This comment is patched"})
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("comment_id"))

    def test_comment_update_failure(self):
        res = self.client.patch("comments/-123")
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data.get("success"))
        self.assertEqual(data.get("message"), "No se ha encontrado el comentario.")
        
    def test_comment_delete_success(self):
        json = {"user_id": self.test_user.id, "content":"This comment is a try", "creation_date": datetime.now()}

        # Create a product for testing purposes     
        res_product = self.client.post("/products", json = self.new_products)
        product_data = res_product.get_json()
        self.test_product = Product.query.get(product_data.get("product_id"))

        # Create a comment for testing purposes
        res_comment = self.client.post("/products/" + str(self.test_product.id) + "/comments", json=json)
        comment_data = res_comment.get_json()
        self.test_comment = Comment.query.get(comment_data.get("comment_id"))

        res = self.client.delete("/comments/"+ str(self.test_comment.id))
        data = res.get_json()
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("comment_id"))

    def test_comment_delete_failure(self):
        res = self.client.delete("/comments/-3981")
        data = res.get_json()

        self.assertEqual(res.status_code,404)
        self.assertFalse(data.get("success"))
        self.assertEqual(data.get("message"), "No se ha encontrado el comentario.")

    # -----------------------

    def tearDown(self) -> None:
        for product in Product.query.all():
            product.delete()
        for user in User.query.all():
            user.delete()
        for image in Image.query.all():
            image.delete()
        for comment in Comment.query.all():
            comment.delete()
        pass
        