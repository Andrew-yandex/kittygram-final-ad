from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from cats.models import Cat


class CatsAPITestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='auth_user')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_exists(self):
        """Проверка доступности списка котиков."""
        response = self.client.get('/api/cats/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_cat_creation(self):
        """Проверка создания котика."""
        data = {
            'name': 'Барсик',
            'color': '#000000',
            'birth_year': 2020,
            'achievements': []
        }
        response = self.client.post('/api/cats/', data=data)
        print("Response status:", response.status_code)
        print("Response data:", response.data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(Cat.objects.filter(name='Барсик').exists())