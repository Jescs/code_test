import requests
import json

def login(url, data):
    s = requests.post(url, data=data)
    return s

