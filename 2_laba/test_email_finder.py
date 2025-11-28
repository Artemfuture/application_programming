import unittest
from email_checker import validate_email, find_emails_in_text


class TestEmailValidation(unittest.TestCase):

    def test_valid_emails(self):
        valid = [
            "test@example.com",
            "user.name+tag@gmail.com",
            "email123@mail.ru",
            "hello@sub.domain.org",
        ]
        for email in valid:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email))

    def test_invalid_emails(self):
        invalid = [
            "plainaddress",
            "@missingusername.com",
            "john.doe@.com",
            "email@@mail.com",
            "user@mail..com",
        ]
        for email in invalid:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email))

    def test_extraction(self):
        text = "Контакты: admin@mail.ru, support@gmail.com"
        self.assertEqual(
            find_emails_in_text(text), ["admin@mail.ru", "support@gmail.com"]
        )


if __name__ == "__main__":
    unittest.main()
