# Ingrese 3 números enteros por teclado e indique ¿cuántos son menores a cero?

x = range(3)
menor0 = 0
igual0 = 0
mayor0 = 0

print("\n")
print("En este programa ingresarás 3 números enteros y te diremos cuantos son menores a 0")

for i in x:
    i = int(input("Ingrese el primer número:\n"))
    if i > 0:
        mayor0 = mayor0 + 1
    elif i < 0:
        menor0 = menor0 + 1
    else:
        igual0 = igual0 + 1

print(f"Hay {menor0} números menores a 0")
