# 1).- Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla utilizando doble for, mostrar los elementos por pantalla de forma ordenada como una matriz, tal cual muestra el ejemplo:

# 3	10	4	16
# 1	7	8	-7
# 9	-1	3	9

import numpy as np

matriz = np.zeros((3, 3))
print(matriz)

for i in range(3):
    for e in range(3):
        matriz[i][e] = int(
            input(f"Ingrese un número para la posición [{i}][{e}]:\n"))

print(matriz)
