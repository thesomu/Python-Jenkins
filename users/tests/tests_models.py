from django.test import TestCase
from users.models import *


class CustomerTestCase(TestCase):
    def create_cust(self):
        return Customer.objects.create(cust_uname="test", cust_email="test@case.com", cust_password="cust@123",
                                       cust_phone="9900000011", cust_fname="test", cust_lname="case")

    def test_create_cust(self):
        c = self.create_cust()
        self.assertTrue(isinstance(c, Customer))


class ShippingTestCase(TestCase):
    def create_ship(self):
        cust = Customer.objects.create(id=5, cust_uname="test", cust_email="test@case.com", cust_password="cust@123",
                                       cust_phone="9900000011", cust_fname="test", cust_lname="case")
        return Shipping.objects.create(ship_uname_id=cust.id, ship_fname="Test", ship_lname="case",
                                       ship_phone="8800880088",
                                       ship_address="Test Case-110022")

    def test_create_ship(self):
        s = self.create_ship()
        self.assertTrue(isinstance(s, Shipping))
