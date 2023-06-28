def calcular_digito_verificador(rut):
    rut = rut.replace(".", "")  # Eliminar puntos y guiones

    # Calcular el dígito verificador
    multiplicador = 2
    suma = 0
    for digito in reversed(rut):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    # Obtener el dígito verificador
    resto = suma % 11
    dv = 11 - resto
    if dv == 10:
        dv = "K"
    elif dv == 11:
        dv = "0"

    return str(dv)


# Ejemplo de uso
rut = input("Introduzca un rut sin dígito verificador:\n")
digito_verificador = calcular_digito_verificador(rut)
print("Dígito verificador:", digito_verificador)
