import requests
import json

# WikiLibs AI Client python module

API_URL = "https://wikilibs-dev-api.azurewebsites.net"

class AIClient:
    # Create a new AIClient
    # @param apikey the API key to use for authenticating with WikiLibs API Server
    def __init__(self, apikey):
        self.APIKey = apikey

    def PushSymbol(self, obj):
        x = obj.get_JSON()
        y = json.loads(x)

        #Authenticate with the server
        headers = {
            "Authorization": self.APIKey,
        }
        loginJson = {
            "email": "wikilibs@yuristudio.net",
            "password": "wikilibs-parser"
        }
        res = requests.post(API_URL + "/user/login", headers=headers, json=loginJson)
        if (res.status_code != 200):
            raise ConnectionError("Could not obtain authorization token")

        #Extract bearer token string
        token = res.text[1:-1]

        #Post a new symbol
        headers = {
            "Authorization": "Bearer " + token
        }
        res = requests.post(API_URL + "/symbol", headers=headers, json=y)
        if (res.status_code != 200):
            raise IOError(res.text)
