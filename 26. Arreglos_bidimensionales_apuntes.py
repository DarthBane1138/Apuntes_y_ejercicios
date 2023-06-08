import numpy as np

# Usando método tradicional
matriz = np.array([[0, 1, 2], [3, 4, 5]])
for f in range(2):  # La matriz tiene dos filas
    for c in range(3):  # La matriz tiene dos columnas
        print(matriz[f][c])
print(matriz)

# Usando listas
lista = [[1, 2, 3], [4, 5, 6]]
matriz1 = np.array(lista)
print(matriz1)

# Operaciones con un arreglo de dos dimensiones (matriz)

# Caso 1
matriz2 = np.array([[0, 1, 2], [3, 4, 5]])
for f in range(2):
    for c in range(3):
        print(matriz[f][c])
print("")
print(matriz)
# En este caso se está pidiendo un número de acuerdo a sus coordenadas en la matriz
print(matriz2[1, 1])

# Caso 2
print("")
lista1 = [[1, 2, 3], [4, 5, 6]]
matriz3 = np.array(lista1)
print(matriz3)
# Mismo caso que anteriormente, con la diferencia es que primero se crea una lista, y a partir de esta lista se convierte a una matriz
print(matriz3[0][1])

# Si tenemos una matriz dad
print("")
lista2 = [[1, 2, 3], [4, 5, 6]]
matriz3 = np.array(lista2)
print(matriz3[1, 1])
# Se imprime el elemento de la segunda fila, y de la segunda columna
print(matriz3[:, 2])
# Imprime todos los elementos de la tercera columna (índice 2) de la matriz. El operador ":" indica que se debe seleccionar todos los elementos de la dimensión correspondiente, es decir, todas las filas
print(matriz3[0, :])
# Imprime todos los elementos de la primera fila (índice 0) de la matriz. El operador ":" en este caso indica que queremos selsciconar todos los elementos en la dimensión correspondiente, es decir, todas las columnas.
print(matriz3[0, ::-1])
# Imprime todos los elementos de la primera fila (índice 0) de la matriz en orden inverso. El operador "::-1" se utiliza para invertir el orden de los elementos en la dimentsión correspondiente. En este caso, se imprimirá 3, 2, 1

# Operaciones con un arreglo de dos dimensiones (matriz)
# Generar matriz con ceros de 3 x 3
matriz3 = np.zeros((3, 3))
print(matriz3)
# Generar matriz con unos
matriz4 = np.ones((3, 3))
print(matriz4)
# Generar matriz con diagonal principal con 1
matriz5 = np.diag([1, 1, 1])
print(matriz5)
# Sumar todos los elementos
print("")
lista3 = [[1, 2, 3], [4, 5, 6]]
matriz6 = np.array(lista3)
print(matriz6.sum())
# Sumar elementos por fila
print("")
lista4 = [[1, 2, 3], [4, 5, 6]]
matriz7 = np.array(lista4)
print("Sumna elementos fila 0: ", matriz7[0, :].sum())
print("Sumna elementos fila 1: ", matriz7[1, :].sum())
