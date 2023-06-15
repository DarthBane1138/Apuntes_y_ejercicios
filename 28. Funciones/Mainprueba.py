from Mainprueba import *

menu = True

while menu:
    try:
        opcion = int(input("Ingrese una opción:\n"))
        if opcion > 0 and opcion < 4:
            if opcion == 1:
                print("Agregar Afiliado")
            elif opcion == 2:
                print("Busacar Afiliado")
            elif opcion == 3:
                print("Listar")
            elif opcion == 4:
                op = int(print("¿Está seguro que desea salir?\n 1. Sí\n 2. No\n"))
                if op == 1:
                    menu = False
    except:
        print("Opción invalida")