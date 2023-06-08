import os
os.system("cls")
suma = 0
i = 0

while i < 5:
    num = int(input("Ingrese número:\n"))
    if num > 0:
        suma = suma + num
        i = i + 1
    else:
        while num <= 0:
            num = int(input("Ingrese numero mayor a 0:\n"))
            if num > 0:
                suma = suma + num
                i = i + 1
print(f"La suma de los 5 números es {suma}")