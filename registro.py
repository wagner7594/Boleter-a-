import tkinter as tk
from tkinter import messagebox

#modulossss
from imagenes import imagen
from Entradas import entrada
from textos import text 
from botones import crear_botones,boton_ventana


#modulo de verificacion email
from verificacion import verificando




#En esta ventana de aqui comprobamos el correo sea valido


codigo=None
registro=None


def Register(ventana):
	global registro
	ventana.withdraw()
	if registro:
		#destruimos ventana porque queremos que los valores se reestablezcan
		registro.destroy()
	#iniciando ventana
	registro = tk.Toplevel()  
	registro.title("Registro")
	registro.geometry("1079x720+175+0")
	registro.resizable(False, False)
	registro.config(bg="gray10")


	#stringvars para modficar entradas desde cualquier punto
	correo_string_enviar=tk.StringVar()
	nombre_var=tk.StringVar()
	codigo_var=tk.StringVar()

	#modulo para ubicar imagen en uso:
	canvas = imagen(registro,"autobus.jpg",1079,720)
	

	#funciones que tienen como evento al modificar una entrada ejecute estas funciones
	#cuando estas funciones se ejecutan habilitan los botones de validar usuario y email
	#estos botones mencionados tienen como proposito verificar que el usuario y el correo no se hayan registrado
	#muestran los botones y ocultan el texto al modficar entrada para comprobacion de nuevo

	def escribir1(event):
		canvas.itemconfig(boton_validar_user,state="normal")
		canvas.itemconfig(texto_user,state="hidden")


	def escribir2(event):
		canvas.itemconfig(boton_validar_meil,state="normal")
		canvas.itemconfig(texto_meil,state="hidden")

	
	
	#esta funcion se encarga de validar que el codigo ingresado sea correcto al que se envio
	#si funciona nos envia al registro2 donde hay que poner las contraseñas
	def pasador():
		
		code=entradades.get()
		if codigo == code:
			from registro2 import register2
			messagebox.showinfo("Bien","El codigo es correcto", parent=registro)
			register2(nombre_user.get(),correo_enviar.get(),registro)
			correo_string_enviar.set("")
			nombre_var.set("")
			codigo_var.set("")
			bloquedespues.place_forget()
		else:
			print(nombre_user.get())
			print(correo_enviar.get())
			messagebox.showerror("error","El codigo esta mallllllllll", parent=registro)
			codigo_var.set("")

	

	
	#esta funcion verifica que en la entrada de usuario no se pongan menos de 5 caracteres ni mas de 15 y no este vacia
	def verificar_usuario():
		if len(nombre_user.get()) ==0:
			messagebox.showerror("Error","Debe colocar algo en el usuario", parent=registro)	 
			nombre_var.set("")
		elif len(nombre_user.get())>15 :
			messagebox.showerror("Advertencia","Debe ingresar un nombre de usario con menos de 16 caracteres",parent=registro)
			nombre_var.set("")
		elif len(nombre_user.get())<=5:
			messagebox.showerror("Advertencia","Debe ingresar un nombre de usario con mas de 5 caracteres",parent=registro)
			nombre_var.set("")
		else:
			return True

	#esta funcion verifica el correo y se envia al modulo de verificacion.py si no funciona vuelve a ocultar btones y el texto de 
	#que el email no se ha aceptado porque va a existir una modificacion 
	def verificandoo():
		global codigo
		codigo=verificando(correo_enviar.get(),correo_string_enviar,registro,bloquedespues)
		if codigo is None:
			print("holallalala")
			canvas.itemconfig(texto_meil,state="hidden")
			canvas.itemconfig(boton_validar_meil,state="normal")
			canvas.itemconfig(boton_verificar,state="hidden")

	#esta funcipn es para volver al registro anterior vaciando entradas
	def volver():
		from inicio import inicial
		correo_string_enviar.set("")
		nombre_var.set("")	
		inicial(registro)

	#esta funcion hace uso de la funcion verificarusuario para validar el usuario pero llamamos una funcion de registro2 
	#debido a que en ese archivo es donde se almacenan los datos de todos los usuarios
	def validar_usuario():
		from registro2 import repeticion_usuario
		if verificar_usuario():
			if repeticion_usuario(nombre_user.get(),nombre_var,registro):
				canvas.itemconfig(boton_validar_user,state="hidden")
				canvas.itemconfig(texto_user,state="normal")



	#esta es similar que la anterior pero con el email:
	def validar_meil():
		from registro2 import repeticion_meil
		if len(correo_enviar.get())==0:
			messagebox.showerror("Advertencia","La entrada no tiene elemento a verificar",parent=registro)
			correo_string_enviar.set("")
		elif "@" not in correo_enviar.get():
			messagebox.showerror("Advertencia","Debe ingresar un correo",parent=registro)
			correo_string_enviar.set("")
		else:
			if repeticion_meil(correo_enviar.get(),correo_string_enviar,registro):
				canvas.itemconfig(boton_validar_meil,state="hidden")
				canvas.itemconfig(texto_meil,state="normal")
				canvas.itemconfig(boton_verificar,state="normal")

			


	#texto gigante principal
	Texto_principal=text(canvas,534,60,"REGISTRE SUS DATOS:", "red", 20, "center")

	#texto y entrada de registrar usuario
	Texto_usuario3=text(canvas,510,150,"Registre su Usuario: ", "red", 18, "left")
	nombre_user=entrada(canvas,540,200,nombre_var)

	#texto y entrada de registrar correo
	Texto_correo4=text(canvas,512,325,"Registre su correo: ", "red", 18, "left")
	correo_enviar=entrada(canvas,540,380,correo_string_enviar)

	#bton para enviar el email y verificar si es real y en caso de que lo sea enviar un correo con un codigo
	#se oculta porque se muestra cuando se valide que el correo ingresado no exista repetido
	boton_verificar=crear_botones("Enviar meil",canvas,verificandoo,540,460,16,"blue","red")
	canvas.itemconfig(boton_verificar,state="hidden")



	#aqui se modifican las entradas para el evento de teclado en las dos primeras funciones de este archivo
	nombre_user.bind("<KeyRelease>",escribir1)	
	correo_enviar.bind("<KeyRelease>",escribir2)


	#aqui creamos el bloque con una entrada y un bton que es para el codigo que nos llega
	#no mostramos el bloque solo lo creamos, se muestra cuando se envie el correo
	bloquedespues=tk.Frame(canvas,width=300,height=250)
	entradades=tk.Entry(bloquedespues,textvariable=codigo_var)
	entradades.pack()
	boton=tk.Button(bloquedespues,text="Enviar codigo", command=pasador)
	boton.pack()

	#este es el texto para aceptar el usuario, inicialmente oculto
	texto_user=text(canvas,840,200,"usuario aceptable", "red", 20, "center")
	canvas.itemconfig(texto_user,state="hidden")


	#y este es del email
	texto_meil=text(canvas,840,380,"correo aceptable", "red", 20, "center")
	canvas.itemconfig(texto_meil,state="hidden")


	#este es el boton de volver con la funcion de muy arriba
	boton_volver=crear_botones("Volver",canvas,volver,590,580,18,"blue","red")

	#este es el boton que valida que el usuario no se encuentre en el sistem
	boton_validar_user=crear_botones("Validar que el usuario no exista",canvas,validar_usuario,860,200,16,"#033F65","#FA8911")


	#y esto es lo mismo que lo anterior pero con meil
	boton_validar_meil=crear_botones("Validar que el email no exista",canvas,validar_meil,860,380,16,"blue","red")

	

