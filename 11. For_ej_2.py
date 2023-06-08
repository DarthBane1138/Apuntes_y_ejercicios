x = range(10)
consonantes = 0
vocales = 0

for i in x:
    i = input("ingrese una letra\n")
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1
        
print (f"El número de vocales son: {vocales}")
print (f"El número de consonantes son: {consonantes}")

# En el rango se define cuantas veces se me va a pedir una letra, de acuerdo a esto y a los valores estándares se me pedirá una letra 5 veces (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)