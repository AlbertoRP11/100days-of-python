import requests
from datetime import datetime

TOKEN = "your token"
USERNAME = "your username"
GRAPH_ID = 'graph1'

# graph_link = "https://pixe.la/v1/users/albertorp/graphs/graph1.html"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime(year=2023, month=12, day=10).strftime("%Y%m%d")
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": int(input("How many pages did you read today?"))
}

# response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)
# print(response)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

update_data = {
    "quantity": "15"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
