import requests
import json
import time
import useful

# WikiLibs AI Client python module

API_URL = "https://wikilibs-dev-api.azurewebsites.net"
APP_KEY = "39d183b2-955f-4d28-90d6-b711e3db355b" # ne pas changer
APP_ID = "96abd6ae-a122-49c0-abbb-278d65d53531"
SEC = "mY3#èvF2,<xT4-çuB6!}nQ8."


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
        print("API key: #" + self._apikey + "#")
        res = requests.post(API_URL + "/auth/bot", headers=headers, json=loginJson)
        if (res.status_code != 200):
            raise ConnectionError("Authorization token rejected " + str(res.status_code) + "\n"
                                  + res.text)

        # Extract bearer token string
        self._token = res.text[1:-1]

        # Get Time
        self._time = time.time()

    def RefreshToken(self):  # WIP tant que nicof n'est pas là
        useful.printVerbose("Refreshing bearer token")
        # # Refreshing bearer token
        # headers = {
        #     "Authorization": self._token,
        # }
        # res = requests.patch(API_URL + "/auth/refresh", headers=headers)
        # if (res.status_code != 200):
        #     raise ConnectionError("Authorization token rejected")

        # # Extract bearer token string
        # self._token = res.text[1:-1]

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
        res = requests.post(API_URL + "/symbol", headers=headers, json=data)
        if (res.status_code != 200):
            raise IOError(res.text)

    def CallOptimizer(self):
        if self._token == "":
            raise ConnectionError("No token")

        self.CheckIfRefresh()
        useful.printVerbose("Optimizer is being called")
        # Call optimizer
        headers = {
            "Authorization": "Bearer " + self._token
        }
        res = requests.patch(API_URL + "/symbol/optimize", headers=headers)
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
        res = requests.post(API_URL + "/auth/bot", headers=headers, json=loginJson)
        if (res.status_code != 200):
            raise ConnectionError("Authorization token rejected")

        # Extract bearer token string
        token = res.text[1:-1]

        useful.printVerbose("Optimizer is being called")
        # Call optimizer
        headers = {
            "Authorization": "Bearer " + token
        }
        res = requests.patch(API_URL + "/symbol/optimize", headers=headers)
        if (res.status_code != 200):
            raise IOError(res.text)
