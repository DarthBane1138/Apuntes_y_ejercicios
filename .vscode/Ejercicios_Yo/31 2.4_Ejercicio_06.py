# Genere las 10 primeras tablas de multiplicar, cada una de ellas de 1 a 10.

print("En este script te pediremos un número para poder calcular su tabla de multiplicar")

i = 0
num = 0

while num <= 0:
    try:
        num = int(input("Ingrese un número entero:\n"))
    except ValueError:
        print("Debe ingresar un número entero")

while i != 10:
    i = i + 1
    mult = i * num
    print(f"{i} * {num} = {mult}")
