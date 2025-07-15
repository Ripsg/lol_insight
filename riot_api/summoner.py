import requests
from config import RIOT_API_KEY

# Function: get_summoner_by_name
# ------------------------------
# Description:
#   Retrieves detailed information about a summoner using their in-game name.
#   This includes the summoner's unique identifiers (like PUUID, summoner ID, and account ID),
#   which are essential for accessing match history and statistics.
# Parameters:
#   - summoner_name (str): The in-game name of the player (e.g., "Faker").
#   - platform (str): The regional platform routing value (e.g., "na1", "euw1", "kr").
# Returns:
#   - JSON object containing summoner details such as:
#       - id (Summoner ID)
#       - accountId
#       - puuid (used for match history)
#       - name
#       - profileIconId
#       - summonerLevel
# Project Purpose:
#   This is the **entry point** to the tracking workflow.
#   The information returned here (especially the `puuid`) is required to fetch the summoner’s match history,
#   making this function the first step in identifying and analyzing a player.

def get_summoner_by_name(summoner_name, platform):
    url = f"https://{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
