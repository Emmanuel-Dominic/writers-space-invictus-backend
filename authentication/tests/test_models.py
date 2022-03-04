from django.test import TestCase
from authentication.models import User

class TestModel(TestCase):
    def setUp(self):
        self.user=User.objects.create(
            username="Daniel-Kigozi",
            email="kdanalex69@gmail.com",
            is_active=True,
            is_staff=True,)

    def test_valid_user_model(self):
        self.assertEquals(self.user.username, "Daniel-Kigozi")
        self.assertEquals(self.user.email, "kdanalex69@gmail.com")
        self.assertEquals(self.user.is_active, True)
        self.assertEquals(self.user.is_staff, True)

    def test_invalid_user_model(self):
        self.assertNotEquals(self.user.username, "Bogere-Paul")
        self.assertNotEquals(self.user.email, "pbogere@gmail.com")
        self.assertNotEquals(self.user.is_active, False)
        self.assertNotEquals(self.user.is_staff, False)

    def test_count_user_model(self):
        self.count_user = User.objects.all().count()
        self.assertEquals(self.count_user, 1)







