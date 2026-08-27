import os

#! LIMPIAR
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#! PAUSAR
def pausar():
    input("\n[P] Presione ENTRAR para continuar . . .")

#! PEDIR DATO
def pedir_dato(mensaje):
    dato = input(mensaje)
    return dato
        
#! PEDIR ISBN
def pedir_isbn():
    while True:
        isbn = input("ISBN: ")
        if not isbn.isdigit():
            print("\n[!] El ISBN debe contener solo números.")
            pausar()
            continue
        if len(isbn) != 13:
            print("\n[!] El ISBN debe contener exactamente 13 dígitos.")
            pausar()
            continue
        return isbn
    
#! PEDIR CONFIRMACION
def pedir_confirmacion(mensaje):
    while True:
        opcion = input(mensaje).lower()
        if opcion == 's':
            return True
        elif opcion == 'n':
            return False
        else:
            print("[!] Opcion incorrecta. Intente de nuevo")
            pausar()
    
#! MENSAJE DE ERROR
def error():
    print("\n[!] Error. Intente de nuevo")