from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_case_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful"""
        email = "daniel@ultrapython.net"
        password = "UltraPython1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for new user to see if it's normalized"""
        email = "daniel@UltraPython.NET"
        user = get_user_model().objects.create_user(email, "UltraPython1234")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'UltraPython1234')

    def test_create_new_superuser(self):
        """ Test creating a new super user """
        user = get_user_model().objects.create_superuser('admin@ultrapython.net', 'UltraPython1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
