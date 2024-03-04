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
    
    def reply_message_channel(self, channel_id , message_id, message):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        payload = json.dumps({
            "content": message,
            "message_reference": {
                "channel_id": channel_id,
                "message_id": message_id
            }
        })
        response = requests.post(url=url, headers=self._header, data=payload)

        return response.text
    
    def delate_message_channel(self, channel_id, message_id ):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
        respose = requests.delete(url=url, headers=self._header)
        
        return respose.text