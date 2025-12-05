import tkinter as tk
from Inicio_sesion import Login
from tkinter import messagebox

#modulos
from imagenes import imagen
from Entradas import entrada
from textos import text 
from botones import crear_botones,boton_ventana


#globales que guardan los usuarios, solo queda imaginar que es una db
usuario_list=[]
correo_list=[]
contraseña_list=[]
#inicializamos ventana,uno nunca sabe
regis=None

#funcion util en otros archivos para verificar que no haya un usuario ya ingresado con ese nombre
def repeticion_usuario(usuario,stringvar,ventana_):
	if usuario in usuario_list:
		messagebox.showerror("Error","Ya alguien se registro con este usuario",parent=ventana_)
		stringvar.set("")
		return False
	else: 
		return True
#lo mismo que la anterior funcion pero con email
def repeticion_meil(meil,stringvar,ventana_):
	if meil in correo_list:
		messagebox.showerror("Error","Este correo ya esta registrado",parent=ventana_)
		stringvar.set("")
		return False
	else: 
		return True


#En esta ventana guardamos el usuario con la contraseña
def register2(nombre_entrada,correo_entrada,ventana):
	global regis,usuario_list,correo_list,contraseña_list
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

	#imagen en el fondo con canvas:
	canvas = imagen(regis,"autobus.jpg",1079,720)


	#funcion que verifica la contraseñas sean iguales para guardar el userrrrrr
	def verificar_ultimate():
		if contra_primer.get()==contra_second.get():

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



	#texto de contra primera y tambien su entrada
	contra_texto1=text(canvas,540,150,"Ingrese una contraseña: ","black",18,"left")
	contra_primer=entrada(canvas,540,200,contra1_var,"*")


	#texto de segunda contraseña y por supuesto su entrada
	contra_texto2=text(canvas,540,325,"Vuelva a ingresar su contraseña: ","black",18,"left")
	contra_second=entrada(canvas,540,380,contra2_var,"*")


	#boton de la funcion anterior
	enviar_datos=crear_botones("Enviar datos",canvas,verificar_ultimate,540,460,16,"blue","red")
	
	#boton de volver 
	volver_boton=boton_ventana("Volver",canvas,700,460,18,"white","#00BFFF",regis,"inicio")
