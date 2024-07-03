import os
import requests
from dotenv import load_dotenv

load_dotenv()

Authorization = "Basic " + os.getenv("SHEETY_AUTH_TOKEN")
URL = "https://api.sheety.co/9e5044e53727815a80ce1021b571ade2/flightDeals/prices"

headers = {
    "Authorization": Authorization
}


class DataManager:
    def __init__(self):
        self.result = {}

    def get_rows(self):
        response = requests.get(url=URL, headers=headers)
        for city in response.json()["prices"]:
            self.result[city["city"]] = city["lowestPrice"]
        return self.result
