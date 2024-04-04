import os
import requests
from datetime import datetime as dt
from smsapi.client import SmsApiPlClient
from twilio.rest import Client

account_sid = 'ACe72d9ae7e057ed413d18d500320c4ea7'
auth_token = '7463e6bf1663a5b7fa39f5c1672294f0'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18442292913',
  body='Pickles',
  to='+18777804236'
)
#
#
# # api_key = "f1b5128eb0855b44b117292534921138"
# api_key = os.environ.get("OWM_API_KEY")
# # SMS_API_KEY = os.environ.get("SMS_API_KEY")
# SMS_API_KEY = "1UlZHyXobaj813DvZ72qi1DQJUYFjo2smgescYzJ"
# OWM_Geo = "http://api.openweathermap.org/geo/1.0/direct"
# OWM_Forecast = "http://api.openweathermap.org/data/2.5/forecast"
# sms_client = SmsApiPlClient(access_token=SMS_API_KEY)
# send_results = sms_client.sms.send(to="+14128491482", message="This is a test message")
# print(send_results)
# #
# # # loc_response = requests.get(
# # #     f"http://api.openweathermap.org/geo/1.0/direct?q=Pittsburgh,PA,US&appid={api_key}")
# # geo_params = {
# #     "q": "Pittsburgh,PA,US",
# #     "appid": api_key
# # }
# # loc_response = requests.get(OWM_Geo, params=geo_params)
# # loc_response.raise_for_status()
# #
# # loc_data = loc_response.json()[0]
# # lat = loc_data["lat"]
# # lon = loc_data["lon"]
# #
# # forcast_params = {
# #     "lat": lat,
# #     "lon": lon,
# #     "cnt": 4,  # Returns only the top 4 results from the list (12 hours worth of data)
# #     "appid": api_key
# # }
# #
# # forecast_response = requests.get(OWM_Forecast, params=forcast_params)
# # forecast_response.raise_for_status()
# # forecast_data = forecast_response.json()["list"]
# #
# # will_rain = False
# #
# # for time in forecast_data:
# #     for weather in time["weather"]:
# #         if int(weather["id"]) < 700:
# #             will_rain = True
# #
# # if will_rain:
# #     print("Bring an umbrella!")
# #     # Make the API call to Twilio or WhatsApp or Telegram or whatever
# #     # Didn't follow the steps here because Twilio doesn't work the way it's described in the course
