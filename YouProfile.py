import requests
import json

class YouProfile:
    def __init__(self, token):
        self._header = {
            "Authorization": token
        }

    def you_name(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self._header)
        data = json.loads(response.text)
        return data.get("username")
    
    def you_id(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self._header)
        data = json.loads(response.text)
        return data.get("id")
    
    def you_global_name(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self._header)
        data = json.loads(response.text)
        return data.get("global_name")
    
    def you_email(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self._header)
        data = json.loads(response.text)
        return data.get("email")

    def you_phone(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self._header)
        data = json.loads(response.text)
        return data.get("phone")
    
    def you_bio(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self._header)
        data = json.loads(response.text)
        return data.get("bio")

