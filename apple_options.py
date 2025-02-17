#apply_options.py
# from https://www.youtube.com/watch?v=87O9qxfMJ-g
from polygon import RESTClient
import datetime as dt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

'''
client = RESTClient(api_key="SOlnh6Eqtscpw7z1QVTDNKwPUh_n6ZYm")
contract = client.get_options_contract("O:AAPL250221C00100000")
# print raw values
print(contract)
'''
# https://api.polygon.io/v3/reference/options/contracts
# ?underlying_ticker=AAPL&
# limit=10&
# apiKey=SOlnh6Eqtscpw7z1QVTDNKwPUh_n6ZYm
client = RESTClient(api_key=)
contractNames = []
for t in client.list_options_contracts(underlying_ticker="AAPL",expiration_date="2025-02-21"):
    contractNames.append(t)
print(contractNames)

