from django.test import TestCase, Client
from django.urls import reverse, resolve
from users.models import *

class Customerviewstest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse('adminhome')
        self.session = self.client.session

    def create_cust(self):
        return Customer.objects.create(cust_uname="test", cust_email="test@case.com", cust_password="cust@123",
                                       cust_phone="9900000011", cust_fname="test", cust_lname="case")

    def test_create_cust(self):
        c = self.create_cust()
        self.assertTrue(isinstance(c, Customer))


    def test_adminlogin(self):
        self.session['adminlogin'] = 'somnath'
        self.session.save()
        response = self.client.get(self.home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custadmin.html')