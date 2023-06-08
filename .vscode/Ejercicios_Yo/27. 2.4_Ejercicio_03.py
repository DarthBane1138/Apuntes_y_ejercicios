# Ingrese por teclado un número entero positivo entre 103 y 987, luego genere un proceso que permita invertir el número, aplicando las 4 operaciones matemáticas básicas (suma, resta, multiplicación y división). Finalmente, muestre el resultado.

num = 1

while num < 103 or num > 987:
    num = input(
        "Ingrese un número entero positivo entre 103 y 987 para poder invertirlo:\n")
    try:
        num = int(num)
        if num >= 103 and num <= 987:
            num1 = num % 10
            num1 = num1 * 10
            num2 = (num // 10) % 10
            numf = (num1 + num2) * 10
            numf = numf + (num // 100)
            print(f"El número invertido es {numf}")
        else:
            print("Has ingresado un número fuera del rango indicado")
            print("Este debe ser mayor o igual a 103 y menor o igual a 987")
    except ValueError:
        print("Debe ingresar un número entero")
        num = 1
