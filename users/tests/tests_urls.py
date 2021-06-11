from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import home, customer, register, dashboard, login, logout, Profile, shipping


class TestUrls(SimpleTestCase):

    def test_home_urls_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_customer_urls_is_resolved(self):
        url = reverse('customer')
        print(resolve(url))
        self.assertEquals(resolve(url).func, customer)

    def test_register_urls_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_login_urls_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_dashboard_urls_is_resolved(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard)

    def test_logout_urls_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout)

    def test_shipping_urls_is_resolved(self):
        url = reverse('shipping')
        print(resolve(url))
        self.assertEquals(resolve(url).func, shipping)

    def test_profile_urls_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, Profile)
