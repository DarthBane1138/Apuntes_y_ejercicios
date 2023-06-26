def resta(a, b):
    return a - b


def funcion():
    return "Bienvenidos a Python"


def resta2(a=None, b=None):
    if a == None or b == None:
        print("Error, faltan parámetros a la función")
        return
    return a - b


def calculo(precio, descuento):
    return precio - (precio * descuento / 100)


def saludo(nombre, mensaje="Python"):
    print(mensaje, nombre)
