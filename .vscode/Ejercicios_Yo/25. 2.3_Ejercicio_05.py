# Genere las 10 primeras tablas de multiplicar, cada una de ellas de 1 a 10.

num = int(input("Ingrese un número para realizar su tabla de multiplicar:\n"))
res = 0

print("\n")
for i in range(1, 11):
    res = i * num
    print(f"{i} * {num} = {res}")
