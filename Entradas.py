import tkinter as tk
#esto es la funcion de entradas, se debe colocar un canvas si o si, una ventana no
def entrada(canvas,ejex,ejey,stringvar,mostrar=""):
	bloque = tk.Frame(canvas, bg="green", width=300, height=35)
	bloque.pack_propagate(False)

	entrada = tk.Entry(bloque, textvariable=stringvar ,bg="gray6", fg="white",
		justify="center",font=("Arial",13,"bold"),show=mostrar)
	entrada.pack(fill="both", expand=True)

	canvas.create_window(ejex,ejey, window=bloque)

	return entrada

	