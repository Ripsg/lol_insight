import requests   
from config import RIOT_API_KEY

#Function to extract the account by the riot ID using the library request for the http petition and connecting to the RIOT's API 
#headers parameter help to guide the get/post etc request in order to guide the server
#In how to procced with the request, so the header acts as a dictionary 
#The raise for status method helps to check the HTTP status code of a response
#and raises a httperror exception if the request was unsuccessful

def get_account_by_riot_id(game_name, tag_line, routing):  
    print("API KEY:", RIOT_API_KEY) 
    url = f"https://{routing}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": RIOT_API_KEY}   
    response = requests.get(url, headers=headers) 
    response.raise_for_status()                   
    return response.json()                        
                                                  
