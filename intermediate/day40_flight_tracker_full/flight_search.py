import os
from datetime import datetime, timedelta
import requests

from flight_data import FlightData

API_KEY = os.environ["FLIGHT_SEARCH_KEY"]

class FlightSearch:
    def __init__(self):
        self.base_url = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": API_KEY
        }
        self.date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    def get_iata_code(self, city_name):
        params = {
            "term": city_name,
            "location_types": "city"
        }
        return requests.get(
            f"{self.base_url}/locations/query",
            headers=self.headers, params=params
            ).json()["locations"][0]["code"]

    def search_flights_from_PIT(self, to):
        '''
        Returns price information.
        Uses the "to" param for where you're flying into.
        "start_date" is the beginning of a 6 month range of dates starting from the passed in value.
        "return_date" is the beginning of a 5 day range of dates to return from the trip.
        '''

        tomorrow = datetime.today() + timedelta(days=1)
        six_months_later = tomorrow + timedelta(days=6*30)

        formatted_tomorrow = tomorrow.strftime("%d/%m/%Y")
        formatted_later = six_months_later.strftime("%d/%m/%Y")

        params = {
            "locale": "en",
            "fly_from": "PIT",
            "fly_to": to,
            "date_from": formatted_tomorrow,
            "date_to": formatted_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "USD",
            "max_stopovers": 3,
            "stopover_to": "06:00",
            "limit": 1
        }

        response = requests.get(
                f"{self.base_url}/v2/search",
                headers=self.headers,
                params=params,
                timeout=10
            )

        try:
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                departure_date=str(datetime.strptime(data["local_departure"], self.date_format)),
                arrival_date=str(datetime.strptime(data["local_arrival"], self.date_format)),
                nights=data["nightsInDest"]
            )
            print(f"{''.join(flight_data.destination_city)}: ${flight_data.price}")
            return flight_data
        except IndexError:
            print(f"There are no available flights from {params['fly_from']} to {params['fly_to']}"
                  f"in the time range {params['date_from']} - {params['date_to']}"
                  f" with only {params['max_stopovers']} layovers."
                  )


