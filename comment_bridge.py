from message import Message

class Comment:
    def __init__(self, message):
        self.author = Author(message.user.name)
        self.body = message.text
        if (len(self.body) == 0):
            self.body = '...'
        self.score = 0

class Author:
    def __init__(self, name):
        self.name = name