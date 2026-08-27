from crud import agregar_libro, editar_libro, eliminar_libro, listar_libros, buscar_libro
from interfaz import limpiar_pantalla, pausar

#! MENU
def menu():
    while True:
        limpiar_pantalla()
        print("\n-- SISTEMA DE ADMINISTRACION LIBRERIA --\n")
        print("1. Agregar nuevo libro")
        print("2. Editar libro existente")
        print("3. Eliminar libro existente")
        print("4. Listar libros")
        print("5. Buscar libro")
        print("6. Salir")
        opcion = input("\nSeleccione una opcion: ")
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            editar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            listar_libros()
        elif opcion == "5":
            buscar_libro()
        elif opcion == "6":
            return
        else:
            print("\n[!] Opcion incorrecta. Intente de nuevo")
            pausar()

#! MAIN
menu()