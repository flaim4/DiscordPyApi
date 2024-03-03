import requests
import json

class Author:
    
    def __init__(self, token):
        self._header = {
            "Authorization": token
        }
        self._user_data = self._fetch_user_data()


    def _fetch_user_data(self):
        response = requests.get(url="https://discord.com/api/v9/users/@me", headers=self._header)
        data = json.loads(response.text)
        return data

    def user_name(self):
        return self._user_data.get("username")
    
    def id(self):
        return self._user_data.get("id")
    
    def global_name(self):
        return self._user_data.get("global_name")