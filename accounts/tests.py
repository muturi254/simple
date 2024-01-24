from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.views import signup


# Create your tests here.
class SignUpTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        signup_url = resolve("/signup/")
        self.assertEqual(signup_url.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)


class SuccessfulSignUpTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'muturi',
            'password1': 'test@Pass',
            'password2': 'test@Pass',
        }

        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_resirection(self):
        self.assertRedirects(self.response, self.home_url)


    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_form_errrors(self):
        form = self.response.content.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())