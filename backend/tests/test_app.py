import unittest
from server import create_app
from models import db, Product, User

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.app = create_app()
        self.client = self.app.test_client()
        db.init_app(self.app)
    
    def test_product_create_success(self):
        res = self.client.post("/products", json={
            
        })