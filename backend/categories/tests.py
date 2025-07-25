from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from slugify import slugify

from .models import MainCategory, SubCategory


class MainCategoryModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.main_category_data = {
            'name': 'Электроника',
            'is_active': True,
        }
        self.main_category = MainCategory.objects.create(**self.main_category_data)


    def test_main_category_creation(self):
        self.assertEqual(MainCategory.objects.count(), 1)

        self.assertEqual(self.main_category.name, self.main_category_data['name'])
        self.assertEqual(self.main_category.is_active, self.main_category_data['is_active'])

        self.assertEqual(self.main_category.slug, slugify(self.main_category_data['name']))

        self.assertEqual(str(self.main_category), self.main_category_data['name'])


    def test_slug_auto_creation(self):
        new_category = MainCategory.objects.create(name='Бытовая техника')
        self.assertEqual(new_category.slug, slugify(new_category.name))


    def test_verbose_names(self):
        meta = MainCategory._meta
        self.assertEqual(meta.verbose_name, _('Основная категория'))
        self.assertEqual(meta.verbose_name_plural, _('Основные категории'))


class SubCategoryModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.parent_category = MainCategory.objects.create(name='Электроника')
        self.sub_category_data = {
            'name': 'Смартфоны',
            'parent': self.parent_category,
            'is_active': True,
        }
        self.sub_category = SubCategory.objects.create(**self.sub_category_data)


    def test_sub_category_creation(self):
        self.assertEqual(SubCategory.objects.count(), 1)

        self.assertEqual(self.sub_category.name, self.sub_category_data['name'])
        self.assertEqual(self.sub_category.is_active, self.sub_category_data['is_active'])
        self.assertEqual(self.sub_category.parent.name, self.sub_category_data['parent'].name)

        self.assertEqual(self.sub_category.slug, slugify(self.sub_category_data['name']))

        self.assertEqual(str(self.sub_category), self.sub_category_data['name'])


    def test_is_parent_property(self):
        self.assertFalse(self.sub_category.is_parent)

        new_category = SubCategory.objects.create(name='Без родителя')
        self.assertTrue(new_category.is_parent)


    def test_full_path_property(self):
        self.assertEqual(
            self.sub_category.full_path, 
            f'{self.sub_category.parent.name} > {self.sub_category.name}'
        )

        new_category = SubCategory.objects.create(name='Без родителя')
        self.assertEqual(new_category.full_path, f'{new_category.name}')


    def test_verbose_name(self):
        meta = SubCategory._meta
        self.assertEqual(meta.verbose_name, _('Категория'))
        self.assertEqual(meta.verbose_name_plural, _('Категории'))


class MainCategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.main_category = MainCategory.objects.create(name='Недвижимость')
        self.valid_payload = {
            'name': 'Одежда',
            'is_active': True,
        }
        self.invalid_payload = {
            'name': '',
        }
        self.list_url = reverse('Main categories')
        self.create_url = reverse('Create main category')


    def test_get_all_main_categories(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_create_valid_main_category(self):
        response = self.client.post(
            self.create_url,
            data = self.valid_payload,
            format = 'json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MainCategory.objects.count(), 2)
        self.assertEqual(response.data['name'], self.valid_payload['name'])


    def test_create_invalid_main_category(self):
        response = self.client.post(
            self.create_url,
            data=self.invalid_payload,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SubCategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.parent_category = MainCategory.objects.create(name='Одежда')
        self.sub_category = SubCategory.objects.create(name='Штаны')
        self.valid_payload = {
            'name': 'Обувь',
            'parent': self.parent_category.id,
            'is_active': True,
        }
        self.invalid_payload = {
            'name': '',
            'is_active': True,
        }
        self.list_url = reverse('Sub categories')
        self.create_url = reverse('Create sub category')


    def test_get_all_sub_categories(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_create_valid_sub_category(self):
        response = self.client.post(
            self.create_url,
            data=self.valid_payload,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCategory.objects.count(), 2)
        self.assertEqual(response.data['name'], self.valid_payload['name'])


    def test_create_invalid_sub_category(self):
        response = self.client.post(
            self.create_url,
            data=self.invalid_payload,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
