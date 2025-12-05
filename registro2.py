import tkinter as tk
from Inicio_sesion import Login
from tkinter import messagebox


from imagenes import imagen
from Entradas import entrada
from textos import text 
from botones import crear_botones,boton_ventana



usuario_list=[]
correo_list=[]
contraseña_list=[]
#En esta ventana guardamos el usuario con la contraseña
regis=None
def repeticion_usuario(usuario,ventana_):
	if usuario in usuario_list:
		messagebox.showerror("Error","Ya alguien se registro con este usuario",parent=ventana_)
		return False
	else: 
		return True

def repeticion_meil(meil,ventana_):
	if meil in correo_list:
		messagebox.showerror("Error","Este correo ya esta registrado",parent=ventana_)
		return False
	else: 
		return True

def register2(nombre_entrada,correo_entrada,ventana):
	global regis,usuario_list,correo_list,contraseña_list
	print(nombre_entrada)
	print(correo_entrada)
	print("1212")
	ventana.withdraw()
	if regis:
		regis.destroy()

	regis=tk.Toplevel()  
	regis.title("Registro 2")
	regis.geometry("1079x720+175+0")
	regis.resizable(False, False)
	regis.config(bg="gray10")
	contra1_var=tk.StringVar()
	contra2_var=tk.StringVar()

	canvas = imagen(regis,"autobus.jpg",1079,720)
	def verificar_ultimate():
		if contra_primer.get()==contra_second.get():
			print("33112")
			print(nombre_entrada)
			print(correo_entrada)
			usuario_list.append(nombre_entrada)
			correo_list.append(correo_entrada)
			contraseña_list.append(contra_primer.get())
			print(usuario_list)
			print(correo_list)
			print(contraseña_list)
			messagebox.showinfo("exito","las contraseñas coinciden", parent=regis)
			Login(regis,usuario_list,contraseña_list)
			contra1_var.set("")
			contra2_var.set("")

		else:
			messagebox.showerror("Error","Las contras no coinciden",parent=regis)
			contra1_var.set("")
			contra2_var.set("")




	text(canvas,540,150,"Ingrese una contraseña: ","black",18,"left")
	contra_primer=entrada(canvas,540,200,contra1_var,"*")
	text(canvas,540,325,"Vuelva a ingresar su contraseña: ","black",18,"left")
	contra_second=entrada(canvas,540,380,contra2_var,"*")

	crear_botones("Enviar datos",canvas,verificar_ultimate,540,460,16,"blue","red")
	
	boton_ventana("Volver",canvas,700,460,18,"white","#00BFFF",regis,"inicio")
