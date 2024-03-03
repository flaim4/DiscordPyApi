import requests
import json

class User:

    def __init__(self, token):
        self._header = {
            "Authorization": token
        }
    
    def id(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("id")
    
    def username(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("username")
    
    def global_name(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("global_name")
    
    def avatar(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("avatar")

    def avatar_decoration_data(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("avatar_decoration_data")
    
    def public_flags(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("public_flags")
    
    def flags(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("flags")
    
    def banner(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("banner")

    def banner_color(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("banner_color")

    def accent_color(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("accent_color")
    
    def bio(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user", {}).get("bio")
    
    def connected_accounts(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("connected_accounts")
    
    def premium_since(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("premium_since")
    
    def premium_type(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("premium_type")
    
    def premium_guild_since(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("premium_guild_since")
    
    def profile_themes_experiment_bucket(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("profile_themes_experiment_bucket")
    
    def pronouns(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("user_profile", {}).get("pronouns")
    
    def guild_badges(self , user_id):
        response = requests.get(url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", headers=self._header)
        data = json.loads(response.text)
        return data.get("guild_badges")
    
    def badges_id(self, user_id):
        response = requests.get(
            url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false",
            headers=self._header
        )
        data = response.json()
        badges = data.get("badges", [])
            
        first_badge = badges[0]
        return first_badge.get("id")
    
    def badges_description(self, user_id):
        response = requests.get(
            url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false",
            headers=self._header
        )
        data = response.json()
        badges = data.get("badges", [])
            
        first_badge = badges[0]
        return first_badge.get("description")

    
    def badges_icon(self, user_id):
        response = requests.get(
            url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false",
            headers=self._header
        )
        data = response.json()
        badges = data.get("badges", [])
            
        first_badge = badges[0]
        return first_badge.get("icon")
    
    def badges_link(self, user_id):
        response = requests.get(
            url=f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends_count=false",
            headers=self._header
        )

        data = response.json()
        badges = data.get("badges", [])
            
        first_badge = badges[0]
        return first_badge.get("link")
