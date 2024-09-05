from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class UserAuthAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="testuser@gmail.com", password="testPassword23$")

    def test_login(self):
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testPassword23$'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
