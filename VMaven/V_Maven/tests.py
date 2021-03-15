from typing import Text
from unittest import skip
from django.http import request, response
from django.test import TestCase, Client
from django.urls.base import reverse
from .models import Product, Category
from django.contrib.auth.models import User
from django.http import HttpRequest
from .views import home 

# Create your tests here.
class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="women's fashion", slug='womens-fashion')

    def test_category_model_entry(self):
        #test category model default name
        data = self.data1
        self.assertEqual(str(data), "women's fashion")


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='skirt', slug='skirt')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, name='black casual dress',
            created_by_id=1, slug='black-casual-dress', price='30.00', image='black_dress.jpg')

    def test_products_model_entry(self):
        #test category model default name
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'black casual dress')


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name="women's fashion", slug='womens-fashion')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, name='black casual dress',
            created_by_id=1, slug='black-casual-dress', price='30.00', image='black_dress.jpg')

    def test_url_allowed_hosts(self):
       response = self.c.get('/')
       self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('V_Maven:product_detail', args=['black-casual-dress']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        response = self.c.get(reverse('V_Maven:category_list', args=['womens-fashion']))

    def test_homepage_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Welcome</title>', html)
        self.assertEqual(response.status_code, 200)
