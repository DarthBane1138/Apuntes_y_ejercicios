a = [12, "Python", 3.1416]

print(a[0])  # 12        Se imprime elemento 1 que está en la posición 0
print(a[1])  # Python    Se imprime elemento 2 que está en la posición 1
print(a[2])  # 3.1416    Se imprime elemento 3 que está en la posición 2
print("\n")
b = [90, "Python", 3.87]
print(b[-1])  # Con el -1 se imprimirá el último elemento de la lista
# Con el -2 se imprimirá el penúltimo elemento de la lista y así sucesivamente
print(b[-2])
print("\n")

lista = [1, 2]
print(lista)
lista.append(3)  # La función append agregará un elemento al final de la lista
print(lista)  # [1, 2, 3]

print("\n")
lista2 = [1, 2]
print(lista2)
# El método extend(), permite añadir una lista a una lista inicial
lista2.extend([3, 4])
print(lista2)  # [1, 2, 3, 4]

print("\n")
lista3 = [1, 3]
print(lista3)
# El método insert permite añadir un elemento en una posición determinada
# El parénsesis determina la posición, en este caso, en la posición 1, se agrega un número 2.
lista3.insert(1, 2)
print(lista3)

print("")
lista4 = [1, 2, 3]
print(lista3)
# El método remove(), permite recibir como argumento un objeto y lo borra de la lista
lista4.remove(3)  # La función buscará el elemento escrito para borrarlo
print(lista4)

print("")
lista5 = [1, 2, 3]
print(lista5)
# El método pop(), elimina el último elemento de la lista, o bien el que se indique entre paréntesis según el índice (posición)
lista5.pop()
print(lista5)  # [1, 2]

print("")
lista6 = [1, 2, 3]
print(lista6)
lista6.reverse()  # El método reverse(), permite invertir el orden de la lista, el paréntesis no acepta argumentos dentro del paréntesis
print(lista6)  # [3, 2, 1]

print("")
lista7 = [1, 2, 3, 4, 5, 6, 7]
print(lista7)
# la funcipon reversed es una alternativa a la función reverse, esta a diferencia de la función reverse() no modifica la ista original
# sino que devuelve un nuevo objeto iterable que puedes convertir en una lista utilizando la función list()
reversed_list = list(reversed(lista7))
print(reversed_list)

print("")
lista7 = [3, 1, 2]
print(lista7)
# El método sort (), permite ordenar los elementos de menor a mayor.
lista7.sort()
print(lista7)  # [1, 2, 3]
print("")
lista8 = ["Patricio", "Manuel", "Eduardo"]
print(lista8)
# El método sort() también puede ordenar strings por orden alfabético
lista8.sort()
print(lista8)
# Hay ciertas variaciones que se pueden realizar con el método sort()
# se puede utilizar con reverse que funciona como argumento booleano.
# Por defecto, su valor es "False" y el ordenamiento se realiza en orden ASCENDENTE
# Si se establece en "True", el ordenamiento se realizará en orden descendente
lista9 = [3, 1, 4, 2]
print(lista9)
lista9.sort(reverse=False)
print(lista9)
lista9.sort(reverse=True)
print(lista9)
# Por otro lado el argumento "Key" permite especificar una función de clave de ordenammiento personalizada.
# Esta función se usa para calcular el valor clave para cada elento de la lista y se utiliza para comparar y ordenar los elementos en función de los valores clave calculados.
# La función de clave debe aceptar un elemento de la lista como argumento y devolver un valor que se utilizará para la comparación.
print("")
lista10 = ("Banana", "Apple", "Cherry", "Date")
print(lista10)
lista10 = list(lista10)
lista10.sort(key=len)
print(lista10)
