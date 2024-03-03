import requests
import json

class Message:

    def __init__(self, token):
        self._header = {
            "Authorization": token,
            "Content-Type": 'application/json',
        }

    def send_message_channel(self, channel_id, message):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

        payload = json.dumps({
            "content": message
        })

        response = requests.post(url, headers=self._header, data=payload)

        return response.text