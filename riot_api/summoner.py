import requests
from config import RIOT_API_KEY

def get_summoner_by_name(summoner_name, platform):
    url = f"https://{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
