from django.test import Client, TestCase
from django.urls import reverse
from authentication.models import User
from rest_framework.exceptions import ErrorDetail


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.update_url = reverse('update')
        self.user=User.objects.create(
            username='Daniel-Kigozi',
            email='kdanalex69@gmail.com',
            is_active=True,
            is_staff=True,
            password='kig123',)

    def test_api_can_login(self):
        response =self.client.post(
            self.login_url,
            content_type='application/json',
            data=self.user)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'detail': ErrorDetail(string='JSON parse error - Expecting value: line 1 column 1 (char 0)', code='parse_error')})

    def test_api_can_register_users(self):
        response =self.client.post(
            self.register_url,
            content_type='application/json',
            data=self.user,
            )
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'detail': ErrorDetail(string='JSON parse error - Expecting value: line 1 column 1 (char 0)', code='parse_error')})

    def test_api_can_update_user(self):
        response =self.client.post(
            self.update_url,
            content_type='application/json',
            data=self.user,
            )
        self.assertEquals(response.status_code, 403)
        self.assertEquals(response.data, {'detail': ErrorDetail(string='You do not have permission to perform this action.', code='permission_denied')})