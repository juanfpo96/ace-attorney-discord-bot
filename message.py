from discord import Message
import re

class Message:
    def __init__(self, update: Message):
        self.user = User(update.author)
        self.text = re.sub(r'(https?)\S*', '(link)', update.content)

class User:
    def __init__(self, user):
        self.name = user.display_name
        self.id = user.id