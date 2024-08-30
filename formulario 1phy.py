import tkinter as tk
from tkinter import messagebox

# Definición de funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    # Limpiar radiobutton
    var_genero.set(0)

def borrar():
    limpiar_campos()

def guardar_valores():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    # Obtener género de los radiobuttons 
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    
    # Generar la cadena de caracteres 
    datos = ("Nombres: " + nombres + "\n" +
             "Edad: " + edad + "\n" +
             "Apellidos: " + apellidos + "\n" +
             "Telefono: " + telefono + "\n" +
             "Estatura: " + estatura + "\n" +
             "Genero: " + genero + "\n")
    
    try:
        
        with open("C:/Users/fabiola velas/OneDrive/Documentos/3MSEMESTRE/PROGRAMACION AVANZADA.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n\n")
        messagebox.showinfo("Información", "Datos guardados con éxito:\n\n" + datos)
    except IOError as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

# Creación de ventana 
ventana = tk.Tk()
ventana.geometry("720x500") # Tamaño de ventana
ventana.title("Formulario v.1")

# Creación de etiquetas y campos de entrada 
# Variable para el radiobutton
var_genero = tk.IntVar()

lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono:")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Genero:")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

# Creación de botones 
btBorrar = tk.Button(ventana, text="Borrar valores", command=borrar)
btBorrar.pack()

btGuardar = tk.Button(ventana, text="Guardar valores", command=guardar_valores)
btGuardar.pack()

# Ejecución de ventana 
ventana.mainloop()
