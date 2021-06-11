from django.test import TestCase
from shopping.models import Company
from shopping.models import User
from shopping.models import Product
from shopping.models import Cart
from shopping.models import OrderPlaced

class CompanyTest(TestCase):
    def create_Company(self,comp_id="only a number"):
        return Company.objects.create(comp_id=comp_id)
    def test_create_Company(self):
        c = self.create_Company()
        self.assertTrue(isinstance(o, Company)) 


class UserTest(TestCase):
    def create_User(self,comp_id="only a number"):
        return User.objects.create(user_id=user_id)
    def test_create_User(self):
        c = self.create_User()
        self.assertTrue(isinstance(o, User))            



# Create your tests here.
