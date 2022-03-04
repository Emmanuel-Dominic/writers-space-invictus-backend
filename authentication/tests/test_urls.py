from django.test import TestCase
from django.urls import reverse, resolve
from authentication.views import UserRetrieveUpdateAPIView, RegistrationAPIView, LoginAPIView

class TestUrls(TestCase):

    def test_user_url_is_resolved(self):
        url = reverse('update')
        self.assertEquals(resolve(url).func.view_class, UserRetrieveUpdateAPIView)

    def test_user_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegistrationAPIView)

    def test_user_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginAPIView)
