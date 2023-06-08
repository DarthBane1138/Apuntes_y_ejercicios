y = range(0, 100, 1)
for i in y:
    if i %2 == 0:
        print(f"{i} es un número par")
    else:
        print (f"{i} es un número impar")
        
# if i %2 == 0 significa que i se divide por 2, y se conserva el modulo, si el modulo (resultado de esta operación después de la coma) es igual a 0, entoces el número es par
# En caso contrario, por ejemplo el 3, la división da 1,5, por lo tanto no se cumple y la condición cae en else.