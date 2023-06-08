import numpy

# Para declarar un arreglo, lo podemos hacer a través de una lista o con datos directamente.
# 1. A través de una lista
lista = [1, 2, 3, 4, 5]
print(type(lista))
print(lista)
# Cuando se ejecuta la línea "Type(lista)", se obtiene como resultado la clase "list", que indica que "lista" es un objeto de tipo lista en python
# 1.1
a = numpy.array(lista)
print(type(lista))
# Para crear un arreglo o un vector en Python usamos la función array() de la biblioteca Numpy.
# Existen dos formas de utilizarla
# Import numpy
# arreglo = numpy.array([1, 3, 5, 7])
# print(type(arreglo))
# print(arreglo)
#
# import numpy as np
# arreglo = np.array([1, 2, 3, 4])
# print(type(arreglo))
# print(arreglo)

arreglo = a
# Dada la variable arreglo, Realizaremos algunas operaciones con funciones
# 1. Acá se imprime "1" debido a que es un arreglo de solo una dimesión
print("Una dimesión")
print(arreglo.ndim)
# Este método, es un método dentro de numpy para obtener la cantidad de diensiones de un arreglo
# Algunos ejemplos de más dimensiones son
print("Dos dimesiones")
arreglo_2d = numpy.array([[1, 2, 3], [4, 5, 6]])
print(arreglo_2d.ndim)  # Salida: 2
print("Tres dimesiones")
arreglo_3d = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arreglo_3d.ndim)  # Salida: 3
# 2. La función len en Python se utiliza para obtener la longitud o cantidad de elementos de un objeto iterable, como una lista
# una cadena de texto, una tupla, un diccionario, etc. Devuelve un número entero que representa la cantidad de elementos en el objeto
longitud = len(lista)
print(longitud)
# O bien
print(len(lista))
# 3. La función shape es un atributo utilizado en numpy para obtener las dimensiones de un arreglo. Devuelve una tupla que representa las dimensiones del arreglo en términos de filas y columnas
# En caso de ser multidimensionales, también incluye las dimensiones adicionales.
# Para una dimensión
arreglo_1d = numpy.array([1, 2, 3, 4, 5])
print(arreglo_1d.shape)  # Salida: (5,)
# Para dos dimensiones
arreglo_2d = numpy.array([[1, 2, 3], [4, 5, 6]])
# Salida: (2, 3), tiene dos dimensiones con 2 filas y 3 columnas.
print(arreglo_2d.shape)
# Para tres dimensiones
arreglo_3d = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# Salida: (2, 2, 2), tiene tres dimesiones con 2 bloques, cada uno con 2 filas y dos columnas
print(arreglo_3d.shape)
# La palabra "array" se utiliza para referirse a una estructura de datos que almacena un conjunto de elementos del mismo tipo en una secuencia contigua en la memoria. En esencia, un array es una colección
# ordenada de elementos que se acceden mediante un índice.
# Si hacemos un slice
arreglo1 = arreglo[1:3]
print(arreglo1)  # Me los muestra sin coma
# Esta forma tiene el orden [inicio:fin:paso] en este caso solo se imprime el 2 por que el índice 3 (número 4) no se incluirá
arreglo2 = arreglo[1:3:2]
print(arreglo2)
# Otro ejemplo con la sintaxis slice:
arreglo2 = arreglo[::2]
# Al omitir los valores de "inicio" y "fin", dejando solo "paso", se seleccionarán todos los elementos del arreglo. Por defecto parte en el primer elemento y terminará en el último elemento avanzando de 2 en 2
print(arreglo2)
# Si se utilizan números negativos se retrocederá la cantidad corespondiente al número negativo desde la última posición
print(arreglo[-2])  # Imprimirá 4, es decir el penúltimo número
# Si usamos la siguiente función
c = [i for i in range(0, 5)]
print(c)  # Se imprimirá [0, 1, 2, 3, 4]
# Se genera un rango de números de 0 a 4 excluyendo al número 5 con un paso de 1
# Para mostrar los elementos del arreglo, utilizando for
for i in range(len(arreglo)):
    print(arreglo[i])
# En este bucle for se recorrenrán los elementos de la lista "arreglo". La función "range(len(arreglo))" crea un rango de valores desde 0 hasta la longitud del arreglo.
# El bucle se ejecutará una vez para cada valor en el rango, y en cada iteración, el valor actual se almacenará en la variable "i"
# Dentro del bucle, se utiliza la variable "i" para acceder a cada elemento de la lista "arreglo" mediante el índice "i"
