import numpy as np
import random
#creacion de arrays  (metodo listas)
esp = ['barcelona', 'real', 'betis']
bra = ['flamengo', 'gremio', 'santos']
chi = ['huachipato', 'audax', 'cobresal']

#creacion de array bidimensional
futbol = [esp, bra, chi]
# print(futbol)
#recoorremos el array
# for fila in futbol:
#     for columna in fila:
#         print(columna)
        
# creacion arrays, metodo matrices
matriz = np.array([[0, 1, 2], [4, 5, 6]])
#print(matriz)
# for fila in matriz:
#     for columna in fila:
#         print(columna)
        
# for i in range(2):
#     for j in range(3):
#         print(matriz[i][j])

#ejercicios
#01
arreglo = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(3):
    for j in range(3):
        arreglo[i][j] = np.random.randint(0, 100)    

matriz2 = np.array(arreglo)
# print(matriz2)
for i in matriz2:
    print(i)

#02
# Utilice las siguientes funciones en el arreglo creado en el punto 1
# Promedio de los elementos.
# Suma de los elementos.
# Mostrar el elemento mayor.
# Mostrar el elemento menor.
# Mostrar sólo los elementos de la diagonal principal.
