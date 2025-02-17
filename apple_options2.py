import requests
import json

# format
# https://api.polygon.io/v3/reference/options/contracts
# ?underlying_ticker=AAPL&
# limit=10&
# apiKey=SOlnh6Eqtscpw7z1QVTDNKwPUh_n6ZYm

# build the url
API_KEY = "SOlnh6Eqtscpw7z1QVTDNKwPUh_n6ZYm"
base_url = "https://api.polygon.io/v3/reference/options/contracts"
ticker = "AAPL"
limit = "10"

def make_url(base_url, ticker, limit, api_key):
    s = f'{base_url}?underlying_ticker={ticker}&limit={limit}&apiKey={api_key}'
    return s 

# u = make_url(base_url, ticker, limit, API_KEY)
# print('Request:')
# print(u)
# resp = requests.get(u)
# print(resp.text)

with open('apple_contracts.json', 'r') as file:
    data = json.load(file)
#print(json.dumps(data, indent=4))
for r in data['results']:
    print(r['ticker'])



