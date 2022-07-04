import unittest
from server import create_app
import json
from models import Product, User, Image, setup_db_test

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
        res = self.client.post("/register", json=json)
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
        self.assertFalse(data.get("user"))


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
    
    # ------------- PRODUCTS -------------

    def test_product_get_success_default(self):
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

    def test_delete_products_success(self):
        res = self.client.post("/products", json=self.new_products)
        data = res.get_json()
        deleted_id = data.get("product_id")
        res = self.client.delete("/products/" +  str(deleted_id))

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("product_id"))

    def test_delete_product_failed(self):
        res = self.client.patch('/products/123',json=self.new_products)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'El producto no se ha encontrado.')
        self.assertEqual(data['success'], False)

    def test_update_product_success(self):

        res0 = self.client.post("/products", json= self.new_products)
        data0 = res0.get_json()
        updated_id = data0.get("product_id")
        res = self.client.patch("/products/" + str(updated_id), json={"description":"This is a new description"})
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["product_id"], data.get("product_id"))

    def test_update_product_failed(self):

        res = self.client.patch("/products/1000")
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'El producto no se ha encontrado.')

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

    def tearDown(self) -> None:
        for product in Product.query.all():
            product.delete()
        for user in User.query.all():
            user.delete()
        for image in Image.query.all():
            image.delete()
        pass
        