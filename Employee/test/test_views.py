from django.test import TestCase, Client
from django.urls import reverse

from Employee.models import empTable


class TestEmployeeViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('empregister')
        self.details_url = reverse('details')
        self.edit_url = reverse('edit')
        self.employeeEdit_url = reverse('employeeEdit')
        self.update_url = reverse('update')
        self.employeeUpdate_url = reverse('employeeUpdate')

    def create_emp(self):
        return empTable.objects.create(name="test name", address="test,, address", phone=123, email="test@email",
                                       designation="null", password=123)

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeRegistration.html')

    def test_register_POST(self):
        response = self.client.post(self.register_url, {
            'name': 'test name',
            'address': 'test,, address',
            'phone': 123,
            'email': 'test@email',
            'designation': 'null'

        })
        self.assertEqual(response.status_code, 302)

    def test_register_address_validation_POST(self):
        response = self.client.post(self.register_url, {
            'name': 'test name',
            'address': 'test, address',
            'phone': 123,
            'email': 'test@email',
            'designation': 'null'

        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeRegistration.html')

    def test_register_name_validation_POST(self):
        response = self.client.post(self.register_url, {
            'name': 'test',
            'address': 'test,, address',
            'phone': 123,
            'email': 'test@email',
            'designation': 'null'

        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeRegistration.html')

    def test_details(self):
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Details.html')

    def test_edit(self):
        emp = self.create_emp()
        response = self.client.post(self.edit_url, {
            'id': emp.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Update.html')

    def test_employeeEdit(self):
        emp = self.create_emp()
        response = self.client.post(self.employeeEdit_url, {
            'id': emp.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeUpdate.html')

    def test_update(self):
        emp = self.create_emp()
        response = self.client.post(self.update_url, {
            'id': emp.id,
            'name': 'test name',
            'address': 'test,, address',
            'phone': 123,
            'email': 'test@email',
            'designation': 'null'

        })
        self.assertEqual(response.status_code, 302)

    def test_update_address_validation(self):
        emp = self.create_emp()
        response = self.client.post(self.update_url, {
            'id': emp.id,
            'name': 'test name',
            'address': 'test, address',
            'phone': 123,
            'email': 'test@email',
            'designation': 'null'

        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Update.html')

    def test_update_name_validation(self):
        emp = self.create_emp()
        response = self.client.post(self.update_url, {
            'id': emp.id,
            'name': 'test',
            'address': 'test,, address',
            'phone': 123,
            'email': 'test@email',
            'designation': 'null'

        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Update.html')

    def test_employeeUpdate(self):
        emp = self.create_emp()
        response = self.client.post(self.employeeUpdate_url, {
            'id': emp.id,
            'name': 'test name',
            'address': 'test,, address',
            'phone': 123,
            'email': 'test@email',

        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeProfile.html')

    def test_employeeUpdate_address_validation(self):
        emp = self.create_emp()
        response = self.client.post(self.employeeUpdate_url, {
            'id': emp.id,
            'name': 'test name',
            'address': 'test, address',
            'phone': 123,
            'email': 'test@email',

        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeUpdate.html')

    def test_employeeUpdate_name_validation(self):
        emp = self.create_emp()
        response = self.client.post(self.employeeUpdate_url, {
            'id': emp.id,
            'name': 'test',
            'address': 'test,, address',
            'phone': 123,
            'email': 'test@email',

        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EmployeeUpdate.html')
