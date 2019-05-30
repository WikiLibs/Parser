import requests
import json
import useful

# WikiLibs AI Client python module

API_URL = "https://wikilibs-dev-api.azurewebsites.net"

class AIClient:
    def PushSymbol(self, path, obj):
        x = obj.get_JSON()
        y = json.loads(x)

        #Authenticate with the server
        headers = {
            "Authorization": useful.apikey,
        }
        loginJson = {
            "email": "wikilibs@yuristudio.net",
            "password": "wikilibs-parser"
        }
        res = requests.post(API_URL + "/auth/internal/login", headers=headers, json=loginJson)
        if (res.status_code != 200):
            raise ConnectionError("Could not obtain authorization token")

        #Extract bearer token string
        token = res.text[1:-1]

        #Post a new symbol
        headers = {
            "Authorization": "Bearer " + token
        }
        y.path = path #TODO : remove when merging with Vic branch
        res = requests.post(API_URL + "/symbol", headers=headers, json=y)
        if (res.status_code != 200):
            raise IOError(res.text)
