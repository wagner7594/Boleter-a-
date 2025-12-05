def crear_botones(texto,canvas,funcion,ejex,ejey,tama,color1,color2):
	boton = canvas.create_text(ejex, ejey, text=texto, fill=color1,font=("Arial", tama, "bold"), justify="center")
	def starting():
		funcion()
	canvas.tag_bind(boton, "<Button-1>", lambda e: starting())
	canvas.tag_bind(boton, "<Enter>", lambda e: [canvas.itemconfig(boton, fill=color2),
	canvas.config(cursor="hand2"), canvas.update_idletasks()])

	canvas.tag_bind(boton, "<Leave>", lambda e: [canvas.itemconfig(boton, fill=color1),
	canvas.config(cursor=""), canvas.update_idletasks()])

def boton_ventana(texto,canvas,ejex,ejey,tama,color1,color2,ventana,dirigir):
	from intermedio import funcion
	boton = canvas.create_text(ejex, ejey, text=texto, fill=color1,font=("Arial", tama, "bold"), justify="center")

	canvas.tag_bind(boton, "<Button-1>", lambda e: funcion(ventana,dirigir))
	canvas.tag_bind(boton, "<Enter>", lambda e: [canvas.itemconfig(boton, fill=color2),
	canvas.config(cursor="hand2"), canvas.update_idletasks()])

	canvas.tag_bind(boton, "<Leave>", lambda e: [canvas.itemconfig(boton, fill=color1),
	canvas.config(cursor=""), canvas.update_idletasks()])



