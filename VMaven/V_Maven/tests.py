from typing import Text
from django.test import TestCase
from .models import Product, Category

# Create your tests here.
class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='skirt', slug='skirt')

    def category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))