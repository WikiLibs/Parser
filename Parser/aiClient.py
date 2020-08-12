import requests
import json
import time
import useful
import urllib.parse

# WikiLibs AI Client python module

VERIFY = True # Set to false when working with local API
#API_URL = "https://localhost:5001"
API_URL = "https://wikilibs-dev-api.azurewebsites.net"
APP_KEY = ""
APP_ID = "3aed2d8a-9b87-40d1-a124-b9827d7536d2"
SEC = "uM4&~tU6/\"fY5;çlQ1%ùwV8@"


class AIClient:
    def __init__(self, apikey, appID, secret):
        self._apikey = apikey
        self._appID = appID
        self._secret = secret
        self._token = ""
        self._time = 0.0

    def GetToken(self):
        useful.printVerbose("Getting bearer token")
        # Authenticate with the server
        headers = {
            "Authorization": self._apikey,
        }
        loginJson = {
            "appId": APP_ID,
            "appSecret": SEC
        }
        res = requests.post(API_URL + "/auth/bot", headers=headers, json=loginJson, verify=VERIFY)
        if (res.status_code != 200):
            raise ConnectionError("Authorization token rejected " + str(res.status_code) + "\n"
                                  + res.text)

        # Extract bearer token string
        self._token = res.text[1:-1]

        # Get Time
        self._time = time.time()

    def RefreshToken(self):  # WIP tant que nicof n'est pas là
        useful.printVerbose("Refreshing bearer token")
        # Refreshing bearer token
        headers = {
            "Authorization": "Bearer " + self._token,
        }
        res = requests.patch(API_URL + "/auth/refresh", headers=headers, verify=VERIFY)
        if (res.status_code != 200):
            raise ConnectionError("Authorization token rejected")

        # Extract bearer token string
        self._token = res.text[1:-1]

    def CheckIfRefresh(self):
        useful.printVerbose("Check if need refresh token")
        # Check if time elapsed > 3min
        if (time.time() - self._time > 180):
            self.RefreshToken()

    def PushSymbol(self, obj):
        x = obj.get_JSON()
        data = json.loads(x)

        if self._token == "":
            raise ConnectionError("No token")

        self.CheckIfRefresh()
        # Post a new symbol
        headers = {
            "Authorization": "Bearer " + self._token
        }
        res = requests.put(API_URL + "/symbol/" + urllib.parse.quote(obj.getPath()), headers=headers, json=data, verify=VERIFY)
        print("path = " + API_URL + "/symbol/" + obj.getPath())
        y = json.dumps(x)
        print(x)
        if (res.status_code != 200):
            raise IOError("Invalid request : return code is " + str(res.status_code) + "\n"
                                  + res.text)

    def CallOptimizer(self):
        if self._token == "":
            raise ConnectionError("No token")

        self.CheckIfRefresh()
        useful.printVerbose("Optimizer is being called")
        # Call optimizer
        headers = {
            "Authorization": "Bearer " + self._token
        }
        res = requests.patch(API_URL + "/symbol/optimize", headers=headers, verify=VERIFY)
        if (res.status_code != 200):
            raise IOError(res.text)

    @staticmethod
    def CallOptimizer_ext(apikey):
        useful.printVerbose("Getting bearer token")
        # Authenticate with the server
        headers = {
            "Authorization": apikey,
        }
        loginJson = {
            "appId": APP_ID,
            "appSecret": SEC
        }
        res = requests.post(API_URL + "/auth/bot", headers=headers, json=loginJson, verify=VERIFY)
        if (res.status_code != 200):
            raise ConnectionError("Authorization token rejected")

        # Extract bearer token string
        token = res.text[1:-1]

        useful.printVerbose("Optimizer is being called")
        # Call optimizer
        headers = {
            "Authorization": "Bearer " + token
        }
        res = requests.patch(API_URL + "/symbol/optimize", headers=headers, verify=VERIFY)
        if (res.status_code != 200):
            raise IOError(res.text)
