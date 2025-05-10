from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Product, Order, OrderItem

class EcommerceAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.token_url = '/api/token/'

        # Create token
        response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'testpass123'})
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Create a product
        self.product = Product.objects.create(name='Test Product', description='Description', price=10.00, stock=100)

    def test_create_order(self):
        # Create an order
        response = self.client.post('/api/orders/', {})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.first().user, self.user)

    def test_add_order_item(self):
        # First, create an order
        order = Order.objects.create(user=self.user)

        # Then, create an order item
        response = self.client.post('/api/order-items/', {
            'order': order.id,
            'product': self.product.id,
            'quantity': 2
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(OrderItem.objects.first().product.name, 'Test Product')

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('Test Product' in str(response.data))

    def test_unauthenticated_order_creation_fails(self):
        self.client.logout()
        response = self.client.post('/api/orders/', {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_auth_token(self):
        response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'testpass123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)