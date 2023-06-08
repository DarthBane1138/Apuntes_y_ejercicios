# Ingrese un número entero mayor a cero por teclado e indique si es o no “Perfecto”. Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos

print("Ingrese un número y te diré si es un número perfecto")
print("\n")

i = 0
suma = 0
num = -1

while num < 0:
    try:
        num = int(input("Ingrese número entero positivo:\n"))
        if num < 0:
            print("El número ingresado es un número negativo")
        elif num >= 0:
            while i < num:
                i = i + 1
                if num % i == 0 and num != i:
                    suma = suma + i
    except ValueError:
        print("El número ingresado no es un número entero")

if suma == num:
    print(f"El número {num} es un número perfecto")
else:
    print(f"El número {num} no es un número perfecto")
