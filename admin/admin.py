from user.user import User
from comments.comment import Comment


class Admin(User):
    """contains the Admin functionalities"""
    def __init__(self):
        super().__init__()

    def edit_comment(self, comment_id, message):
        """contains the edit functionality"""
        comment = Comment.find_comment_by_id(comment_id)
        comment["message"]= message

    def delete_comment(self, comment_id):
        comment = Comment.find_comment_by_id(comment_id)
        comment.clear()
        
