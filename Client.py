from .YouProfile import YouProfile
from .User import User
from .Guild import Guild
from .Friend import Friend
from .Message import Message

class Client(YouProfile, User, Guild, Friend, Message):
    def __init__(self, token):
        super().__init__(token)