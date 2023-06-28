# 2).- Crear un Arreglo [3][3] manualmente, los valores del arreglo pueden ser “amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.
# Una vez completado, mostrar la siguiente información:
# ●	Número de elementos “amarillo”.
# ●	Número de elementos “rojo”.
# ●	Número de elementos “Naranja”.
# ●	Número de elementos “Verde”.
# ●	Número de elementos “Blanco”

import os
import numpy as np


print("En la siguiente aplicación rellenaremos una matriz con strings de distintos colores")
colores = """
Las opciones son:
- Amarillo
- Rojo
- Naranja
- Verde
- Blanco"""
print(colores)

matriz = np.empty((3, 3), dtype=object)
print(matriz)

# Ahora toca pedirle, posición por posición que el usuario rellene cada una de las ubicaciones
for i in range(3):
    for e in range(3):
        color = ""
        while color not in ["amarillo", "rojo", "naranja", "verde", "blanco"]:
            os.system("cls")
            print(colores)
            color = input(f"Ingrese un color para la posición [{i}][{e}]:\n")
            color = color.lower()
            if color not in ["amarillo", "rojo", "naranja", "verde", "blanco"]:
                print(
                    "El color que has escrito no se encuentra dentro de las opciones disponibles")
                input("Presione enter para continuar...")
            else:
                print(f"Color {color} se ha agregado a la matriz")
                # Acá es donde se selecciona el lugar en la matriz que se insertará, el valor de [i], y [e] se determina en el lugar que estemos en el for
                matriz[i][e] = color
                input("Presione enter para continuar...")

conteo_colores = {
    "amarillo": 0,
    "rojo": 0,
    "naranja": 0,
    "verde": 0,
    "blanco": 0
}
# En esta parte, el referenciar uno de los elementos escritos en en esta lista hace que el número sume en 1 a diferencia de el otro de las funciones que se refería a un string como un elemento de la variable uin conjunto de datos que son distintos

for i in matriz:
    for e in i:
        if e in conteo_colores:
            conteo_colores[e] += 1
# Esta función me costó -----> En le primer for


# Mostrar la información de conteo
print("Número de elementos 'Amarillo':", conteo_colores["amarillo"])
print("Número de elementos 'Rojo':", conteo_colores["rojo"])
print("Número de elementos 'Naranja':", conteo_colores["naranja"])
print("Número de elementos 'Verde':", conteo_colores["verde"])
print("Número de elementos 'Blanco':", conteo_colores["blanco"])
