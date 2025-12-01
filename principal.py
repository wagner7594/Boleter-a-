import tkinter as tk


start=None
def principel(ventana):
	global start
	ventana.withdraw()
	if start:
		start.deiconify()
	else:
		start = tk.Toplevel()
		start.iconbitmap("favicon.ico")    
		start.title("principal")
		start.geometry("1079x720+175+0")
		start.resizable(False, False)
		start.config(bg="gray10")
