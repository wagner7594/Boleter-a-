import tkinter as tk
#modulos
from botones import crear_botones,boton_ventana
from imagenes import imagen
start=None
def principel(ventana):
	global start
	ventana.withdraw()
	if start:
		start.deiconify()
	else:
		start = tk.Toplevel()
	  
		start.title("principal")
		start.geometry("1079x720+175+0")
		start.resizable(False, False)
		
		start.config(bg="gray10")

		canvas = imagen(start,"autobus.jpg",1079,720)
		boton_cerrar_se=boton_ventana("Cerrar sesion",canvas,700,460,18,"white","#00BFFF",start,"inicio")
