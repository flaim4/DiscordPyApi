import requests
import json

class Friend:
    def __init__(self, token):
        self._header = {
            "Authorization": token
        }

    def get_list_frends(self):
        url = "https://discord.com/api/v9/users/@me/relationships"
        response = requests.get(url=url, headers=self._header)
        return response.text
    
    def get_list_id_frends(self):
        url = "https://discord.com/api/v9/users/@me/relationships"
        response = requests.get(url=url, headers=self._header)
        data = json.loads(response.text)
        return [friend["id"] for friend in data]
    
    def get_list_global_name_frends(self):
        url = "https://discord.com/api/v9/users/@me/relationships"
        response = requests.get(url=url, headers=self._header)
        data = json.loads(response.text)
        return [friend["user"]["global_name"] for friend in data]
    
    def get_list_username_frends(self):
        url = "https://discord.com/api/v9/users/@me/relationships"
        response = requests.get(url=url, headers=self._header)
        data = json.loads(response.text)
        return [friend["user"]["username"] for friend in data]