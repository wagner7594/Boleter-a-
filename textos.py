#modulo de textoss

def text(canvas,ancho,alto,texto,color,tama,alineacion):
	texto=canvas.create_text(ancho,alto, text=texto,
		fill=color, font=("Arial", tama, "bold"), justify=alineacion)
	return texto