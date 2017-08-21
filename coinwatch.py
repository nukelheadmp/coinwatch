#! /usr/bin/env python3

import threading
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from guimain import guimain

def app_main():
  win = guimain()
  win.connect("delete-event", Gtk.main_quit)
  win.show_all()

if __name__ == "__main__":
  
  app_main()
  Gtk.main()
