import pprint
import curses
import time
from poloniex import poloniex

screen = curses.initscr()
screen.nodelay(1)

apikey = {"key": "", "secret": ""}

polo = poloniex(apikey['key'], apikey['secret'])

pairs = []
pairs.append(["BCH", "USDT_BCH", "BTC_BCH"])
pairs.append(["DASH", "USDT_DASH", "BTC_DASH"])
pairs.append(["ETC", "USDT_ETC", "BTC_ETC"])
pairs.append(["ETH", "USDT_ETH", "BTC_ETH"])
pairs.append(["LTC", "USDT_LTC", "BTC_LTC"])
pairs.append(["NXT", "USDT_NXT", "BTC_NXT"])
pairs.append(["REP", "USDT_REP", "BTC_REP"])
pairs.append(["STR", "USDT_STR", "BTC_STR"])
pairs.append(["XMR", "USDT_XMR", "BTC_XMR"])
pairs.append(["XRP", "USDT_XRP", "BTC_XRP"])
pairs.append(["ZEC", "USDT_ZEC", "BTC_ZEC"])

delay = 5

btcusd = 0.0
altusd = 0.0
altbtc = 0.0
altbtcusd = 0.0
varperc = 0.0

y, x = 0, 0
usdx = 5
btcusdx = 20
btcx = 40
varpercx = 55

i = 0
input = 0

while input != ord('q'):

    try:
        response = polo.returnTicker()

        screen.clear()

        if response:
            btcusd = response['USDT_BTC']['last']
            screen.addstr(y, x, "BTC = " + str(btcusd))
            screen.addstr(y, varpercx, str(i))
            i += 1
            y += 1

            screen.addstr(y, usdx, "USD")
            screen.addstr(y, btcusdx, "BTCUSD")
            screen.addstr(y, btcx, "BTC")
            screen.addstr(y, varpercx, "%")
            y += 1

            for pair in pairs:
                altusd = response[pair[1]]['last']
                altbtc = response[pair[2]]['last']
                altbtcusd = float(altbtc) * float(btcusd)
                varperc = ((altbtcusd - float(altusd)) / altbtcusd) * 100

                screen.addstr(y, x, pair[0])
                screen.addstr(y, usdx, altusd)
                screen.addstr(y, btcusdx, str(altbtcusd))
                screen.addstr(y, btcx, altbtc)
                screen.addstr(y, varpercx, str("%.4f" % varperc))
                y += 1

            y = 0
            screen.refresh()

    except:
        pass
    
    input = screen.getch()
    time.sleep(delay)
 
curses.endwin()
