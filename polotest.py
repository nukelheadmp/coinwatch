import pprint
from poloniex import poloniex

polo = poloniex("U73MR298-R7GA3ZSE-UM7W8ZSR-H1CHIZR3", "004f930f844c68d285fdb72ebce7cc1826817835067780c4639229374217fcdda43618dafafc1aa573df9338df5c2922d13a84f9c40429bea19ea97a6b09d534")
response = polo.returnTicker()
pprint.pprint(response)
