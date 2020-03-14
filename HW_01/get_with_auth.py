import os
import json
import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.github.com/user'
user = 'echebotarev'
client_secret = 'df936a39afbc25691b18e9e513b58f499c7221d9'

res = requests.get(url,auth=HTTPBasicAuth(user, client_secret))

with open(f"{os.getcwd()}/response_auth.json", "w", encoding="utf-8") as file:
    json.dump(res.json(), file)