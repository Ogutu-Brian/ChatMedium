from user.user import User, UserCollection
from comments.comment import Comment
class Moderator(User):
    
    def __init__(self):
        super.__init__()
        self.comment = Comment()
    def edit_comment(self,comment_id,message):
        """ allow moderator to edit comment"""
        # comment = Commment().edit_comment(comment_id, message)

    def delete_comment(self):
        pass