# Ingrese un número entero mayor a cero por teclado e indique si es o no “Primo”.

print("En este programa se te pedirá un número y el programa determinará si este es primo o no es primo")

num = int(input("Ingrese el número:\n"))
contador = 0

for i in range(2, num):
    if num % i == 0:
        contador = contador + 1

if contador > 0:
    print(f"El número {num} no es un número primo")
else:
    print(f"El número {num} es un número primo")
