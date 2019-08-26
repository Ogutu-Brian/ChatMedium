import re


def verify_email(email):
    while not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        # raise ValueError("Email format not invented\
        #    Provide valid email")
        print("Email format not invented\
            Provide valid email")

        email = input("Enter email")

    return email

def validate_user(user):
    """Validates user during sign up"""
    errors = []
    if not user.first_name:
        errors.append({
            "error": "A user should be able to provide the first name"
        })
    elif not user.last_name:
        errors.append({
            "error": "A last name must be provivided"
        })
    elif not user.password:
        errors.append({
            "error": "A user password must be given"
        })
    elif not user.email:
        errors.append({
            "error": "A user should be able to provide an email address"
        })
    return len(errors) == 0
