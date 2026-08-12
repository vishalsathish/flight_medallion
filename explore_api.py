import requests
import json

params = {
    'access_key': MY_ACCESS_KEY
}

url = "https://api.aviationstack.com/v1/flights"

fetch_data = requests.get(url, params=params)

fetch_data_json = fetch_data.json()

# print(fetch_data_json)

with open("sample_flight.json", "w") as file:
    json.dump(fetch_data_json, file, indent=4)