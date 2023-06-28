# 1).- Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla utilizando doble for
# mostrar los elementos por pantalla de forma ordenada como una matriz, tal cual muestra el ejemplo:
# 3	10	4	16
# 1	7	8	-7
# 9	-1	3	9

# # Crear el arreglo de 3x4
# arreglo = [[0] * 4 for _ in range(3)]

# # Ingresar los elementos numéricos por pantalla
# import numpy as np
# for i in range(3):
#     for j in range(4):
#         arreglo[i][j] = int(
#             input(f"Ingrese el elemento en la posición [{i}][{j}]: "))

# # Mostrar los elementos en forma de matriz
# for i in range(3):
#     for j in range(4):
#         print(arreglo[i][j], end="\t")
#     print()  # Salto de línea después de cada fila


# # Crear el arreglo de 3x4 con NumPy
# arreglo = np.zeros((3, 4))
# # La función zeros se utiliza para que se cree una matriz llena de ceros que será la que se rellenará después
# # print(arreglo)

# # # Ingresar los elementos numéricos por pantalla
# for i in range(3):
#     for j in range(4):
#         arreglo[i][j] = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))

# # # Mostrar los elementos en forma de matriz
# print(arreglo)

# 2).- Crear un Arreglo [3][3] manualmente, los valores del arreglo pueden ser “amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.
# Una vez completado, mostrar la siguiente información:
# ●	Número de elementos “amarillo”.
# ●	Número de elementos “rojo”.
# ●	Número de elementos “Naranja”.
# ●	Número de elementos “Verde”.
# ●	Número de elementos “Blanco”

# mensaje = """Ingrese alguno de los siguientes valores:
# - Amarillo
# - Rojo
# - Naranja
# - Verde
# - Blanco"""

# import numpy as np

# # Crear una matriz vacía de 3x3
# matriz = np.empty((3, 3), dtype=object)

# # Pedir al usuario los colores uno por uno y llenar la matriz
# for i in range(3):
#     for j in range(3):
#         color = ""
#         while color not in ["amarillo", "rojo", "naranja", "verde", "blanco"]:
#             color = input(f"Ingrese el color para la posición [{i}][{j}]: ")
#             color = color.lower()
#             if color not in ["amarillo", "rojo", "naranja", "verde", "blanco"]:
#                 print(f"El color {color}, no está dentro de las opciones")
#             matriz[i][j] = color
#             # La línea "matriz[i][j] = color" asigna el valor de "color" a la posición [i][j] de la matriz.
#             # Esta función permite ir rellenando cada uno de los valores con el color ingresado en la variable color
#             # La ubicación de la matriz está determinada por la posición de acuerdo al for correspondiente

# # Mostrar los valores de la matriz
# print("Valores de la matriz:")
# for fila in matriz:
#     print(fila)

# # Contar el número de elementos de cada color
# conteo_colores = {
#     "amarillo": 0,
#     "rojo": 0,
#     "naranja": 0,
#     "verde": 0,
#     "blanco": 0
# }

# for fila in matriz:
#     for elemento in fila:
#         if elemento in conteo_colores:
#             conteo_colores[elemento] += 1

# # Mostrar la información de conteo
# print("Número de elementos 'Amarillo':", conteo_colores["amarillo"])
# print("Número de elementos 'Rojo':", conteo_colores["rojo"])
# print("Número de elementos 'Naranja':", conteo_colores["naranja"])
# print("Número de elementos 'Verde':", conteo_colores["verde"])
# print("Número de elementos 'Blanco':", conteo_colores["blanco"])

# Crear un Arreglo [10][4] en el cual simula un bus, tendrá que darle de forma automática los números de asiento y luego mostrarlo por pantalla de la siguiente forma

# 1	    2	3	4
# 5	    6	7	8
# 9	    10	11	12
# 13	14	15	16
# 17	18	19	20
# 21	22	23	24
# 25	26	27	28
# 29	30	31	32
# 33	34	35	36
# 37	38	39	40

arreglo = [[0] * 4 for _ in range(10)]
print(arreglo)

# Ingresar los elementos numéricos por pantalla
for i in range(10):
    for j in range(4):
        arreglo[i][j] = int(
            input(f"Ingrese el elemento en la posición [{i}][{j}]: "))

# Mostrar los elementos en forma de matriz
for i in range(10):
    for j in range(4):
        print(arreglo[i][j], end="\t")
    print()  # Salto de línea después de cada fila
