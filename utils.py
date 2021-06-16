import jwt
import json
import requests


def generate_token(api_key, secret_key):
    payload = {"key": api_key}
    encoded = jwt.encode(payload, secret_key, algorithm="HS256")
    return encoded


def api_push(url, token, message):
    x = requests.post(url, data=json.dumps(message), headers={'Token': token})
    return x
