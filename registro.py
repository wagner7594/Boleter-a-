import tkinter as tk
from tkinter import messagebox

from imagenes import imagen
from Entradas import entrada
from textos import text 
from botones import crear_botones,boton_ventana


from verificacion import verificando




#En esta ventana de aqui comprobamos el correo sea valido


codigo=None
registro=None


def Register(ventana):
	global registro
	ventana.withdraw()
	if registro:
		registro.destroy()
	registro = tk.Toplevel()  
	registro.title("Registro")
	registro.geometry("1079x720+175+0")
	registro.resizable(False, False)
	registro.config(bg="gray10")

	correo_string_enviar=tk.StringVar()
	nombre_var=tk.StringVar()
	codigo_var=tk.StringVar()


	canvas = imagen(registro,"autobus.jpg",1079,720)
	text(canvas,534,60,"REGISTRE SUS DATOS:", "red", 20, "center")

	text(canvas,510,150,"Registre su Usuario: ", "red", 18, "left")
	nombre_user=entrada(canvas,540,200,nombre_var)

	text(canvas,512,325,"Registre su correo: ", "red", 18, "left")
	correo_enviar=entrada(canvas,540,380,correo_string_enviar)
	


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

	

	bloquedespues=tk.Frame(canvas,width=300,height=250)
	entradades=tk.Entry(bloquedespues,textvariable=codigo_var)
	entradades.pack()
	boton=tk.Button(bloquedespues,text="Enviar codigo", command=pasador)
	boton.pack()

	def verificar_usuario():
		if len(nombre_user.get())>15:
			messagebox.showerror("Advertencia","Debe ingresar un nombre de usario con menos de 16 caracteres",parent=registro)
			nombre_var.set("")
		if nombre_user.get() is None:
			messagebox.showerror("Error","Debe colocar algo en el usuario", parent=registro)	 
			nombre_var.set("")
		if len(nombre_user.get())<15 and nombre_user.get() is not None:
			return True


	def verificandoo():
		global codigo
		if verificar_usuario():
			codigo=verificando(correo_enviar.get(),correo_string_enviar,registro,bloquedespues)
		
	crear_botones("Enviar meil",canvas,verificandoo,540,460,16,"blue","red")

	def volver():
		from inicio import inicial
		correo_string_enviar.set("")
		nombre_var.set("")	
		inicial(registro)	
	def validar_usuario():
		from registro2 import repeticion_usuario
		if repeticion_usuario(nombre_user.get(),registro):
			text(canvas,840,230,"usuario bien", "red", 20, "center")

	def validar_meil():
		from registro2 import repeticion_meil
		if repeticion_meil(correo_enviar.get(),registro):
			text(canvas,840,400,"usuario bien", "red", 20, "center")

	crear_botones("Volver",canvas,volver,700,460,18,"blue","red")

	crear_botones("Validar_usuario",canvas,validar_usuario,840,200,18,"#033F65","#FA8911")

	crear_botones("Validar_meil",canvas,validar_meil,840,380,18,"blue","red")
	
	


		
	

    #Hacer un boton que diga enviar email y se conecte con la funcion "enviarmeil"
   

    #hacer un boton que nos lleve a la pag principal a traves de la funcion "confirmar_volver"

	#hacer un boton que se ejecute en el bloque despues q verifique el codigo    
