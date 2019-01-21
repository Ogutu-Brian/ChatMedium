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
        self.id = ""
        self.full_name = self.first_name+" "+self.last_name

    def to_dictionary(self):
        """Rpresents the user data in dictionary"""
        result = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "password": self.password,
            "email": self.email,
            "role": self.role
        }
        return result


class UserCollection:
    """A class for storing user data"""

    def __init__(self):
        self.user_data = {}
        self.id = 1

    def add_user(self, user):
        """Adds a user data"""
        user.id = self.id
        self.user_data[user.id] = user
        self.id += 1

    def query_by_id(self, item_id):
        """Queries a user by the user id"""
        response = None
        for item in self.user_data.values():
            if item.id == item_id:
                response = item
        return response
