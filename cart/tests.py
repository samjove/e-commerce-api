from products.models import Product
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class CartAPITestCase(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title="Test Product",
            description="Test description",
            category="Test Category",
            price=19.99,
            stock=10
        )
        self.user = User.objects.create_user(username="testuser", password="testPassword23$")
        self.client.force_authenticate(user=self.user)

    def test_add_product_to_cart(self):
        url = reverse('add_to_cart')
        data = {'product_id': self.product.id, 'quantity': 2}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
