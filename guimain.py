import pprint
import threading
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from exchange import exchange

class guimain(Gtk.Window):
    
    usdtbtc = 0.0
    
    # List of lists for each pair containing the symbol, USD and BTC pairing
    pairs = []
    pairs.append([0, "BCH", "USDT_BCH", "BTC_BCH"])
    pairs.append([1, "DASH", "USDT_DASH", "BTC_DASH"])
    pairs.append([2, "ETC", "USDT_ETC", "BTC_ETC"])
    pairs.append([3, "ETH", "USDT_ETH", "BTC_ETH"])
    pairs.append([4, "LTC", "USDT_LTC", "BTC_LTC"])
    pairs.append([5, "NXT", "USDT_NXT", "BTC_NXT"])
    pairs.append([6, "REP", "USDT_REP", "BTC_REP"])
    pairs.append([7, "STR", "USDT_STR", "BTC_STR"])
    pairs.append([8, "XMR", "USDT_XMR", "BTC_XMR"])
    pairs.append([9, "XRP", "USDT_XRP", "BTC_XRP"])
    pairs.append([10, "ZEC", "USDT_ZEC", "BTC_ZEC"])

    # Number of seconds to pause between each update
    delay = 5

    def __init__(self):
        # Exchange object that interfaces with exchange APIs
        self.exch = exchange()
        
        Gtk.Window.__init__(self, title="CoinWatch")
        self.set_border_width(10)

        # Setting up the self.grid in which the elements are to be positionned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)
        
        # Creating Bitcoin label and entry
        label = Gtk.Label("USDT BTC")
        self.grid.attach(label, 0, 0, 1, 1)
        
        self.btcentry = Gtk.Entry()
        self.btcentry.set_editable(False)
        self.btcentry.set_text(str(self.usdtbtc))
        self.grid.attach(self.btcentry, 1, 0, 1, 1)

        # Creating the ListStore model
        self.pair_liststore = Gtk.ListStore(str, float, float, float)
        self.current_filter_language = None

        # Creating the filter, feeding it with the liststore model
        self.language_filter = self.pair_liststore.filter_new()

        # Creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(["Symbol", "USDT", "USDT BTC", "BTC"]):
            renderer = Gtk.CellRendererText(xalign=1)
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_alignment(0.5)
            self.treeview.append_column(column)

        # Setting up the layout, putting the treeview in a scrollwindow
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 1, 2, 10)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()
        
        # Populate list with initial values
        for pair in self.pairs:
            self.pair_liststore.append(list([str(pair[1]), 0.0, 0.0, 0.0]))
        
        # Use threading for list updates
        thread = threading.Thread(target=self.update_list)
        thread.daemon = True
        thread.start()

    def update_list(self):
        while 1:
            try:
                results = self.exch.get_polo_tickers()
                self.usdtbtc = float(results["USDT_BTC"]['last'])
                self.btcentry.set_text(str(self.usdtbtc))
                for pair in self.pairs:
                    usdt = float(results[pair[2]]["last"])
                    btc = float(results[pair[3]]["last"])
                    btcusdt = self.usdtbtc * btc
                    self.pair_liststore[pair[0]][1] = usdt
                    self.pair_liststore[pair[0]][2] = btcusdt
                    self.pair_liststore[pair[0]][3] = btc
            except:
                pass
            time.sleep(self.delay)
        
