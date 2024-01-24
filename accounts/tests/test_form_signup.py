from django.test import TestCase

from accounts.forms import SignUpForm

# tests
class SignUpFormTest(TestCase):

    def test_form_has_field(self):
        form = SignUpForm()
        expected = ["username", "email", "password1", "password2"]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)