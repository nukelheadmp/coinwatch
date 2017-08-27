from poloniex import poloniex

class exchange:
    def __init__(self):
        self.polo = poloniex("", "")

    def get_polo_tickers(self):
        return self.polo.returnTicker()
