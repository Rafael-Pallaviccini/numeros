import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ventana = Gtk.Window()
ventana.set_title("hola mi jugador favorito")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show()

caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
caja.show()
ventana.add(caja)

etiqueta = Gtk.Label("hola wey")
etiqueta.show()
caja.pack_start(etiqueta, True, True, 0)

boton = Gtk.Button("salir")
boton.show()
boton.connect("clicked", Gtk.main_quit)
caja.pack_start(boton, True, True, 0)

Gtk.main()
