from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from slugify import slugify
from categories.models import MainCategory, SubCategory
from .models import Product


class ProductMoedlTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.parent_category = MainCategory.objects.create(name='Электроника')
        self.sub_category = SubCategory.objects.create(name='Смартфоны', parent=self.parent_category)
        self.product_data = {
            'name': 'Iphone',
            'description': 'Iphone 16 Pro Max',
            'price': 255.99,
            'sub_category': self.sub_category,
            'is_active': True,
        }
        self.product = Product.objects.create(**self.product_data)


    def test_product_creation(self):
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(self.product.name, self.product_data['name'])
        self.assertEqual(self.product.slug, slugify(self.product_data['name']))
        self.assertEqual(self.product.description, self.product_data['description'])
        self.assertEqual(self.product.price, self.product_data['price'])
        self.assertEqual(self.product.sub_category.name, self.product_data['sub_category'].name)
        self.assertEqual(self.product.sub_category.is_active, self.product_data['is_active'])
        self.assertEqual(str(self.product), self.product_data['name'])


    def test_full_path(self):
        self.assertEqual(self.product.full_path, f'{self.product.sub_category.parent.name} > {self.product.sub_category.name} > {self.product.name}')


    def test_verbose_name(self):
        meta = Product._meta
        self.assertEqual(meta.verbose_name, _('Товар'))
        self.assertEqual(meta.verbose_name_plural, _('Товары'))


class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()        
        self.list_url = reverse('Products')
        self.create_url = reverse('Create product')
        self.parent_category = MainCategory.objects.create(name='Электроника')
        self.sub_category = SubCategory.objects.create(name='Смартфоны', parent=self.parent_category)
        self.product_data = {
            'name': 'Iphone',
            'description': 'Iphone 16 Pro Max',
            'price': 255.99,
            'sub_category': self.sub_category,
            'is_active': True,
        }
        self.product = Product.objects.create(**self.product_data)

        self.valid_payload = {
            'name': 'Samsung',
            'description': 'Samsung Galaxy S25',
            'price': 199.00,
            'sub_category': self.sub_category.id,
            'is_active': True,
        }
        self.invalid_payload = {
            'name': '',
            'description': '',
            'price': '',
            'is_active': True,
        }


    def test_get_all_products(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_create_valid_product(self):
        response = self.client.post(
            self.create_url,
            data=self.valid_payload,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(response.data['name'], self.valid_payload['name'])


    def test_create_invalid_product(self):
        response = self.client.post(
            self.create_url,
            data=self.invalid_payload,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
