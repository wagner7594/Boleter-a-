import tkinter as tk
from imagenes import imagen
from Entradas import entrada
from textos import text 

from botones import crear_botones
from verificacion import verificando
from tkinter import messagebox
from registro2 import register2
from basededatos import comprobar_correo


codigo=None
registro=None


def Register(ventana):
	global registro
	ventana.withdraw()
	if registro:
		registro.deiconify()
	else:
		registro = tk.Toplevel()
		registro.iconbitmap("favicon.ico")    
		registro.title("Registro")
		registro.geometry("1079x720+175+0")
		registro.resizable(False, False)
		registro.config(bg="gray10")

		correo_string_enviar=tk.StringVar()
		nombre_var=tk.StringVar()

		canvas = imagen(registro,"autobus.jpg",1079,720)

		text(canvas,300,200,"Ingrese su correo:", "red", 18, "center")


		correo_enviar=entrada(canvas,300,300,correo_string_enviar)

		nombre_user=entrada(canvas,700,300,nombre_var)


		def pasador():
			code=entradades.get()
			if codigo == code:
				messagebox.showinfo("Bien","El codigo es correcto", parent=registro)
				register2(nombre_user.get(),correo_enviar.get(),registro)
			else:
				messagebox.showerror("error","El codigo esta mallllllllll", parent=registro)

		bloquedespues=tk.Frame(canvas,width=300,height=250)
		entradades=tk.Entry(bloquedespues)
		entradades.pack()
		boton=tk.Button(bloquedespues,text="Enviar codigo", command=pasador)
		boton.pack()


		def verificandoo():
			global codigo
			if comprobar_correo(correo_enviar.get(),registro):
				codigo=verificando(correo_enviar.get(),correo_string_enviar,registro,bloquedespues)
				print(codigo)


		crear_botones("Enviar meil",canvas,verificandoo,200,400,16,"blue","red")

		
	

    #Hacer un boton que diga enviar email y se conecte con la funcion "enviarmeil"
   

    #hacer un boton que nos lleve a la pag principal a traves de la funcion "confirmar_volver"

	#hacer un boton que se ejecute en el bloque despues q verifique el codigo    
