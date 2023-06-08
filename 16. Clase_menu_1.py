try:
    a = int(input("ingrese 1er número\n"))
    b = int(input("ingrese 2do número\n"))
    c = a/b
    print(f"El resultado es {c}")
except:
    print("No se puede dividir por 0")
else:

    print("Tipo de dato incorrecto")
    
# ¿En que ocasión se puede caer en el else? el else sirve para filtrar que no pasen dats incorrectos a la operación siguiente