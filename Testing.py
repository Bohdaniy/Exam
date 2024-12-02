import unittest
from main import find_all_emails

class TestFindAllEmails(unittest.TestCase):
    def test_multiple_emails(self):
        result = find_all_emails("Emails: first@example.com, second@domain.org.")
        self.assertEqual(result, ["first@example.com", "second@domain.org"])

    def test_single_email(self):
        result = find_all_emails("Contact: single@example.com")
        self.assertEqual(result, ["single@example.com"])

    def test_no_email(self):
        with self.assertRaises(ValueError) as context:
            find_all_emails("This text has no email.")
        self.assertEqual(str(context.exception), "No email addresses found in the input string.")

    def test_email_with_special_characters(self):
        result = find_all_emails("Contact: user.name+tag+sorting@example.com")
        self.assertEqual(result, ["user.name+tag+sorting@example.com"])

    def test_email_at_start_and_end(self):
        result = find_all_emails("admin@domain.org is admin and support@helpdesk.com.")
        self.assertEqual(result, ["admin@domain.org", "support@helpdesk.com"])

    def test_no_match_but_similar_text(self):
        with self.assertRaises(ValueError) as context:
            find_all_emails("This is not an email: user@com or @example.")
        self.assertEqual(str(context.exception), "No email addresses found in the input string.")

    def test_emails_with_numbers_and_dots(self):
        result = find_all_emails("Please email 123.user@company.co.uk or support123@service.io.")
        self.assertEqual(result, ["123.user@company.co.uk", "support123@service.io"])

if __name__ == "__main__":
    unittest.main()
