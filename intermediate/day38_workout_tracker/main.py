import datetime
import requests
import os

# Posts exercises to this Google Sheet:
# https://docs.google.com/spreadsheets/d/1ImDFggnebnFG0XryHDeRqNrDKl7DmwC3tOT934lnj5c/edit#gid=0


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")

exercise_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEETY")

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}


exercise_string = input("Tell me which exercises you did today: ")

exercise = {
    "query": exercise_string
}

response = requests.post(exercise_endpoint, json=exercise, headers=exercise_headers)
exercises = response.json()
print(exercises)

for exercise in exercises:
    exercise_data = {
        "workout": {
        "date": datetime.datetime.now().date().strftime("%d/%m/%Y"),
        "time": datetime.datetime.now().time().strftime("%H:%M:%S"),
        "exercise": exercise["name"].title(),
        "duration": float(exercise["duration_min"]),
        "calories": float(exercise["nf_calories"])
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=exercise_data, headers=sheety_headers)
