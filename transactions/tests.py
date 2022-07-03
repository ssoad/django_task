from django.test import TestCase
from rest_framework.test import APIClient

from usersinfo.models import Customer
# Create your tests here.
class TransactionTest(TestCase):

    def test_transaction(self):
        #User one
        response = self.client.post('/accounts/register/', {
            'username': 'test2022',
            'password': 'test@2022',
            'password2': 'test@2022',
            'email': 'test2022@gmail.com',
            'phone': '1234567892020'
            })
        #User Two
        response = self.client.post('/accounts/register/', {
            'username': 'test20221',
            'password': 'test@2022',
            'password2': 'test@2022',
            'email': 'test2022@gmail.com',
            'phone': '1234567902020'
            })
        client = APIClient()
        user1 = Customer.objects.get(user__username='test2022')
        user1.balance = 1000
        user1.save()
        client.login(username='test2022', password='test@2022')
        response = client.post('/transaction/sendmoney/', {
            'receiver': '1234567902020',
            'amount': '100',
            'datetime': '02/07/22 23:56:19'
        })
        self.assertEqual(response.status_code, 200)
        user2 = Customer.objects.get(user__username='test20221')
        self.assertEqual(user2.balance, 100)
    
    def test_transaction_history(self):
        rand = str(2022) #str(random.randint(0, 100))
        response = self.client.post('/accounts/register/', {
            'username': 'test'+rand,
            'password': 'test@2022',
            'password2': 'test@2022',
            'email': 'test'+rand+'@gmail.com',
            'phone': '123456789'+rand
            })
        client = APIClient()
        client.login(username='test2022', password='test@2022')
        # print(response.content)
        response = client.get('/transaction/history/')
        self.assertEqual(response.status_code, 200) 