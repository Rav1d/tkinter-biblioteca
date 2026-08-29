import tkinter as tk

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Libros")

def hola():
    print("Hola")
    
def boton(mensaje, funcion):
    boton = tk.Button(ventana, text=mensaje, command=funcion)
    boton.pack()
    
def boton_salir(mensaje):
    boton = tk.Button(ventana, text=mensaje, command=ventana.destroy)
    boton.pack()
    
boton("1. Agregar libro", hola)
boton("2. Editar libro", hola)
boton("3. Eliminar libro", hola)
boton("4. Buscar libro", hola)
boton("5. Listar libro", hola)
boton_salir("6. Salir")

ventana.mainloop()