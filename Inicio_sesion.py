import tkinter as tk
from tkinter import messagebox


#modulos 
from imagenes import imagen
from Entradas import entrada
from textos import text 
from botones import crear_botones






#inicializamos la ventana por si se requiere guardar luego de crearse y no crearse cada vez
inicios=None


#En esta ventana hacemos uso de donde guardamos el usuario y la contraseña


def Login(ventana,usuario=None,contrase=None):
	global inicios
	ventana.withdraw()
	if inicios:
		inicios.deiconify()
	else:
		#iniciar ventanaa
		inicios = tk.Toplevel() 
		inicios.title("iniciando")
		inicios.geometry("1079x720+175+0")
		inicios.resizable(False, False)
		inicios.config(bg="gray10")
		#estos son stringvarss
		correo_str_var=tk.StringVar()
		contra_str_var=tk.StringVar()

		#este es el modulo de canvas
		canvas = imagen(inicios,"autobus.jpg",1079,720)

		#funcion para ir a la pagina principal despues de iniciar sesion correctament
		def comprobar():
			from principal import principel
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

		#funcion para volver, tiene esta forma porque al ejecutar la funcion se requiere mas acciones
		def volver():
			from inicio import inicial
			correo_str_var.set("")
			contra_str_var.set("")	
			inicial(inicios)	
		
		#texto que aparece automaticamente al no haber ningun usuario registrado
		if usuario==None and contrase==None:
			almacenados=text(canvas,440,460,"No hay usuarios Almacenados", "red", 18, "left")
		else:
			boton_comprobar=crear_botones("Comprobar",canvas,comprobar,540,460,16,"blue","red")
			

		#Texto de Ingresar usuario
		usuario_text=text(canvas,510,150,"Ingrese su usuario: ","black",18,"center")
		#Entrada de ingresar usuario
		user=entrada(canvas,540,200,correo_str_var)

		#texto de Ingresar contraseña
		contra_text=text(canvas,512,325,"Ingrese su contraseña: ","black",18,"center")
		#entrada de ingresar contraseña
		contra=entrada(canvas,540,380,contra_str_var)



		


		

		crear_botones("Regresar",canvas,volver,700,460,16,"blue","red")

		



