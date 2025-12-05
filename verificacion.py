from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import threading
import random
from tkinter import messagebox
import asyncio
import time


miemail = "User2442E@gmail.com"
micontra = "skhf cwfc yclf fhzl"

funciono=None
correo_usar=None
codigo=None
ventana_usar=None
def verificando(correo,stringvar,ventana,bloquedespues):

	global funciono,correo_usar,codigo,ventana_usar
	ventana_usar=ventana
	correo_usar=correo

	if not correo or "@" not in correo:
		messagebox.showerror("ERROR", "Debe ingresar un email válido",parent=ventana_usar)
		stringvar.set("")
		return

	codigo = str(random.randint(100000, 999999))
	print(codigo)

	hilo = threading.Thread(target=enviar_email,daemon=True)
	hilo.start()
	hilo.join()

	if funciono:
		bloquedespues.place(x=500,y=600)
		return codigo
	else:
		messagebox.showerror("Error","El correo no es válido",parent=ventana_usar)
	


def enviar_email():
	global miemail,micontra,funciono,correo_usar,codigo

	try:
		mensaje = MIMEMultipart()
		mensaje["From"] = miemail
		mensaje["To"] = correo_usar
		mensaje["Subject"] = "Código de verificación"

		escrito = f"""
		Código de verificación

		Este es su código: {codigo}"""
		mensaje.attach(MIMEText(escrito, "plain"))

		servidor = smtplib.SMTP("smtp.gmail.com", 587)
		servidor.starttls()
		servidor.login(miemail, micontra)
		servidor.send_message(mensaje)
		servidor.quit()
		funciono=True
		print("1")

	except Exception as e:
		print(f"Error enviando email: {e}")
		funciono=False
		print("falseee")


def enviar_email_outl():
	global miemail,micontra,funciono,correo_usar,codigo

	try:
		mensaje = MIMEMultipart()
		mensaje["From"] = miemail
		mensaje["To"] = correo_usar
		mensaje["Subject"] = "Código de verificación"

		escrito = f"""
		Código de verificación

		Este es su código: {codigo}"""
		mensaje.attach(MIMEText(escrito, "plain"))

		servidor = smtplib.SMTP("smtp.microsoft365.com", 587)
		servidor.starttls()
		servidor.login(miemail, micontra)
		servidor.send_message(mensaje)
		servidor.quit()
		funciono=True
		print("1")
		
	except Exception as e:
		print(f"Error enviando email: {e}")
		funciono=False
		



        
        

