# En este programita deberemos hacer un menú para una ISAPRE, en este menú tendremos que tener las siguientes características
# 1. Agregar afiliado
# 2. Buscar afiliado por número de rut
# 3. La posibilidad de listar afiliados segun estado civil solteros
# 4. Salir del menú y cerrar el programa
# Además se deberá comprobar que el rut del usuario ingresado no se repita y comprobar si el dígito verificador es correcto

import os
from Funciones_08 import *


menu = True

while menu:
    os.system("cls")
    menus()
    try:
        opcion = int(input("Por favor seleccione una opción disponible:\n"))
        if opcion == 1:
            agregar_afiliado()
        elif opcion == 2:
            buscar_afiliado()
        elif opcion == 3:
            estado_civil()
        elif opcion == 4:
            mostrar_todo()
        elif opcion == 5:
            op = 5
            while op != 1 and op != 2:
                print("Ha selecionado la opción salir")
                op = int(input("¿Está seguro que desea salir?\n1. Sí \n2. No\n"))
                if op == 1:
                    print("Salida confirmada. Adiós")
                    menu = False
                elif op == 2:
                    print("Regresando al menú de selección")
                    input("Presione enter para continuar...")
                else:
                    print("La opción seleccionada no es válida")

        else:
            print("La opción ingresada no está disponible")
    except ValueError:
        print("La opción ingresada no es válida")
