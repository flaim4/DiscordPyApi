import requests

class Friend:
    def __init__(self, token):
        self._header = {
            "Authorization": token
        }

    def get_list_frends(self):
        url = "https://discord.com/api/v9/users/@me/relationships"
        response = requests.get(url=url, headers=self._header)

        return response.text