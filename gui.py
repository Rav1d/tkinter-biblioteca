import tkinter as tk
from validaciones import validar_texto

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Libros")

def hola():
    print("hola")
    
#! FRAMES
frame_menu = tk.Frame(ventana)
frame_agregar = tk.Frame(ventana)

#! DICCIONARIOS
entries_agregar = {}
errores_agregar = {}    

#! FUNCIONES
def boton(raiz, mensaje, funcion):
    boton = tk.Button(raiz, text=mensaje, command=funcion)
    boton.pack()
    
def boton_salir(raiz, mensaje):
    boton = tk.Button(raiz, text=mensaje, command=ventana.destroy)
    boton.pack()
    
def label(raiz, mensaje):
    label = tk.Label(raiz, text=mensaje)
    label.pack()
    return label
    
def entry(raiz):
    campo = tk.Entry(raiz)
    campo.pack()
    return campo

def cambiar_frame(ocultar, mostrar):
    ocultar.pack_forget()
    mostrar.pack()
    
def ir_a_agregar():
    cambiar_frame(frame_menu, frame_agregar)

def ingresar_dato(raiz, mensaje, diccionario, diccionario_errores, llave):
    label(raiz, mensaje)
    diccionario[llave] = entry(raiz)
    diccionario_errores[llave] = label(raiz, "")
    
def validar_campo_texto(diccionario_agregar, diccionario_errores, nombre_llave, mensaje):
    nombre_campo = diccionario_agregar[nombre_llave].get()
    campo_corregido = validar_texto(nombre_campo, 50)
    if campo_corregido == False:
        diccionario_errores[nombre_llave].configure(text=mensaje)
    else:
        diccionario_errores[nombre_llave].configure(text="")
        
    return campo_corregido
    
def guardar_libro():
    titulo = validar_campo_texto(entries_agregar, errores_agregar, "titulo", "Titulo no valido")
    autor = validar_campo_texto(entries_agregar, errores_agregar, "autor", "Autor no valido")
    editorial = validar_campo_texto(entries_agregar, errores_agregar, "editorial", "Editorial no valida")
        
    
#! MENU  
boton(frame_menu, "1. Agregar libro", ir_a_agregar)
boton(frame_menu, "2. Editar libro", hola)
boton(frame_menu, "3. Eliminar libro", hola)
boton(frame_menu, "4. Buscar libro", hola)
boton(frame_menu, "5. Listar libro", hola)
boton_salir(frame_menu, "6. Salir")

#! AGREGAR

label(frame_agregar, "AGREGAR NUEVO LIBRO")

ingresar_dato(frame_agregar, "ID", entries_agregar, errores_agregar, "id")
ingresar_dato(frame_agregar, "Titulo", entries_agregar, errores_agregar, "titulo")
ingresar_dato(frame_agregar, "Autor", entries_agregar, errores_agregar, "autor")
ingresar_dato(frame_agregar, "ISBN", entries_agregar, errores_agregar, "isbn")
ingresar_dato(frame_agregar, "Editorial", entries_agregar, errores_agregar, "editorial")
ingresar_dato(frame_agregar, "Paginas", entries_agregar, errores_agregar, "paginas")
ingresar_dato(frame_agregar, "Precio", entries_agregar, errores_agregar, "precio")
boton(frame_agregar, "Guardar", guardar_libro)

#! FRAME MENU
frame_menu.pack()

ventana.mainloop()