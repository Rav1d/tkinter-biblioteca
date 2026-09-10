import tkinter as tk
from validaciones import validar_texto, validar_numero, validar_isbn
from datos import libros

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
nuevo_libro = {}

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
    
def regresar():
    cambiar_frame(frame_agregar, frame_menu)
    
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

def validar_campo_numero(diccionario_agregar, diccionario_errores, nombre_llave, mensaje):
    nombre_campo = diccionario_agregar[nombre_llave].get()
    campo_corregido = validar_numero(nombre_campo, 1)
    if campo_corregido == False:
        diccionario_errores[nombre_llave].configure(text=mensaje)
    else:
        diccionario_errores[nombre_llave].configure(text="")
        
    return campo_corregido

def validar_campo_isbn(diccionario_agregar, diccionario_errores, mensaje):
    isbn = diccionario_agregar["isbn"].get()
    isbn_corregido = validar_isbn(isbn)
    if isbn_corregido == False:
        diccionario_errores["isbn"].configure(text=mensaje)
        return False
    
    for libro in libros.values():
        if libro["isbn"] == isbn_corregido:
            diccionario_errores["isbn"].configure(text=mensaje)
            return False
    
    diccionario_errores["isbn"].configure(text="")
    return isbn_corregido

def validar_campo_id(diccionario_agregar, diccionario_errores, mensaje):
    id_libro = diccionario_agregar["id"].get()
    id_libro_corregido = validar_numero(id_libro, 1)
    if id_libro_corregido == False:
        diccionario_errores["id"].configure(text=mensaje)
        return False
    
    if id_libro_corregido in libros:
        diccionario_errores["id"].configure(text=mensaje)
        return False
    
    diccionario_errores["id"].configure(text="")
    return id_libro_corregido
    
    
def guardar_libro():
    id_libro =  validar_campo_id(entries_agregar, errores_agregar, "ID no valido o ya existe")
    titulo = validar_campo_texto(entries_agregar, errores_agregar, "titulo", "Titulo no valido")
    autor = validar_campo_texto(entries_agregar, errores_agregar, "autor", "Autor no valido")
    editorial = validar_campo_texto(entries_agregar, errores_agregar, "editorial", "Editorial no valida")
    isbn = validar_campo_isbn(entries_agregar, errores_agregar, "ISBN no valido o ya existe")
    paginas = validar_campo_numero(entries_agregar, errores_agregar, "paginas", "No. de paginas no valido")
    precio = validar_campo_numero(entries_agregar, errores_agregar, "precio", "Precio no valido")
    
    if id_libro != False and titulo != False and autor != False and editorial != False and isbn != False and paginas != False and precio != False:
        
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "editorial": editorial,
            "isbn": isbn,
            "paginas": paginas,
            "precio": precio,
            "disponible": True
        }
        
        libros[id_libro] = nuevo_libro
        mensaje_guardado.configure(text="Libro guardado correctamente")
        for entry in entries_agregar.values():
            entry.delete(0, tk.END)
    
        
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
mensaje_guardado = label(frame_agregar, "")
boton(frame_agregar, "Regresar", regresar)

#! FRAME MENU
frame_menu.pack()

ventana.mainloop()