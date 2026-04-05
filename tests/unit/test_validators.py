import unittest
from app.utils.validators import validate_email, validate_password_strength, sanitize_input

class TestValidators(unittest.TestCase):
    def test_valid_email_formats(self):
        """Test a variety of correct email formats [cite: 397-400]"""
        self.assertTrue(validate_email('user@example.com'))
        self.assertTrue(validate_email('test.user@domain.co.uk'))

    def test_invalid_email_formats(self):
        """Test known bad email formats [cite: 404-406]"""
        self.assertFalse(validate_email('invalid-email'))
        self.assertFalse(validate_email('@no-user.com'))

    def test_password_strength(self):
        """Test security requirements [cite: 415-420]"""
        self.assertFalse(validate_password_strength('short')) # Too short
        self.assertFalse(validate_password_strength('NoNumbers!')) # Missing digit
        self.assertTrue(validate_password_strength('SecurePass123!')) # Valid

    def test_sanitize_input(self):
        """Verify HTML tags are escaped [cite: 428-432]"""
        dirty = "<script>alert('xss')</script>"
        clean = sanitize_input(dirty)
        self.assertNotIn("<script>", clean)
        self.assertIn("&lt;script&gt;", clean)