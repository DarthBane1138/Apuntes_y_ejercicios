# Declarar y poblar un arreglo unidimensional de largo 10 con números enteros positivos, utilizando la función random, luego ingrese un número e indique si éste se encuentra en el arreglo.

import random

# Declaro un rreglo vacío
arreglo = []
for i in range(10):
    # Se genera un número entero aleatorio entre 1 y 100
    numero = random.randint(1, 100)
    # El append es para que los números generados se vayan incorporando a el arreglo
    arreglo.append(numero)

print("Arreglo:", arreglo)  # Imprime Arreglo: "la lista de arreglo"

# Ingresar un número y comprobar se se encuentra en el arreglo

numero_buscado = -1
while numero_buscado < 0:
    try:
        numero_buscado = int(input("Ingrese un número entero positivo:\n"))
        if numero_buscado >= 0:
            print("Gracias")
        else:
            print("El número ingresado es un número negativo")
    except ValueError:
        print("El valor ingresado no es un valor válido")

if numero_buscado in arreglo:
    print("El número", numero_buscado, "Sí se encuentra en el arreglo")
else:
    print("El número buscado", numero_buscado, "No se encuentra en el arreglo")
