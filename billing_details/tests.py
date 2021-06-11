from django.test import TestCase
from billing_details.models import *
# Create your tests here.
class CreditTestCase(TestCase):
    def create_Credit(self):
        return billing.objects.create(fullname="Jai",emailid="jaiarora5080@gmail.com",address="Krishna Nagar",
        city="Delhi",state="Delhi",zip="110051",cardname="Jai Arora" ,cardnumber="1111222255558888", expiry_month="10",expiry_year="2014",cvv="458")
    
    def test_create_Credit(self):
        e=self.create_Credit()
        self.assertTrue(isinstance(e,billing))

class SalaryTestCase(TestCase):
    def create_Salary(self):
        return Salary.objects.create(Employee_ID="259",working_hour="45.6",month="June",email="jaiarora5080@gmail.com")
    
    def test_create_Salary(self):
        e=self.create_Salary()
        self.assertTrue(isinstance(e,Salary))        