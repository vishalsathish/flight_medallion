import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

MY_API_KEY = os.getenv("VISH_API_KEY")

params = {
    'access_key': MY_API_KEY
}

url = "https://api.aviationstack.com/v1/flights"

fetch_data = requests.get(url, params=params)

fetch_data_json = fetch_data.json()

# print(fetch_data_json)

with open("sample_flight_2.json", "w") as file:
    json.dump(fetch_data_json, file, indent=4)