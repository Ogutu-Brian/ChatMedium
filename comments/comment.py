'''Module representing the comments'''
from datetime import datetime

COMMENTS = []

class Comment:
    '''Defintions for the comment entity'''
    def __init__(self, author, message):
        self.comment_id = len(COMMENTS) + 1
        self.author = author
        self.message = message
        self.created_at = str(datetime.now())

    def save(self, comment):
        '''Save a comment to the comments list'''
        COMMENTS.append(comment)

    @staticmethod
    def find_comment_by_author(author):
        '''Find a comment by author'''
        comment = {}
        for index, _ in enumerate(COMMENTS):
            if COMMENTS[index].get(author) == author:
                comment = COMMENTS[index]
        return comment

    def comment_to_dict(self):
        '''Return a dictionary of the comments object'''
        return {
            'author': self.author,
            'message': self.message,
            'created_at': self.created_at
        }
