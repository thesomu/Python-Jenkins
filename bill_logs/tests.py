from django.test import TestCase, Client
from django.urls import reverse
from bill_logs.models import *

# Create your tests here.

class ExportsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.details_url = reverse('export_bill')
        
    def create_export(self):
        return Export.objects.create(billing_amt="4500",date_of_export="25 sept 2021",gst_imposed="18%",exported_to="xyz company",
        order_ID="1597",quantity="45",estimated_time="5 days")
    
    def test_create_export(self):
        e=self.create_export()
        self.assertTrue(isinstance(e,Export))
    
    def test_details(self):
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exported_bill.html')

    def test_edit(self):
        emp = self.create_export()

        response = self.client.post(reverse('edit_export'), {
            'id': emp.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')   
    
    def test_update(self):
        emp = self.create_export()
        response = self.client.post(reverse('update_export'), {
            'id': emp.id,
            'billing_amt': 8555,
            'date_of_export':"29 sept 2021",
            'gst_imposed':"18%",
            'exported_to':"xyz company",
            ' order_ID':"1597",
            'quantity':"85",
            'estimated_time':"9 days"
           })
        self.assertEqual(response.status_code, 302)      

class ImportsTestCase(TestCase):
    def create_Import(self):
        return imported.objects.create(billing_amt="8500",date_of_import="29 oct 2021",gst_imposed="18%",imported_from="abc company",
        order_ID="1892",quantity="50",estimated_time="8 days")
    
    def test_create_Imported(self):
        e=self.create_Import()
        self.assertTrue(isinstance(e,imported))

    
     