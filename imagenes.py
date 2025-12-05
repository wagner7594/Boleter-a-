import os
from PIL import Image, ImageTk
import tkinter as tk

def imagen(ventana, nombre_imagen, ancho, alto):
    canvas = tk.Canvas(ventana, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    
    ruta_actual = os.path.dirname(__file__)
    ruta_imagen = os.path.join(ruta_actual, nombre_imagen)
    
    
    fondo = Image.open(ruta_imagen).resize((ancho, alto))
    fondo_tk = ImageTk.PhotoImage(fondo)
    
    
    canvas.fondo = fondo_tk
    canvas.create_image(0, 0, image=fondo_tk, anchor="nw")
    
    return canvas