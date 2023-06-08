print("En este programa se le mostrará la tabla de multiplicar del 1 al 10 de un número ingresado por usted")
num = -1
res = 0

while num < 0:
    num = int(input("Ingrese un número positivo:\n"))
    print("\n")
    if num >= 0:
        x = range(1, 11)
        for i in x:
            res = num * i
            print(f"{i} * {num} = {res}")
    else:
        print("El número ingresado es negativo, por favor ingrese un número positivo")

print("\n")
