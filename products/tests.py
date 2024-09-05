from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product
from django.contrib.auth.models import User

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            title="Test Product",
            description="A description",
            category="Test Category",
            price=9.99,
            stock=100
        )
        self.assertEqual(product.title, "Test Product")
        self.assertEqual(product.price, 9.99)

class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Create a product to test API with
        self.product = Product.objects.create(
            title="Test Product",
            description="Test description",
            category="Test Category",
            price=19.99,
            stock=10
        )
        self.url = reverse('product_list_create')
        self.user = User.objects.create_user(username="testuser", password="testPassword23$")
        self.client.force_authenticate(user=self.user)

    def test_list_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
