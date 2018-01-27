import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window(title="PyJosep")
win.show_all()
#win.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
