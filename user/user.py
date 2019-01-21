class Role:
    """A template class for user roles"""
    admin = "admin"
    user = "user"
    moderator = "moderator"


class User:
    """A user template class"""

    def __init__(self, first_name="", last_name="", password="", email="", role=""):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.role = role
