from poloniex import poloniex

class poloticker:
  polo = poloniex("", "")
  def get_tickers():
    return polo.returnTicker()
