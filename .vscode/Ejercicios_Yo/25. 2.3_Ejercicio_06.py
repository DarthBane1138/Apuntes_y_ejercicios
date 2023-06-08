# Genere las tablas de multiplicar de los primeros números pares entre 1 y 10.

res = 0

for i in range(2, 11, 2):
    for x in range(1, 11):
        if i % 2 == 0:
            res = i * x
            print(f"{x} * {i} = {res}")
