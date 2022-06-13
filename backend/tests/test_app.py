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
    
    def test_user_create_success(self):
        res = self.client.post("/register", json={"email" : "test2@test.com", "password" : "testpass123", "name" : "Test Com", "phone" : "955108212"})
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

    def test_user_login_success(self):
        res = self.client.post("/login", json={"email" : self.test_user.email, "password" : "testpass123"})
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

    def tearDown(self) -> None:
        for product in Product.query.all():
            product.delete()
        for user in User.query.all():
            user.delete()
        pass
        