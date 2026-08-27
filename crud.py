from validaciones import validar_texto, validar_numero, validar_isbn
from datos import libros
from interfaz import limpiar_pantalla, pausar, pedir_dato, pedir_isbn, pedir_confirmacion, error

#! REGISTRO VACIO
def registro_vacio():
    if not libros:
        print("[!] No se encontraron libros.")
        pausar()
        return True
    return False

#! MOSTRAR LIBROS
def mostrar_libros(id_libro):
    print(f"\n| ID: {id_libro}")
    print(f"| Titulo: {libros[id_libro]['titulo']}")
    print(f"| Autor: {libros[id_libro]['autor']}")
    print(f"| ISBN: {libros[id_libro]['isbn']}")
    print(f"| Editorial: {libros[id_libro]['editorial']}")
    print(f"| Paginas: {libros[id_libro]['paginas']}")
    print(f"| Precio: ${libros[id_libro]['precio']}")
    print(f"| Disponible: {libros[id_libro]['disponible']}")
    
#! AGREGAR
def agregar_libro():
    limpiar_pantalla()
    print("\n-- AGREGAR NUEVO LIBRO --\n")
    print("Ingrese los siguientes datos >>\n")
    
    while True:
        id_libro = pedir_dato("ID: ") 
        id_libro_corregido = validar_numero(id_libro, 1)
        
        if id_libro_corregido == False:
            error()
            pausar()
            continue
        
        id_libro = id_libro_corregido
        
        if id_libro in libros:
            print("\n[!] El ID ya existe. Intente de nuevo")
            pausar()
            continue
        break 
        
    while True:
        titulo = pedir_dato("Titulo: ")
        titulo_corregido = validar_texto(titulo, 50) 
        
        if titulo_corregido == False:
            print("\n[!] Error. Intente de nuevo.")
            pausar()
            continue
        
        titulo = titulo_corregido
        break
        
    
    while True:
        autor = pedir_dato("Autor: ")
        autor_corregido = validar_texto(autor, 50)
        
        if autor_corregido == False:
            error()
            pausar()
            continue
        
        autor = autor_corregido
        break
    
    while True: 
        isbn_valido = True
        isbn = pedir_isbn()
        isbn_corregido = validar_isbn(isbn)
        
        if isbn_corregido == False:
            error()
            pausar()
            continue
        
        isbn = isbn_corregido
        
        for libro in libros.values():
            if libro["isbn"] == isbn_corregido:
                error()
                pausar()
                isbn_valido = False
                
        if isbn_valido == False:
            continue
        
        break
        
    while True:
        editorial = pedir_dato("Editorial: ") 
        editorial_corregido =  validar_texto(editorial, 50)
        
        if editorial_corregido == False:
            error()
            pausar()
            continue
        
        editorial = editorial_corregido
        break
    
    while True:
        paginas = pedir_dato("Paginas: ")
        paginas_corregido = validar_numero(paginas, 1)
        
        if paginas_corregido == False:
            error()
            pausar()
            continue
        
        paginas = paginas_corregido
        break
        
    while True:
        precio = pedir_dato("Precio: $")
        precio_corregido = validar_numero(precio, 1)
        if precio_corregido == False:
            error()
            pausar()
            continue
        
        precio = precio_corregido
        break
    
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "editorial": editorial,
        "paginas": paginas,
        "precio": precio,
        "disponible": True
    }
    
    libros[id_libro] = nuevo_libro
    
    print("\nSe agrego correctamente el libro:\n")
    mostrar_libros(id_libro)
    pausar()
    

#! EDITAR
def editar_libro():
    limpiar_pantalla()
    print("-- EDITOR DE LIBROS --")
    
    if registro_vacio():
        return
    
    while True:
        id_editar = pedir_dato("ID a editar: ")
        id_editar_corregido = validar_numero(id_editar, 1)
        if id_editar_corregido == False:
            error()
            pausar()
            continue
        
        id_editar = id_editar_corregido
        if id_editar not in libros:
            error()
            pausar()
            continue
        
        break
    
    print("\nIngrese los siguientes datos >>\n")
    
    while True:
        nuevo_titulo = pedir_dato("Titulo: ")
        nuevo_titulo_corregido = validar_texto(nuevo_titulo, 50)
        
        if nuevo_titulo_corregido == False:
            error()
            pausar()
            continue
        
        nuevo_titulo = nuevo_titulo_corregido
        break
        
    while True:
        nuevo_autor = pedir_dato("Autor: ")
        nuevo_autor_corregido = validar_texto(nuevo_autor, 50)
        
        if nuevo_autor_corregido == False:
            error()
            pausar()
            continue
        
        nuevo_autor = nuevo_autor_corregido
        break
        
    while True:
        nuevo_isbn_valido = True
        nuevo_isbn = pedir_isbn()
        nuevo_isbn_corregido = validar_isbn(nuevo_isbn)
        
        if nuevo_isbn_corregido == False:
            error()
            pausar()
            continue
        
        nuevo_isbn = nuevo_isbn_corregido
        
        for id_libro, libro in libros.items():
            if libro["isbn"] == nuevo_isbn and id_libro != id_editar:
                error()
                pausar()
                nuevo_isbn_valido = False
            
        if nuevo_isbn_valido == False:
            continue
        
        break
            
    
    while True:
        nuevo_editorial = pedir_dato("Editorial: ")
        nuevo_editorial_corregido = validar_texto(nuevo_editorial, 50)
        
        if nuevo_editorial_corregido == False:
            error()
            pausar()
            continue
        
        nuevo_editorial = nuevo_editorial_corregido
        break
    
    while True:
        nuevo_paginas = pedir_dato("Paginas: ")
        nuevo_paginas_corregido = validar_numero(nuevo_paginas, 1)
        
        if nuevo_paginas_corregido == False:
            error()
            pausar()
            continue
        
        nuevo_paginas =  nuevo_paginas_corregido
        break
    
    while True:
        nuevo_precio = pedir_dato("Precio: $")
        nuevo_precio_corregido = validar_numero(nuevo_precio, 1)
        
        if nuevo_precio_corregido == False:
            error()
            pausar()
            continue
        
        nuevo_precio = nuevo_precio_corregido
        break
        
            
    nuevo_estatus = pedir_confirmacion("\nDisponible? (S/N): ")
    
    libro_editado = {
        "titulo": nuevo_titulo,
        "autor": nuevo_autor,
        "isbn": nuevo_isbn,
        "editorial": nuevo_editorial,
        "paginas": nuevo_paginas,
        "precio": nuevo_precio,
        "disponible": nuevo_estatus
    }
    
    libros[id_editar] = libro_editado
    
    print("\nSe edito correctamente el libro:\n")
    mostrar_libros(id_editar)
    pausar()
    
#! ELIMINAR
def eliminar_libro():
    limpiar_pantalla()
    print("\n-- ELIMINAR LIBRO --\n")
    
    if registro_vacio():
        return
    
    while True:
        id_eliminar = pedir_dato("ID a editar: ")
        id_eliminar_corregido = validar_numero(id_eliminar, 1)
        if id_eliminar_corregido == False:
            error()
            pausar()
            continue
        
        id_eliminar = id_eliminar_corregido
        if id_eliminar not in libros:
            error()
            pausar()
            continue
        
        break
    
    print("\nLibro encontrado:")
    mostrar_libros(id_eliminar)
    
    if pedir_confirmacion("\n¿Desea eliminar el libro? (S/N): "):
        del libros[id_eliminar]
        print("\nEl Libro ha sido eliminado correctamente!")
        pausar()
    else:
        print("\nEl libro no ha sido eliminado.")
        pausar()

#! BUSCAR
def buscar_libro():
    limpiar_pantalla()
    print("\n-- BUSCADOR DE LIBROS --\n")
    
    if registro_vacio():
        return
    
    while True:
        id_buscar = pedir_dato("ID a buscar: ")
        id_buscar_corregido = validar_numero(id_buscar, 1)
        if id_buscar_corregido == False:
            error()
            pausar()
            continue
        
        id_buscar = id_buscar_corregido
        
        if id_buscar not in libros:
            error()
            pausar()
            continue
        
        break
        
    print("\nLibro encontrado:\n")
    mostrar_libros(id_buscar)
    pausar()
    return

#! LISTAR
def listar_libros():
    limpiar_pantalla()
    print("\n-- LISTADO DE LIBROS --\n")
    
    if registro_vacio():
        return
    
    for id_libro in libros:
        mostrar_libros(id_libro)
    pausar()