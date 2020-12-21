import requests
import json

url = "https://na1.api.riotgames.com/lol/match/v4/matches/3685845648"
matchId = 3685845648
payload={}

#Need to update every time I run this
API_Key = "RGAPI-8684d48d-05f8-4a1c-916e-90805cf080e5"

headers = {
    'X-Riot-Token': API_Key
}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = response.text

json_object = json.loads(json_data)

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)

#print(response.text)
