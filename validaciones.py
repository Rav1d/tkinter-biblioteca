def validar_titulo(titulo):
    titulo_corregido = titulo.strip()
    if len(titulo_corregido) == 0:
        return False
    elif len(titulo_corregido) > 100:
        return False
    else:
        return titulo_corregido
    
def validar_texto(texto, maximo):
    texto_corregido = texto.strip()
    if len(texto_corregido) == 0:
        return False
    elif len(texto_corregido) > maximo:
        return False
    else: 
        return texto_corregido
    
def validar_numero(numero, minimo):
    try:
        numero_corregido = int(numero)
    except ValueError:
        return False
    if numero_corregido < minimo:
        return False
    else:
        return numero_corregido

def validar_isbn(isbn):
    isbn_corregido = isbn.strip()
    if len(isbn_corregido) == 13 and isbn_corregido.isdigit():
        return isbn_corregido
    return False        