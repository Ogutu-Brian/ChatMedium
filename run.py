from user.user import User, UserCollection
from utils import validate_user
user_collection = UserCollection()


def login_user(email="", password=""):
    """ add login data"""
    user = user_collection.query_by_field("email")
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
