#
# MODULE by @lyricsroot
# LICENSE: private; no external usage
#

""" 'CryptoTrader' Kraken API Caller module.

This module contains the KRAKEN_API_CALLER class. Which is used to
handle all HTTP requests and responses to/from the KRAKEN API

class fields:
    ROOT_URL: string, root-url of the KRAKEN server
    HTTP_USER_AGENT: string, user-agent for http request- headers

class methods:
    __init__:
        called when instantiating class
        params(public_key, private_key):
            public_key: string, public api user key
            private_key: string, private api user key
    test:
        called to test connection to kraken server through out requesting server time
        return true: if connection success
        return false: if connection failed
"""
##imports
import version_info
import requests

##class
class KRAKEN_API_CALLER:
    #fields
    ROOT_URL = 'https://api.kraken.com'
    HTTP_USER_AGENT = {'User-Agent': version_info.__packageName__ + '/' + version_info.__version__}
    #init
    def __init__(self, public_key='', private_key=''):
        self.api_public_key = public_key
        self._api_private_key = private_key
    #test api request
    def test(self):
        url_plus = '/0/public/Time'
        try:
            response = requests.get(self.ROOT_URL+url_plus, headers=self.HTTP_USER_AGENT)
            print('!Connection success!')
            print(response.text+'\n')
            return True
        except requests.exceptions.RequestException as e:
            print('!ERROR: connection failed!'+'\n')
            print(e+'\n')
            return False
    #get asset information
    def getAssetInfo(self):
        url_plus = '/0/public/Assets'
        print('fetching assets..')
        try:
            res = requests.get(self.ROOT_URL+url_plus, headers=self.HTTP_USER_AGENT)
            return res.json()
        except requests.exceptions.RequestException as e:
            print('!ERROR!\n')
            print(e+'\n')
    #get tradeable asset pairs
    def getTradeableAssetPairs(self):
        url_plus = '/0/public/AssetPairs'
        print('fetching tradeable asset pairs..')
        try:
            res = requests.get(self.ROOT_URL+url_plus, headers=self.HTTP_USER_AGENT)
            return res.json()
        except requests.exceptions.RequestException as e:
            print('!ERROR!\n')
            print(e+'\n')
    #get ohlc data for asset-pair
    def getOHLC(self, asset_pair):
            url_plus = '/0/public/OHLC'
            params = {'pair': asset_pair, 'interval': 1}
            print('fetching OHLC data for %s..' % asset_pair)
            try:
                res = requests.get(self.ROOT_URL+url_plus, headers=self.HTTP_USER_AGENT, params=params)
                return res.json()
            except requests.exceptions.RequestException as e:
                print("!ERROR!\n")
                print(e+'\n')
