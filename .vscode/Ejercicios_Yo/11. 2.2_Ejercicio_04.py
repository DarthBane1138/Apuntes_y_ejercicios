# Ingrese por teclado un número entero mayor a 1 y menor a 101 por teclado, luego indique si es par o impar.

num = 0

while num <= 1 or num >= 101 or num % 1 != 0:
    num = float(
        input("Por favor ingrese un número entero mayor a 1 y menor a 101:\n"))
    if num % 1 != 0:
        print(f"El número {num} ingresado no es un número entero")
    elif num % 2 == 0 and num > 1 and num < 101:
        print(f"El número ingresado es el {num}, este es un número par")
    elif num % 2 != 5 and num > 1 and num < 101:
        print(f"El número ingresado es el {num}, este es un número impar")
    elif num <= 1:
        print(
            f"El número {num} es menor o igual a 1, por favor ingresar un número mayor a 1 y menor a 101")
    elif num >= 101:
        print(
            f"El número {num} es mayor o igual a 101, por favor ingresar un número mayor a 1 y menor a 101")
