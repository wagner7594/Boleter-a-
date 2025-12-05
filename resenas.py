import tkinter as tk

from imagenes import imagen
from botones import crear_botones,boton_ventana
resenas=None
def Re(ventana):
	global resenas
	if ventana:
		ventana.withdraw()
	if resenas:
		resenas.deiconify()
	else:
		resenas=tk.Toplevel()
		resenas.title("reseñas")
		resenas.geometry("1079x720+175+0")
		resenas.resizable(False, False)
		resenas.config(bg="gray10")



		canvas = imagen(resenas,"autobus.jpg",1079,720)


		boton_ventana("Volver",canvas,630,543,18,"black","#00BFFF",resenas,"inicio")



