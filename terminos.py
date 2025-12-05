import tkinter as tk

from botones import crear_botones,boton_ventana
from imagenes import imagen


from selectores import elegir



#este es una pag de terminos 

terminos=None
def Ter(ventana):
	global terminos
	if ventana:
		ventana.withdraw()
	if terminos:
		terminos.deiconify()
	else:
		terminos=tk.Toplevel() 
		terminos.title("terminos")
		terminos.geometry("1079x720+175+0")
		terminos.resizable(False, False)
		terminos.config(bg="gray10")



		canvas = imagen(terminos,"autobus.jpg",1079,720)

		#Boton de regresar
		boton_ventana("Volver",canvas,630,543,18,"black","red",terminos,"inicio")
		

		elegir(canvas,"Origen",450,200,"manta","guayaquil")

		elegir(canvas,"Destino",450,350,"galapagos","guayaquil")


	