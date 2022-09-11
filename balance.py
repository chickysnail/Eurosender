import requests
import json
import config

def getToken(mail, pwd):
    url = 'https://www.eurosender.com/api/v1/users/login'
    params = {"username": mail, "password": pwd}

    r = requests.post(url, json=params)
    result = json.loads(r.text)
    token = result["accessToken"]

    return token

def getBalance():
    token = getToken(config.login, config.sitePwd)

    url = 'https://www.eurosender.com/api/v2/me'
    header = {"Authorization": f"Bearer {token}"}

    r = requests.get(url, headers=header)
    accountInfo = json.loads(r.text)
    balance = accountInfo["data"]["creditBalance"]

    return balance
