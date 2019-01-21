import re


def verify_email(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        raise ValueError("Email format not invented\
            Provide valid email")
