import requests
import json
import useful

# WikiLibs AI Client python module

API_URL = "https://wikilibs-dev-api.azurewebsites.net"


class AIClient:
    def GetToken(sefl):
        # Authenticate with the server
        headers = {
            "Authorization": useful.apikey,
        }
        loginJson = {
            "email": "wikilibs@yuristudio.net",
            "password": "wikilibs-parser"
        }
        res = requests.post(API_URL + "/auth/internal/login", headers=headers, json=loginJson)
        if (res.status_code != 200):
            raise ConnectionError("Authorization token rejected")

        # Extract bearer token string
        token = res.text[1:-1]
        return token

    def PushSymbol(self, obj):
        x = obj.get_JSON()
        y = json.loads(x)

        token = self.GetToken()
        # Post a new symbol
        headers = {
            "Authorization": "Bearer " + token
        }
        res = requests.post(API_URL + "/symbol", headers=headers, json=y)
        if (res.status_code != 200):
            raise IOError(res.text)

    def CallOptimizer(self):
        token = self.GetToken()

        # Call optimizer
        headers = {
            "Authorization": "Bearer " + token
        }
        res = requests.patch(API_URL + "/symbol/optimize", headers=headers)
        if (res.status_code != 200):
            raise IOError(res.text)
