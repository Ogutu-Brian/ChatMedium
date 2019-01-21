from user.user import User, UserCollection
user_collection = UserCollection()


def login_user(email="", password=""):
    """ add login data"""
    user = user_collection.query_by_field("email")
    response = None
    if not user:
        response = "A user with that email does not exist"
    elif user.password == password:
        response = user
    return response
