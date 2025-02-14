# Importa le librerie necessarie
from dotenv import load_dotenv
import os
import requests

load_dotenv()

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")

# Funzione per ottenere il token OAuth
def get_oauth_token():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    return response.json().get('access_token')

# Funzione per ottenere informazioni su uno streamer
def get_streamer_info(n, streamer_name):
    token = get_oauth_token()
    url = 'https://api.twitch.tv/helix/users'
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {token}'
    }
    params = {
        'login': streamer_name
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if data['data']:
        user_info = data['data'][0]
        if n == 1:
            return user_info['profile_image_url']
        elif n == 2:
            return user_info['display_name']
        else:        
            print(f"Description: {user_info['description']}")
            print(f"Total Views: {user_info['view_count']}")
            print(f"Profile Image URL: {user_info['profile_image_url']}")
    else:
        print(f"Nessuno streamer trovato con il nome {streamer_name}")
            