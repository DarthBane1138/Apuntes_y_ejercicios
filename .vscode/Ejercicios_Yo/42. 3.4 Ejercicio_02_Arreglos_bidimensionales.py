# Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive, luego esos números serán las dimensiones de un arreglo bidimensional. Posteriormente, poblar la matriz con números reales. Finalmente, muestre:
# El arreglo poblado.
# La suma por filas.
# El promedio por columnas.

import numpy as np

num1 = 1
num2 = 1

while (num1 < 3 or num1 > 6) or (num2 < 3 or num2 > 6):
    try:
        num1 = int(
            input("Ingrese un primer número entre el 3 y el 6 ambos inclusive:\n"))
        num2 = int(
            input("Ingrese un segundo número entre el 3 y el 6 ambos inclusive:\n"))
        if (num1 >= 3 and num1 <= 6) and (num2 >= 3 and num2 <= 6):
            print("Valores ingresados")
        else:
            print("Uno de los valores ingresados no está en el rango solicitado")
    except ValueError:
        print("El valor ingresado es un valor no válido")

matriz = np.zeros((num1, num2))
print(matriz)
# print(matriz)
# matriz = np.random.randint(num1, num2)
# print(matriz)

matriz = np.random.randint(1, 51, (num1, num2))

# Imprimir la matriz
print(matriz)

for i in range(num1):
    print("Suma elementos fila", i, ":", matriz[i, :].sum())

for e in range(num1):
    promedio_fila = np.mean(matriz[e, :])
    print("Promedio de la fila", e, ":", promedio_fila)
