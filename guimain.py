import threading
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class guimain(Gtk.Window):
    
    #list of tuples for each pair containing the symbol, USD and BTC pairing
    pairs = []
    pairs.append(["BCH", "USDT_BCH", "BTC_BCH", 0])
    
    delay = 5
    counter = 0

    def __init__(self):
        Gtk.Window.__init__(self, title="CoinWatch", default_height=300, default_width=600)
        self.set_border_width(10)

        #Setting up the self.grid in which the elements are to be positionned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        #Creating the ListStore model
        self.pair_liststore = Gtk.ListStore(str, str, str, int)
        self.current_filter_language = None

        #Creating the filter, feeding it with the liststore model
        self.language_filter = self.pair_liststore.filter_new()

        #creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(["Symbol", "USD", "BTC", "Counter"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        #setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

        thread = threading.Thread(target=self.update_list)
        thread.daemon = True
        thread.start()

    def update_list(self):
        while 1:
            self.pair_liststore.clear()
            self.counter += 1
            for pair in self.pairs:
                pair[3] = self.counter
                self.pair_liststore.append(list(pair))
            time.sleep(self.delay)
        
