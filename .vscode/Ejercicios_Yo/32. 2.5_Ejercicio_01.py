sw = 1
while sw == 1:
    print("1. Opción  1, numeros pares")
    print("2. Opción  2, serie Fibonacci")
    print("3. Salir")
    try:
        op = int(input("Seleccione una opción:\n"))
        if op > 0 and op < 4:
            if op == 1:
                print("Ha seleccionado la opción 1. números pares")
                num = 1.1
                while num % 1 != 0:
                    try:
                        num = int(input("Ingrese un número entero:\n"))
                        if num % 2 == 0:
                            print("Es un número par")
                        else:
                            print("Es un número impar")
                    except ValueError:
                        print("No ha ingresado un número entero")
                continu = int(input("Desea salir 1 = Sí 2 = No:\n"))
                if continu == 1:
                    print("Adiós")
                    sw = 0
            elif op == 2:
                print("Ha seleccionado la opción 2, serie Fibonacci")
                i = 0
                a = 0
                b = 1
                print(f"{a}")
                print(f"{b}")
                for i in range(1, 9):
                    c = a + b
                    print(f"{c}")
                    a = b
                    b = c
                continu = int(input("Desea salir 1 = Sí 2 = No:\n"))
                if continu == 1:
                    print("Adiós")
                    sw = 0
            elif op == 3:
                print("Ha seleccionado la opción de 3 para salir del menú")
                sw = 0
        else:
            print("Ha seleccionado un número de opción no válida")
    except ValueError:
        print("Por favor, solo ingrese números enteros")
