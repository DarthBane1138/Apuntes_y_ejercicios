# Ingresar por teclado 5 números enteros, luego debe indicar:
# Cuántos números son mayores a cero
# Sume los números pares
# Mostrar los resultados

print("En este programa se te pedirán 5 números enteros")
print("Se te mostrarán cuantos de ellos son mayores a 0")
print("Y cuantos de ellos son pares")

i = 1
mayor_cero = 0
menor_cero = 0
par = 0

while i <= 5:
    num = input(f"Ingrese el valor número {i}:\n")
    try:
        num = int(num)
        if num >= 0:
            mayor_cero = mayor_cero + 1
            i = i + 1
            if num % 2 == 0:
                par = par + 1
        elif num < 0:
            menor_cero = menor_cero + 1
            i = i + 1
            if num % 2 == 0:
                par = par + 1
                i = i + 1
    except ValueError:
        print(f"El número {num} no es un número entero")

print(f"----- Ingresaste {mayor_cero} números mayores a 0 -----")
print(f"----- Ingresaste {par} números pares -----")
