import os
import requests

SECRET_TOKEN = os.environ["SHEETY_FLIGHT_TOKEN"]

class DataManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.sheety_headers = {
            "Authorization": f"Bearer {SECRET_TOKEN}"
        }

    def get_flight_records(self):
        return requests.get(f"{self.base_url}/prices", headers=self.sheety_headers)

    def get_user_records(self):
        return requests.get(f"{self.base_url}/users", headers=self.sheety_headers)

    def update_flight_record(self, id, data):
        url = f"{self.base_url}/{id}"
        response = requests.put(url=url, json=data, headers=self.sheety_headers)



