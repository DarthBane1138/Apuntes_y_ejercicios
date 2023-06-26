def calculoiva(precio, iva):
    return print("El precio con IVA de su producto es de", precio * iva)


def descuento(precio, descuento):
    descuento = descuento / 100
    precio = precio - (precio * descuento)
    descuento = descuento * 100
    precio = int(precio)
    return print(f"El precio con un descuento del {descuento}% es de ${precio}")


def imc(peso, estatura):
    imc = (peso / estatura ** 2)
    return imc


def indicadorimc(imc):
    if imc < 18.5:  # Acá arroja un error
        return print("Estás bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        return print("Estás en un peso adecuado")
    elif imc >= 25 and imc <= 29.9:
        return print("Estás sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        return print("Estás obeso grado 1")
    elif imc >= 35 and imc <= 39.9:
        return print("Estás obeso grado 2")
    elif imc > 40:
        return print("Estás obeso grado 3")
