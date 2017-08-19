import pprint
from poloniex import poloniex

polo = poloniex("", "")
response = polo.returnTicker()
pprint.pprint(response)
