import os
import requests
import json

url = 'https://api.github.com/users/echebotarev/repos'

res = requests.get(url)
with open(f"{os.getcwd()}/repos.json", "w", encoding="utf-8") as file:
    json.dump(res.json(), file)