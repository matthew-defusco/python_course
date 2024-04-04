import requests
from datetime import datetime

USERNAME = "defuscom"
TOKEN = "nhyejwkdufb222"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Create User
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create Graph
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Pages Read",
#     "unit": "Pages",
#     "type": "int",
#     "color": "ajisai"
# }
#

#
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post to Graph
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime(year=2024, month=4, day=3)
#
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50"
}
#
# response = requests.post(pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "45"
}

# response = requests.put(pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

response = requests.delete(pixel_delete_endpoint, headers=headers)
print(response.text)
