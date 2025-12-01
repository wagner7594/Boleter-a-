import tkinter as tk
from tkinter import messagebox

from imagenes import imagen
from Entradas import entrada
from textos import text 

from botones import crear_botones

from basededatos import validar_login
from principal import principel



inicios=None
def Login(ventana):
	global inicios
	ventana.withdraw()
	if inicios:
		inicios.deiconify()
	else:
		inicios = tk.Toplevel()
		inicios.iconbitmap("favicon.ico")    
		inicios.title("iniciando")
		inicios.geometry("1079x720+175+0")
		inicios.resizable(False, False)
		inicios.config(bg="gray10")

		correo_str_var=tk.StringVar()
		contra_str_var=tk.StringVar()

		canvas = imagen(inicios,"autobus.jpg",1079,720)


		user=entrada(canvas,300,300,correo_str_var)

		contra=entrada(canvas,710,300,contra_str_var)

		def comprobar():
			if validar_login(user.get(),contra.get(),inicios):
				principel(inicios)
			else:
				messagebox.showerror("Error","El usuario no se encuentra", parent=inicios)

		crear_botones("comprobar",canvas,comprobar,300,400,16,"blue","red")



