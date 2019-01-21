from user.user import User, UserCollection
from utils import validate_user
user_collection = UserCollection()


def login_user(email="", password=""):
    """ add login data"""
    user = user_collection.query_by_field("email",email)
    response = None
    if user:
        if user.password == password:
            response = user
    return response


def signup(first_name="", last_name="", password="", email=""):
    """A function that creates a user account"""
    response = None
    if user_collection.query_by_field("email", email):
        response = "A user with that email address already exists"
    else:
        user = User(first_name=first_name, last_name=last_name,
                    password=password, email=email)
        if validate_user(user):
            user_collection.add_user(user)
            response = user
    return response


if __name__ == "__main__":
    while True:
        choice = None
        user = None
        print("Welcome to Medium")
        print("Please choose from the menu provided")
        print("1. Sign up")
        print("2. Log in")
        choice = input("Enter choice")
        if not choice:
            print("You did not enter a valid choice")
            break
        if int(choice) == 1:
            first_name = input("Enter first name:")
            last_name = input("Enter last name:")
            password = input("Enter password:")
            email = input("Enter email address:")
            user = signup(first_name=first_name, last_name=last_name,
                          password=password, email=email)
            if user:
                print("Successfully signed up")
        elif int(choice) == 2:
            email = input("Enter email address:")
            password = input("Enter password:")
            user = login_user(email=email, password=password)
            if user:
                print("You successfully logged in")
