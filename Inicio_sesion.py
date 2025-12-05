import tkinter as tk
from tkinter import messagebox

from imagenes import imagen
from Entradas import entrada
from textos import text 

from botones import crear_botones
from principal import principel






inicios=None


#En esta ventana hacemos uso de donde guardamos el usuario y la contraseña


def Login(ventana,usuario=None,contrase=None):
	global inicios
	ventana.withdraw()
	if inicios:
		inicios.deiconify()
	else:
		inicios = tk.Toplevel() 
		inicios.title("iniciando")
		inicios.geometry("1079x720+175+0")
		inicios.resizable(False, False)
		inicios.config(bg="gray10")

		correo_str_var=tk.StringVar()
		contra_str_var=tk.StringVar()

		canvas = imagen(inicios,"autobus.jpg",1079,720)

		text(canvas,510,150,"Ingrese su usuario: ","black",18,"center")
		user=entrada(canvas,540,200,correo_str_var)
		text(canvas,512,325,"Ingrese su contraseña: ","black",18,"center")
		contra=entrada(canvas,540,380,contra_str_var)

		def comprobar():
			contador=0
			if user.get() not in usuario:
				messagebox.showerror("Error","El usuario no se encuentra", parent=inicios)
			else:
				for i in usuario:
					if i==user.get():
						if contrase[contador]==contra.get():
							messagebox.showinfo("Exito","Credenciales correctas", parent=inicios)
							correo_str_var.set("")
							contra_str_var.set("")
							principel(inicios)
					else:
						contador+=1


			
			



		if usuario==None and contrase==None:
			text(canvas,440,460,"No hay usuarios Almacenados", "red", 18, "left")
		else:
			crear_botones("Comprobar",canvas,comprobar,540,460,16,"blue","red")


		def volver():
			from inicio import inicial
			correo_str_var.set("")
			contra_str_var.set("")	
			inicial(inicios)	

		crear_botones("Regresar",canvas,volver,700,460,16,"blue","red")

		



