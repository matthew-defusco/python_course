import os
import requests
from dotenv import load_dotenv

load_dotenv()
SECRET_TOKEN = os.environ["SHEETY_FLIGHT_TOKEN"]

class DataManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.sheety_headers = {
            "Authorization": f"Bearer {SECRET_TOKEN}"
        }

    def get_records(self):
        return requests.get(self.base_url, headers=self.sheety_headers)

    def update_record(self, id, data):
        url = self.base_url + f"/{id}"
        response = requests.put(url=url, json=data, headers=self.sheety_headers)



