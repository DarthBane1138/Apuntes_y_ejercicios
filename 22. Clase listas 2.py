#para trabajar con listas es necesario declararla o instanciarla

lista_cadenas = ["hola", "como", "estas"]

# print(lista_cadenas)


#para agregar elementos a una lista usaremos 'append'
# numero1 = 10
# numero2 = int(input("ingrese un valor"))
lista_numeros = [7, 2, 9]
lista2 = [10, 5, 30, -2]
lista3 = [4, -2, 3]
#lista_numeros.append(lista3)
#si utiliza 'extend', recuerde que la lista que agregue 
# sera independiente de la lista original
lista_numeros.extend(lista2)

#para el 'insert' es necesario 2args el 1ero es la posicion y el 2do es el valor
lista_numeros.insert(2, 3)

#para eliminar con 'remove' debe recordar que eliminará desde EL VALOR
lista_numeros.remove(-2)

#para eliminar con 'pop' debe recordar que eliminará desde EL VALOR
#si no le entrega argumento a este metodo, automaticamente eliminara el
#ultimo elemento de la lista
lista_numeros.pop(4)
print(lista_numeros)

#este metodo nos permite invertir el orden de los elementos que existen en la lista
lista_numeros.reverse()
print(lista_numeros)

#para ordenar de manera ascendente 
#lista_numeros.sort()
print(lista_numeros)

#para ordenar de manera descendente 
#lista_numeros.sort(reverse = True)
print(lista_numeros)

#para recorrer una lista
# for i in lista_numeros:
#     print(i)
    
#tamaño de lista
print(len(lista_numeros))

#copiar la lista
lista_numeros.copy()
print(lista_numeros)

#borrar todos los elementos de una lista
    # lista_numeros.clear()
    # print(lista_numeros)

