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
    
    def avatar(self):
        return self._user_data.get("avatar")
    
    def discriminator(self):
        return self._user_data.get("discriminator")
    
    def public_flags(self):
        return self._user_data.get("public_flags")
    
    def premium_type(self):
        return self._user_data.get("premium_type")
    
    def flags(self):
        return self._user_data.get("flags")
    
    def banner(self):
        return self._user_data.get("banner")
    
    def accent_color(self):
        return self._user_data.get("accent_color")
    
    def avatar_decoration_data(self):
        return self._user_data.get("avatar_decoration_data")
    
    def banner_color(self):
        return self._user_data.get("banner_color")
    
    def mfa_enabled(self):
        return self._user_data.get("mfa_enabled")
    
    def locale(self):
        return self._user_data.get("locale")
    
    def email(self):
        return self._user_data.get("email")
    
    def verified(self):
        return self._user_data.get("verified")

    def phone(self):
        return self._user_data.get("phone")
    
    def nsfw_allowed(self):
        return self._user_data.get("nsfw_allowed")

    def linked_users(self):
        return self._user_data.get("linked_users")
    
    def bio(self):
        return self._user_data.get("bio")

    def authenticator_types(self):
        return self._user_data.get("authenticator_types")
