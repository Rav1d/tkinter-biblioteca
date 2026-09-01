import tkinter as tk

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Libros")

def hola():
    print("hola")
    
#! FRAMES
frame_menu = tk.Frame(ventana)
frame_agregar = tk.Frame(ventana)

#! FUNCIONES
def cambiar_frame(ocultar, mostrar):
    ocultar.pack_forget()
    mostrar.pack()
    
def ir_a_agregar():
    cambiar_frame(frame_menu, frame_agregar)
    
def boton(raiz, mensaje, funcion):
    boton = tk.Button(raiz, text=mensaje, command=funcion)
    boton.pack()
    
def boton_salir(raiz, mensaje):
    boton = tk.Button(raiz, text=mensaje, command=ventana.destroy)
    boton.pack()
    
def label(raiz, mensaje):
    label = tk.Label(raiz, text=mensaje)
    label.pack()
    
def entry(raiz):
    campo = tk.Entry(raiz)
    campo.pack()
    return campo

    
#! MENU  
boton(frame_menu, "1. Agregar libro", ir_a_agregar)
boton(frame_menu, "2. Editar libro", hola)
boton(frame_menu, "3. Eliminar libro", hola)
boton(frame_menu, "4. Buscar libro", hola)
boton(frame_menu, "5. Listar libro", hola)
boton_salir(frame_menu, "6. Salir")

#! AGREGAR
entries_agregar = {}

label(frame_agregar, "AGREGAR NUEVO LIBRO")

label(frame_agregar, "ID")
entries_agregar["id"] = entry(frame_agregar)

label(frame_agregar, "Titulo")
entries_agregar["titulo"] = entry(frame_agregar)

label(frame_agregar, "Autor")
entries_agregar["autor"] = entry(frame_agregar)

label(frame_agregar, "ISBN")
entries_agregar["isbn"] = entry(frame_agregar)

label(frame_agregar, "Editorial")
entries_agregar["editorial"] = entry(frame_agregar)

label(frame_agregar, "Paginas")
entries_agregar["paginas"] = entry(frame_agregar)

label(frame_agregar, "Precio")
entries_agregar["precio"] = entry(frame_agregar)

#! FRAME MENU
frame_menu.pack()

ventana.mainloop()