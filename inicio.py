import tkinter as tk


from imagenes import imagen
from botones import crear_botones,boton_ventana
from textos import text



presentacion=None

def inicial(ventana=None):
	global presentacion
	if ventana:
		ventana.withdraw()
	if presentacion:
		presentacion.deiconify()
	else:
		presentacion = tk.Tk() 



		presentacion.geometry("1079x720+175+0")
		presentacion.resizable(False, False)
		presentacion.title("BoleteriaOficial")


		canvas = imagen(presentacion,"fondo_principal.jpg",1079,720)

		text(canvas,535,280,"BIENVENIDOS","white",20,"center")

		#boton registrarse
		boton_ventana("Registrarse",canvas,535,345,18,"#033F65","#FA8911",presentacion,"registro")

		#boton iniciar sesion
		boton_ventana("Iniciar Sesion",canvas,535,437,18,"#033F65","#FA8911",presentacion,"inicio_sesion")
		

		#boton de terminos
		boton_ventana("Terminos",canvas,450,543,18,"#033F65","#FA8911",presentacion,"terminos")
	

		#boton de reseñas
		boton_ventana("Reseñas",canvas,630,543,18,"#033F65","#FA8911",presentacion,"reseñas")




		presentacion.mainloop()