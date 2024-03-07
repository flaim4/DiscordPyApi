import requests
import json

class User:
    def __init__(self, token):
        self._header = {
            "Authorization": token
        }
    
    def user_name(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("username")
    
    def user_global_name(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("global_name")
    
    def user_bio(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("bio")