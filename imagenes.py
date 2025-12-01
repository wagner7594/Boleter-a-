from PIL import Image,ImageTk
import tkinter as tk

def imagen(ventana,imaged,ancho,alto):
    canvas = tk.Canvas(ventana, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    fondo = Image.open(imaged).resize((ancho,alto))


    fondo_tk = ImageTk.PhotoImage(fondo)
    canvas.fondo=fondo_tk

    canvas.create_image(0, 0, image=fondo_tk, anchor="nw")
    return canvas
