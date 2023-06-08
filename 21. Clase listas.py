# Para trabajar con listas es necesario declararla o inicializarla
lista_numeros = [7, 2, 9]
lista_cadenas =["Hola", "como", "estás"]
print(lista_numeros)
print(lista_cadenas)

numero1 = 10
numero2 = int(input("Ingrese un valor"))
# Para agregar elementos a una lista usaremos append
lista_numeros.append(numero1)
lista_numeros.append(numero2)
print(lista_numeros)

#Se puede declarar la posición específica en una lista para imprimir un valorn en particular
print(lista_numeros[2])

# Si escribimos -1 entre el corchete imprimirá el último número agregado a la lista, -2 el penúltimo y así sucesivamente

# Si llevo una lista a otra con extend la lista se integrará ala lista con corchetes, en cambio con append se integrará sin corchetes.

lista_numeros.insert(2, 3)
print(lista_numeros)

# remove es para borrar elementos de la lista, esta función elimina el valor indicado
lista_numeros.remove()

#Para eliminar con "pop" debe recordar que eliminará desde el

# Para recorrer una lista
for i in lista_numeros:
    print(i)