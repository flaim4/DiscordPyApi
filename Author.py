import requests
import json

class Author:
    
    def __init__(self, token):
        self.header = {
            "Authorization": token
        }

    def user_name(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self.header)
        data = json.loads(response.text)
        return data.get("username")

    def id(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self.header)
        data = json.loads(response.text)
        return data.get("id")
    
    def global_name(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self.header)
        data = json.loads(response.text)
        return data.get("global_name")