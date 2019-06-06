import request
import json
import useful

# WikiLibs AI Client python module

API_URL = "https://wikilibs-dev-api.azurewebsites.net"


class AIClient:
    def PushSymbol(self, obj):
        x = obj.get_JSON()
        y = json.loads(x)

        # Authenticate with the server
        headers = {
            "Authorization": useful.apikey,
        }
        loginJson = {
            "email": "wikilibs@yuristudio.net",
            "password": "wikilibs-parser"
        }
        res = request.post(API_URL + "/auth/internal/login", headers=headers, json=loginJson)
        if (res.status_code != 200):
            raise ConnectionError("Could not obtain authorization token")

        # Extract bearer token string
        token = res.text[1:-1]

        # Post a new symbol
        headers = {
            "Authorization": "Bearer " + token
        }
        res = request.post(API_URL + "/symbol", headers=headers, json=y)
        if (res.status_code != 200):
            raise IOError(res.text)

    def CallOptimizer(self):
        headers = {
            "Authorization": useful.apikey,
        }
        loginJson = {
            "email": "wikilibs@yuristudio.net",
            "password": "wikilibs-parser"
        }
        res = request.post(API_URL + "/auth/internal/login", headers=headers, json=loginJson)
        if (res.status_code != 200):
            raise ConnectionError("Could not obtain authorization token")

        # Extract bearer token string
        token = res.text[1:-1]

        # Call optimizer
        headers = {
            "Authorization": "Bearer " + token
        }
        res = request.patch(API_URL + "/symbol/optimize", headers=headers)
        if (res.status_code != 200):
            raise IOError(res.text)
