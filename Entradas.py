import tkinter as tk

def entrada(canvas,ejex,ejey,stringvar,mostrar=""):
	bloque = tk.Frame(canvas, bg="darkorchid4", width=300, height=35)
	bloque.pack_propagate(False)

	entradacorreo1 = tk.Entry(bloque, textvariable=stringvar ,bg="gray6", fg="white",
		justify="center",font=("Arial",13,"bold"),show=mostrar)
	entradacorreo1.pack(fill="both", expand=True, padx=2, pady=2)

	canvas.create_window(ejex,ejey, window=bloque)

	return entradacorreo1

	