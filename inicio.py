import tkinter as tk
from botones import crear_botones
from imagenes import imagen
from textos import text


from registro import Register
from Inicio_sesion import Login
from resenas import Re
from terminos import Ter

presentacion=None

def inicial(ventana=None):
	global presentacion
	if ventana:
		ventana.withdraw()
	if presentacion:
		presentacion.deiconify()
	else:
		presentacion = tk.Tk() 


		presentacion.iconbitmap("favicon.ico")
		presentacion.geometry("1079x720+175+0")
		presentacion.resizable(False, False)
		presentacion.title("BoleteriaOficial")


		canvas = imagen(presentacion,"fondo_principal.jpg",1079,720)
		def a_registro():
			Register(presentacion)
		def a_sesion():
			Login(presentacion)
		def a_terminos():
			Ter()
		def a_rese():
			Re()


		text(canvas,535,280,"BIENVENIDOS","white",20,"center")
		#boton registrarse
		crear_botones("Registrarse",canvas,a_registro,535,345,18,"white","#00BFFF")

		#boton iniciar sesion
		crear_botones("Iniciar sesión",canvas,a_sesion,535,437,18,"white","#00BFFF")

		#boton de terminos
		crear_botones("Terminos",canvas,a_terminos,450,543,13,"white","#00BFFF")

		#boton de reseñas
		crear_botones("Reseñas",canvas,a_rese,630,543,13,"white","#00BFFF")




		presentacion.mainloop()