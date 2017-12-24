from pip._vendor import requests

from pip.


parameters = {"market": "BTC-NEO"}

response = requests.get("https://bittrex.com/api/v1.1/public/getticker", params=parameters)

data = response.json()
print(data)