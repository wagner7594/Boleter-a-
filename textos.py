def text(canvas,ancho,alto,texto,color,tama,alineacion):
	canvas.create_text(ancho,alto, text=texto,
	fill=color, font=("Arial", tama, "bold"), justify=alineacion)