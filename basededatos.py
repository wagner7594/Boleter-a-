import sqlite3
from tkinter import messagebox

def conectar_db():
    conn = sqlite3.connect('base_datos.db')
    return conn

def crear_tabla():
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         nombre TEXT NOT NULL, 
                         email TEXT UNIQUE NOT NULL, 
                         password TEXT NOT NULL)''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error al crear tabla: {e}")

def guardar_usuario(nombre, email, password):
    try:
        crear_tabla()
        
        conn = conectar_db()
        cursor = conn.cursor()
    
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)", 
                      (nombre, email, password))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        return True
        
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El email ya está registrado")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar usuario: {str(e)}")
        return False

def validar_login(usuario,contra, ventana):
    conn=conectar_db()
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND password = ?", (usuario,contra))
    resultado= cursor.fetchone()
    conn.commit()
    conn.close()

    if resultado:
        messagebox.showinfo("Bien","El usuario fue encontrado", parent=ventana)
        return True
    else:
        messagebox.showerror("Mal","EL usuario no fue encontrado", parent=ventana)
        return False
def comprobar_correo(correo,ventana):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (correo,))
    comprobado=cursor.fetchone()
    conn.close()

    if comprobado:
        messagebox.showerror("Error", "El email ya está registrado",parent=ventana)
        return False


    else:    
        return True   
 
crear_tabla()