
#esta funcion sirve para cambiar de ventanas es el finalizador del 
#intermediario que es intermedio.py

def cambio(ventana,texto):
	if texto.lower()=="registro":
		from registro import Register
		Register(ventana)
	elif texto.lower()=="inicio_sesion":
		from Inicio_sesion import Login
		Login(ventana)
	elif texto.lower()=="inicio":
		from inicio import inicial
		inicial(ventana)
	elif texto.lower()=="terminos":
		from terminos import Ter
		Ter(ventana)
	elif texto.lower()=="reseñas":
		from resenas import Re
		Re(ventana)





