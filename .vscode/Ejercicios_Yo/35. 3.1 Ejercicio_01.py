# Investiga con tus compañeros sobre otras operaciones con las listas, por ejemplo:

# Tamaño de la lista.
# Copiar una lista.
# Borrar los elementos de la lista.
# Contar un elemento x de la lista

# Expone a tus compañeros y docente.

# Para el tamaño de una lista se ocupa la función "len", esta devuelve la cantidad de elementos que hay en una lista
print("Función \"len\"")
lista1 = [1, 2, 3, 4, 5]
tamaño = len(lista1)
print(tamaño)

# Para copiar una lista existen enfoques distintos
# 1. Slicing (rebanado), se puede ocupar el método slicing para crear una copia de la lista original.
print("Método \"slicing\"")
lista_original = [1, 2, 3, 4, 5]
print(lista_original)
lista_copia = lista_original[:]
print(lista_copia)
# Acá lista "lista_original[:]" crea una nueva lista que contiene todos los elemtentos de "lista_original".
# Asignarla a "Lista_copia crea una copia independiente de la lista original"
# 2. El constructor list(), Puedes utilizar el constructor "list()" para crear una nueva lista a partir de la lista original
print("Constructor \"list()\"")
lista_copia2 = list(lista_original)
print(lista_copia2)
# Al pasar "lista_original como argumento para "list(), se crea una nueva lista con los mismos elementos que la lista original"
# 3. El método copy()
print("Método \"copy\"")
lista_copia3 = lista_original.copy()
print(lista_copia3)
# Al llamar al método "copy()" en la lista original, se crea una copia independiente de la lista.

# Para borrar elementos de una lista existen varios métodos además de los tradicionales remove() y pop()
# 1. La sentencia "del", esta se usa seguida del índice del elemento que deseas eliminar.
print("Sentencia \"del\"")
lista2 = [1, 2, 3, 4, 5]
print(lista2)
del lista2[2]  # Elimina el elemento en el índice 2 (el valor 3)
print(lista2)
# 2. Método "pop()", que permite eliminar un elemento de la lista utilizando su índice y, al mismo tiempo, devuelve el valor eliminado
print("Método pop()")
lista3 = [1, 2, 3, 4, 5]
# Elimina y devuelve el elemento en el índice 2 (valor 3)
elemento_eliminado = lista3.pop(2)
print(elemento_eliminado)  # Imprime el valor eliminado (3)
# 3. método "remove()", este permite eliminar un elemento específico de la lista por su valor.
print("Método remove")
lista4 = [1, 2, 3, 4, 5]
print(lista4)
lista4.remove(3)  # Elimina el elemento con valor 3
print(lista4)

# Para contar la cantidad de veces que aparece un elemento específico en una lista en Python, se puede utilizar el método "count()"
# El método "count()" devuelve el número de ocurrencias del elemento dentro de la lista
print("Como contar elementos en una lista")
lista5 = [1, 2, 2, 3, 4, 5, 2, 6, 2]
contador = lista5.count(2)
print(contador)
# En este caso "lista5.count(2)" se devuelve el valor 4 debido a que el número 2 aparece 4 veces.
# Si este elemento no se encuentra en la lista, el print() te devolverá el valor 0
