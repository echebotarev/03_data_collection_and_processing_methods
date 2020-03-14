import os
import json
import requests

url = 'https://api.github.com/user'
user = input('Введите имя пользователя:')
pwd = input('Введите пароль:')

res = requests.get(url, auth=(user, pwd))

with open(f"{os.getcwd()}/response_auth.json", "w", encoding="utf-8") as file:
    json.dump(res.json(), file)