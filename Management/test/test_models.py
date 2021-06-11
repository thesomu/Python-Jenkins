from django.test import TestCase, Client
from django.urls import reverse

from Management.models import empAttendance, dailyAttendance, totalAttendance
from Employee.models import empTable


class TestManagementModels(TestCase):
    def create_emp(self):
        return empTable.objects.create(name="test name", address="test address", phone=123, email="test@email",
                                       designation="null", password=123)

    def create_dailyAttendance(self):
        emp = self.create_emp()
        return dailyAttendance.objects.create(empId=emp, inTime="null", outTime="null")

    def test_dailyAttendance(self):
        e = self.create_dailyAttendance()
        self.assertTrue(isinstance(e, dailyAttendance))

    def create_empAttendance(self):
        emp = self.create_emp()
        return empAttendance.objects.create(empId=emp, dayOne=0, dayTwo=0, dayThree=0, dayFour=0, dayFive=0, daySix=0)

    def test_empAttendance(self):
        e = self.create_empAttendance()
        self.assertTrue(isinstance(e, empAttendance))

    def create_totalAttendance(self):
        emp = self.create_emp()
        return totalAttendance.objects.create(empId=emp, May=0, June=0, July=0)

    def test_totalattenndance(self):
        e = self.create_totalAttendance()
        self.assertTrue(isinstance(e, totalAttendance))
