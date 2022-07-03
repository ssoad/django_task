
from django.test import TestCase
import random
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
# Create your tests here.


class RegisterTest(TestCase):

    def test_register(self):
        rand = str(2022) #str(random.randint(0, 100))
        response = self.client.post('/accounts/register/', {
            'username': 'test'+rand,
            'password': 'test@2022',
            'password2': 'test@2022',
            'email': 'test'+rand+'@gmail.com',
            'phone': '123456789'+rand
            })
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], 'User created successfully')
        
        response = self.client.post('/accounts/login/', {
                'username': 'test2022',
                'password': 'test@2022'
                })
        # print(response.content)
        token = response.json()['token']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['token'], token)

        client = APIClient()
        
        client.login(username='test2022', password='test@2022')
        response = client.get('/accounts/user/')
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['phone'], '1234567892022')

           
