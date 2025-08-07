from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'email': 'test@gmail.com',
            'password': 'test',
            'phone_number': '111224444444',
            'first_name': 'First',
            'last_name': 'Last',
        }
        self.user = User.objects.create(**self.user_data)


    def test_create_user(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.password, self.user_data['password'])
        self.assertEqual(self.user.phone_number, self.user_data['phone_number'])
        self.assertEqual(self.user.first_name, self.user_data['first_name'])
        self.assertEqual(self.user.last_name, self.user_data['last_name'])
        self.assertEqual(str(self.user), self.user_data['email'])


    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name, f'{self.user_data['first_name']} {self.user_data['last_name']}')


class UserAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('log_in')
        self.logout_url = reverse('log_out')
        self.user_detail = reverse('user_detail')
        
        self.user = User.objects.create(**{
            'email': 'test@gmail.com',
            'password': 'test',
            'phone_number': '111224444444',
            'first_name': 'Valid',
            'last_name': 'Payload',
        })

        self.valid_payload = {
            'email': 'unique@gmail.com',
            'password': 'test1',
            'phone_number': '111224444444',
            'first_name': 'Valid',
            'last_name': 'Payload',
        }

        self.invalid_payload = {
            'email': 'smth2com',
            'password': '',
            'phone_number': 'asd',
            'first_name': '',
            'last_name': '',
        }

    def register_valid_user(self):
        response = self.client.post(
            self.register_url,
            data=self.valid_payload,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.data['email'], self.valid_payload['email'])


    def register_invalid_user(self):
        response = self.client.post(
            self.register_url,
            data=self.invalid_payload,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)


    def test_retrieve_user_details_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.user_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)


    def test_retrieve_user_details_unauthenticated(self):
        response = self.client.get(self.user_detail)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_log_out_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        refresh = RefreshToken.for_user(self.user)
        response = self.client.post(
            self.logout_url, 
            {'refresh_token': str(refresh)}, 
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        self.assertEqual(response.data, {'message': 'Log Out'})


    def test_log_out_unauthentucated_user(self):
        response = self.client.post(
            self.logout_url, 
            {}, 
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_log_out_missing_token(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.logout_url,
            {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)