import requests
import json
import time
import useful
import urllib.parse

# WikiLibs AI Client python module interface
# This class should be the parent of the bot that push symbols
# called ?
# The logic should not be modified (C++ interface)
# PushSymbols() and Optimize() must be implemented by the child class
# Other functions can be modified here, but not overrided by the child
class AIClientInterface:
    def __init__(self, apikey, appID, secret):
        self._apikey = apikey
        self._appID = appID
        self._secret = secret
        self._token = ""
        self._time = 0.0

    def PushSymbol(self, obj):
        # function that must be called in order to push symbols
        # should be connected to API in order to call routes to push
        # https://wikilibs-dev-api.azurewebsites.net/swagger/index.html
        useful.logError("Function PushSymbol is not overloaded")

    def Optimize(self):
        # function that optimize in DB symbols that have been pushed 
        # should be connected to API in order to call routes to push
        # https://wikilibs-dev-api.azurewebsites.net/swagger/index.html
        useful.logError("Function Optimize is not overloaded")
