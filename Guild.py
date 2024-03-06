import requests

class Guild:
    def __init__(self, token):
        self._header = {
            "Authorization": token
        }

    def get_guilds(self):
        url="https://discordapp.com/api/users/@me/guilds"
        response = requests.get(url=url, headers=self._header)
        return response.text