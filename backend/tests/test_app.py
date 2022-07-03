import unittest
from server import create_app
from models import Product, User, setup_db_test

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()
        setup_db_test(self.app)
        # Create a user for testing purposes
        res_user = self.client.post("/register", json={"email" : "test@test.com", "password" : "testpass123", "name" : "Test Com", "phone" : "955108292"})
        user_data = res_user.get_json()
        self.test_user = User.query.get(user_data.get("user_id"))
    
    # ------------- REGISTER ------------- 
    def test_user_create_success(self):
        json = {"email" : "test2@test.com", "password" : "testpass123", "name" : "Test Com", "phone" : "955108212"}
        res = self.client.post("/register", json=json)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("user_id"))
        self.assertTrue(data.get("user"))
    
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
        json = {}
        res = self.client.post("/login", json=json)
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
        json = {
            "user_id" : self.test_user.id,
            "price" : 100,
            "name" : "Test Product",
            "description" : "This is a long description. Read it carefully.",
            "size" : "M",
            "sex" : "M",
            "category" : "Polos",
            "city" : "SANTIAGO DE SURCO"
        }
        res = self.client.post("/products", json=json)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("product_id"))
    
    def test_product_create_failure(self):
        json = {
            "user_id" : "",
            "price" : 100,
            "name" : "Test Product",
            "description" : "This is a long description. Read it carefully.",
            "size" : "M",
            "sex" : "M",
            "category" : "Polos",
            "city" : "SANTIAGO DE SURCO"
        }
        res = self.client.post("/products", json=json)
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data.get("success"))
        self.assertFalse(data.get("product_id"))



    def tearDown(self) -> None:
        for product in Product.query.all():
            product.delete()
        for user in User.query.all():
            user.delete()
        pass
        