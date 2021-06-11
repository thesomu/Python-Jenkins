from django.test import TestCase, Client
from django.urls import reverse
from Import.models import Import, Companies


class ImportModelsTestCase(TestCase):
    """
    """

    def setUp(self):
        """
        """
        self.import1 = Import.objects.create(orderImport_id=5, order_date="2021-10-25", import_product="Jeans",
                                             orderImport_country="America", status_of_import="No", total_cost=20000)
        self.import2 = Import.objects.create(orderImport_id=10, order_date="2021-10-25", import_product="Jacket",
                                             orderImport_country="Japan", status_of_import="No", total_cost=25000)

        Companies.objects.create(
            product_name=self.import1,
            company_id=2,
            company_name="ABC Pvt. Ltd.",
            price_per_piece=1000,
            shipping_cost=5000,
            estimated_dateOfDelivery="2021-9-22"
        )

        Companies.objects.create(
            product_name=self.import2,
            company_id=1,
            company_name="XYZ Pvt. Ltd.",
            price_per_piece=1000,
            shipping_cost=5000,
            estimated_dateOfDelivery="2021-10-22"
        )

    def test_importorderexists(self):
        """
        """
        totalOrders = Import.objects.all()
        self.assertEqual(totalOrders.count(), 2)

    def test_companiesexists(self):
        """
        """
        totalCompanies = Companies.objects.all()
        self.assertEqual(totalCompanies.count(), 2)


class ImportViewsTestCase(TestCase):
    """
    """

    def setUp(self):
        """
        """
        self.client = Client()
        self.session = self.client.session
        self.home_page_url = reverse('portalPage')
        self.login_page_url = reverse('portalLogin')
        self.logout_page_url = reverse('pageLogout')
        self.menu_page_url = reverse('importMain')
        self.import_insert_url = reverse('importOrder')
        self.import_display_url = reverse('showOrders')

    def test_portal_page(self):
        """
        """
        response = self.client.get(self.home_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'importAndExportPortal.html')

    def test_portal_login_POST(self):
        """
        """
        response = self.client.post(self.login_page_url, {
            'user': 'harsh1234',
            'password': '1998'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menuPage.html')

    def test_portal_login_failed_POST(self):
        """
        """
        response = self.client.post(self.login_page_url, {
            'user': 'harsh1234',
            'password': '1999'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_portal_logout(self):
        """
        """
        response = self.client.get(self.logout_page_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_portal_menu_import_POST(self):
        """
        """
        self.session['user'] = 'harsh1234'
        self.session.save()
        response = self.client.post(self.menu_page_url, {
            'imp': 'Import'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'importPage.html')

    def test_portal_menu_export_POST(self):
        """
        """
        self.session['user'] = 'harsh1234'
        self.session.save()
        response = self.client.post(self.menu_page_url, {
            'exp': 'Export'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/displayExportOrders')

    def test_import_order_insert_POST(self):
        """
        """
        self.session['user'] = 'harsh1234'
        self.session.save()
        response = self.client.post(self.import_insert_url, {
            'orderid': 1,
            'orderdate': '2021-10-13',
            'orderCountry': 'London',
            'orderProduct': 'T-Shirt',
            'list': 'Pending',
            'orderCost': 25000
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/displayOrders')

    def test_import_order_insert_GET(self):
        """
        """
        self.session['user'] = 'harsh1234'
        self.session.save()
        response = self.client.get(self.import_insert_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'importPage.html')

    # def test_display_import_order_GET(self):
    #     """
    #     """
    #     self.session['user'] = 'harsh1234'
    #     self.session.save()
    #     response = self.client.get(self.import_display_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'importOrders.html')
