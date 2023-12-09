import requests

parameters = {
    "amount": 10,
    "category": 22,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = [question_info for question_info in data["results"]]
