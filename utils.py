import re


def verify_email(email):
    while not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        # raise ValueError("Email format not invented\
        #    Provide valid email")
        print("Email format not invented\
            Provide valid email")
        email = input("Enter email")

    return email
