from django.test import TestCase, Client
from django.urls import reverse

from Employee.models import empTable
from Management.models import dailyAttendance, empAttendance, totalAttendance


class TestManagementViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.base_url = reverse('base')
        self.login_url = reverse('hrlogin')
        self.employeeLogin_url = reverse('employeeLogin')

    def create_emp(self):
        emp = empTable.objects.create(name="test name", address="test address", phone=123, email="test@email",
                                      designation="null", password=123)
        dailyAttendance.objects.create(empId=emp, inTime="2021-6-3 0:0:0", outTime="2021-6-3 0:0:0")
        empAttendance.objects.create(empId=emp)
        totalAttendance.objects.create(empId=emp)
        return emp

    def create_dailyAttendance(self):
        emp = self.create_emp()
        return dailyAttendance.objects.create(empId=emp, inTime="2021-6-1 0:0:0", outTime="2021-6-1 0:0:0")

    def test_base(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Base.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HRLogin.html')

    def test_employeeLogin_GET(self):
        response = self.client.get(self.employeeLogin_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeLogin.html')

    def test_login_pass_POST(self):
        response = self.client.post(self.login_url, {
            'id': 'kanishk',
            'password': 'admin'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_fail_POST(self):
        response = self.client.post(self.login_url, {
            'id': 'kanishk',
            'password': 'admi'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HRLogin.html')

    def test_employeeLogin_pass_POST(self):
        emp = self.create_emp()
        response = self.client.post(self.employeeLogin_url, {
            'id': emp.id,
            'password': emp.password
        })
        self.assertEqual(response.status_code, 302)

    def test_employeeLogin_fail_POST(self):
        emp = self.create_emp()
        response = self.client.post(self.employeeLogin_url, {
            'id': emp.id,
            'password': 789
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeLogin.html')

    def test_dashboard(self):
        response = self.client.get(reverse('hrdashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HRLogin.html')

    def test_dashboard_POST(self):
        pass

    def test_hrlogout(self):
        response = self.client.get(reverse('hrlogout'))
        self.assertEqual(response.status_code, 302)

    def test_employeeLogout(self):
        response = self.client.get(reverse('employeeLogout'))
        self.assertEqual(response.status_code, 302)

    def test_team(self):
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Team.html')

    def test_achievements(self):
        response = self.client.get(reverse('achievements'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Achievements.html')

    def test_adventures(self):
        response = self.client.get(reverse('adventures'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Adventures.html')

    def test_attendanceIn(self):
        emp = self.create_emp()
        response = self.client.post(reverse('attendanceIn'), {
            'id': emp.id,
            'in': "2021-6-5 0:0:0"
        })
        self.assertEqual(response.status_code, 302)

    def test_attendanceOut(self):
        emp = self.create_emp()
        response = self.client.post(reverse('attendanceOut'), {
            'id': emp.id,
            'out': "2021-6-3 0:0:10"
        })
        self.assertEqual(response.status_code, 302)

    def test_attendance(self):
        emp = self.create_emp()
        response = self.client.post(reverse('attendance'), {
            'id': emp.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeAttendance.html')

    def test_HRAttendance(self):
        response = self.client.post(reverse('HRattendance'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HRAttendance.html')
