# Crear un arreglo unidimensional de tamaño 10,
# con elementos aleatorios de números enteros del 0 al 100, para
# ello deberá investigar la función que permita crear números aleatorios

import numpy as np

arreglo = np.random.randint(0, 101, 10)
print(arreglo)

# Crear una copia del arreglo y muestre:
arreglo1 = arreglo[:].copy()
# Elemento mayor
print(arreglo1.max())
# Elemento menor
print(arreglo1.min())
# Suma de los elementos
print(arreglo1.sum())
# Promedio de los elementos
print(arreglo1.mean())
# Mostrar todos los elementos
print(arreglo1)
