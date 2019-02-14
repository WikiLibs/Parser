import requests

# WikiLibs AI Client python module

API_URL = "https://localhost:8080"
API_KEY = "7ad19ee2-db3f-4d1f-95d1-58311c3caf11"

class AIClient:
    # Create a new AIClient
    # @param user the email address of the AI account on WikiLibs
    # @param passwd the password that was given with the email address
    def __init__(self, user, passwd):
        self.User = user
        self.Pass = passwd
    
    def PushSymbol(self, path, json):
        headers = {
            "Authorization": API_KEY,
            "email": self.User,
            "password": self.Pass
        }
        res = requests.post(API_URL + "/user/login", headers=headers)
        if (res.status_code == 401):
            raise ConnectionError("Could not obtain authorization token")
        token = res.text[1:-1]
        headers = {
            "Authorization": "Bearer " + token,
            "path": path
        }
        res = requests.post(API_URL + "/symbol", headers = headers, json = json)
        if (res.status_code == 401):
            raise ConnectionError("Authorization token rejected")
        elif (res.status_code == 400):
            raise IOError("Bad symbol format")
        elif (res.status_code == 409):
            raise IOError("Path conflict")
