from django.test import TestCase

from Employee.models import *


class EmployeeTestCase(TestCase):
    def create_emp(self):
        return empTable.objects.create(name="test name", address="test address", phone=123, email="test@email",
                                       designation="null", password=123)

    def test_create_emp(self):
        e = self.create_emp()
        self.assertTrue(isinstance(e, empTable))
