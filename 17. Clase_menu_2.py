import time
import os

sw = True
while sw:
    os.system("cls")
    print("1. opción 1")
    print("2. opción 2")
    print("3. opción 3")
    print("4. Salir")
    try:
        op = int(input("Seleccione opción\n"))
        if (op > 0 and op < 5):
            if (op == 1):
                print("Hola 1")
            elif (op == 2):
                print("Hola 2")
            elif (op == 3):
                print("Hola 3")
            elif (op == 4):
                print("Chau")
                sw = False
        else:
            print("Opción no existe")
    except ValueError:
        print("opcion ingresada no es válida")
        time.sleep(2)
