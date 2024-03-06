import requests
import json

class Guild:
    def __init__(self, token):
        self._header = {
            "Authorization": token
        }

    def get_guilds(self):
        url="https://discordapp.com/api/users/@me/guilds"
        response = requests.get(url=url, headers=self._header)
        return response.text

    def get_id_guilds(self):
        url="https://discordapp.com/api/users/@me/guilds"
        response = requests.get(url=url, headers=self._header)
        data = json.loads(response.text)
        return [guild["id"] for guild in data]
    
    def get_name_guilds(self):
        url="https://discordapp.com/api/users/@me/guilds"
        response = requests.get(url=url, headers=self._header)
        data = json.loads(response.text)
        return [guild["name"] for guild in data]
    
    def get_channel_guilds(self, guild_id):
        url=f"https://discord.com/api/v9/guilds/{guild_id}/channels"
        response = requests.get(url=url, headers=self._header)
        data = json.loads(response.text)
        return [guild["name"] for guild in data]