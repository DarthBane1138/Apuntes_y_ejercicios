# Ingrese tres números enteros, si son mayores a cero y par, entonces súmelos, sino cuéntelos

n1 = 1.1
n2 = 1.1
n3 = 1.1

while n1 % 1 != 0 or n2 % 1 != 0 or n3 % 1 != 0:
    n1 = float(input("Ingrese el primer número:\n"))
    n2 = float(input("Ingrese el segundo número:\n"))
    n3 = float(input("Ingrese el tercer número:\n"))
    if n1 % 1 != 0 or n2 % 1 != 0 or n3 % 1 != 0:  # Primero se verifica que no sean decimales
        print("Uno o más números no son enteros, favor solo ingresar números enteros")
    elif n1 % 2 != 0 or n2 % 2 != 0 or n3 % 2 != 0:  # Si son impares entran en este elif
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        print(
            f"Uno de los números es impar, los números ingresados son {n1}, {n2}, {n3}")
    elif n1 > 0 and n2 > 0 and n1 > 0:  # Si no cumplen con ninguna restricción, entonces enteros, pares y mayores que 0
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        res = n1 + n2 + n3
        print(
            f"Todos los números son pares, la suma de {n1}, {n2}, {n3} es {res}")
    else:
        print("Uno de los números es un número menor o igual a 0")
