from django.test import TestCase, testcases
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        # test creating a new user with an email is successfull
        temail = 'test@gmail.com'
        tpassword = 'test123'
        user = get_user_model().objects.create_user(
            email=temail,
            password=tpassword
        )
        self.assertEqual(user.email,temail)
        self.assertTrue(user.check_password,tpassword)
    def test_new_user_email_normalized(self):
        email = "test@gmail.com"
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')
    
    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
    