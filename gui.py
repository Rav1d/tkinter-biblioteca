import tkinter as tk

def hola():
    print("Hola")
    
ventana = tk.Tk()

ventana.title("Sistema de Gestión de Libros")

boton = tk.Button(ventana, text="1. Agregar libro", command=hola)
boton.pack()


ventana.mainloop()