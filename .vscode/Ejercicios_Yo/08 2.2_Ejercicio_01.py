# Ingrese por teclado dos números enteros e indique cuál de ellos es el mayor.

num1 = int(input("Ingrese primer número:\n"))
num2 = int(input("Ingrese segundo número:\n"))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}")
