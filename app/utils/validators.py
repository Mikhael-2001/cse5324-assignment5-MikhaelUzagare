import re

def validate_email(email):
    """Verifies email format using regex [cite: 396-397]"""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password_strength(password):
    """Ensures password meets security requirements [cite: 415]"""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True

def sanitize_input(text):
    """Basic HTML sanitization to prevent XSS [cite: 428-429]"""
    return text.replace("<", "&lt;").replace(">", "&gt;")