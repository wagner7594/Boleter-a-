import tkinter as tk
from basededatos import guardar_usuario
from Inicio_sesion import Login
from tkinter import messagebox


from imagenes import imagen
from Entradas import entrada
from textos import text 

from botones import crear_botones
regis=None
def register2(nombre,correo,ventana):
	global regis
	ventana.withdraw()
	if regis:
		regis.deiconify()
	else:

		regis=tk.Toplevel()
		regis.iconbitmap("favicon.ico")    
		regis.title("Registro 2")
		regis.geometry("1079x720+175+0")
		regis.resizable(False, False)
		regis.config(bg="gray10")
		name=nombre
		correo_meil=correo
		contra1_var=tk.StringVar()
		contra2_var=tk.StringVar()

		canvas = imagen(regis,"autobus.jpg",1079,720)
		def verificar_ultimate():
			global contra1_var,contra2_var
			if contra_primer.get()==contra_second.get():
				
				guardar_usuario(name,correo_meil,contra_primer.get())
				messagebox.showinfo("exito","las contraseñas coinciden", parent=regis)
				Login(regis)

			else:
				messagebox.showerror("Error","Las contras no coinciden",parent=regis)
				contra1_var.set("")
				contra2_var.set("")

		contra_primer=entrada(canvas,300,300,contra1_var)
		contra_second=entrada(canvas,595,300,contra2_var)
		from registro import Register
		crear_botones("Enviar datos",canvas,verificar_ultimate,200,400,16,"blue","red")
		crear_botones("Volver",canvas,Register,350,400,16,"blue","red")
