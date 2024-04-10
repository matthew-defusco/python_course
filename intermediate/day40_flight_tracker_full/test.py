import os
import requests

# print(os.environ["SHEETY_FLIGHT_TOKEN"])
response = requests.get(
                f"{os.environ['SHEETY_BASE_URL']}/users",
                headers={"Authorization": f"Bearer {os.environ["SHEETY_FLIGHT_TOKEN"]}"}
            )

users = response.json()["users"]

emails = [user["email"] for user in users]

print(", ".join(emails))