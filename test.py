from user import User
from data import Data
import unittest


class TestValidItems(unittest.TestCase):

    u = User()
    d = Data()

    def test_invalid_age(self):
        valid_age_item = self.u.valid_age(age="e")
        self.assertFalse(valid_age_item)

    def test_valid_age(self):
        valid_age_item = self.u.valid_age(age=3)
        self.assertTrue(valid_age_item)

    def test_invalid_email_1(self):
        valid_email_item = self.u.valid_email(email="edwardcorreo")
        self.assertFalse(valid_email_item)

    def test_invalid_email_2(self):
        valid_email_item = self.u.valid_email(email="@edward.correo")
        self.assertFalse(valid_email_item)

    def test_invalid_email_3(self):
        valid_email_item = self.u.valid_email(email="edwardcorreo.com")
        self.assertFalse(valid_email_item)

    def test_valid_email_1(self):
        valid_email_item = self.u.valid_email(email="edward@correo.com")
        self.assertTrue(valid_email_item)
    
    def test_valid_email_2(self):
        valid_email_item = self.u.valid_email(email="edward@correo.com.co")
        self.assertTrue(valid_email_item)

    def test_valid_user(self):
        valid_user = self.u.set_user(idu=2,name="camilo",lastname="arango",age=22,email="ca@mail.com")
        self.assertTrue(valid_user)
    
    def test_invalid_user_age(self):
        valid_user = self.u.set_user(idu=2,name="camilo",lastname="arango",age="ee",email="ca@mail.com")
        self.assertEqual(valid_user,["La edad debe ser un Numero"])

    def test_invalid_user_email(self):
        valid_user = self.u.set_user(idu=2,name="camilo",lastname="arango",age=22,email="camail.com")
        self.assertEqual(valid_user,["El formato de email debe ser abcde@abcde.ab.abc o abcde@abcde.abc; caracteres aceptados .!#$%&'*+/=?^_`{|}~-"])