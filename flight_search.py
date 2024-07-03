import os
import requests
import datetime as dt
from dotenv import load_dotenv
from data_manager import DataManager
from notification_manager import send_message

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
URL_Flight = "https://test.api.amadeus.com/v2/shopping/flight-offers"
URL_Auth = "https://test.api.amadeus.com/v1/security/oauth2/token"
URL_City = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

headers_auth = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data_auth = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET
}

params_city = {
    "keyword": "PARIS",
    "max": 1,
    "include": ["AIRPORTS"]
}

params_flight = {
    "originLocationCode": "TBS",
    "destinationLocationCode": " ",
    "departureDate": "2024-12-13",
    "adults": 1
}


def get_auth_token():
    response = requests.post(url=URL_Auth, headers=headers_auth, data=data_auth)
    response_data = response.json()
    return response_data["access_token"]


class FlightSearch:
    def __init__(self):
        self.token = get_auth_token()

    def get_city_data(self, params):
        headers = {
            "Authorization": "Bearer " + self.token
        }
        response = requests.get(url=URL_City, params=params, headers=headers)
        return response.json()["data"][0]["iataCode"]

    def get_flights_data(self, params):
        results = []
        today = dt.datetime.now()
        day_counter = 1
        headers = {
            "Authorization": "Bearer " + self.token
        }

        for i in range(day_counter):
            today = today + dt.timedelta(days=1)
            today_formatted = today.strftime("%Y-%m-%d")
            params_flight["departureDate"] = today_formatted
            response = requests.get(url=URL_Flight, params=params, headers=headers)
            price = response.json()["data"][0]["price"]["total"]
            results.append((today_formatted, price, params_city["keyword"]))
        best_deal = results[0]
        min_price = best_deal[1]
        for item in results:
            if item[1] < min_price:
                min_price = item[1]
                best_deal = item
        return best_deal

    def get_deals(self):
        current = DataManager().get_rows()
        for city, price in current.items():
            params_city["keyword"] = city.upper()
            destination = self.get_city_data(params=params_city)
            params_flight["destinationLocationCode"] = destination
            lowest_current = self.get_flights_data(params_flight)
            if float(price) > float(lowest_current[1]):
                send_message(str(lowest_current))


if __name__ == "__main__":
    flight_search = FlightSearch()
    flight_search.get_deals()
