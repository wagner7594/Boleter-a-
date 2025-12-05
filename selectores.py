import tkinter as tk
from tkinter import ttk

#este es un modulo de prueba que son selectores

def elegir(canvas,ubicacion,enx,eny,opcion1,opcion2):
    
    opciones = [f"{opcion1}",f"{opcion2}"]

    frame=tk.Frame(canvas,width=150,height=40)
    frame.place(x=enx,y=eny)
    frame.pack_propagate(False)


    combo = ttk.Combobox(
        frame, 
        values=opciones,
        state="readonly", 
        font=("Arial", 10),
    )
    combo.pack(fill="both",expand=True,padx=2,pady=2)

    combo.set(f"{ubicacion}")


