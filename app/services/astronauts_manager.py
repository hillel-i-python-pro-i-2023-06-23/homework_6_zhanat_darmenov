import json
import requests


def read_web_json_file():
    response = requests.get("http://api.open-notify.org/astros.json")

    extraction = json.loads(response.text)

    return extraction["number"]
