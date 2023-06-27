import os


def mostrar_menu():
    print("""
    ---------- Menú ----------
1. Espresso ------------------> $1.500 
2. Capuchino -----------------> $1.800 
3. Latte ---------------------> $1.600 
4. Moca ----------------------> $1.700
5. Terminar con la compra
6. Cancelar la compra""")


def compra_cafe(opcion, contador, cantidad_espresso, cantidad_capuchino, cantidad_latte, cantidad_moca):
    while opcion != 5:
        os.system("cls")
        mostrar_menu()
        print(f"   Subtotal ----------> {contador}$")
        try:
            opcion = int(input("Seleccione la opción que desee;\n"))
            if opcion == 1:
                print("Ha selecconado la opción espresso por 1.500$ c/u")
                cantidad = int(
                    input("Ingrese la cantidad de productos que desesa:\n"))
                cantidad_espresso = cantidad_espresso + cantidad
                contador = contador + cantidad * 1500
                print(
                    f"Ha saleccionado {cantidad} café espresso por {cantidad * 1500}$")
                presione()
            elif opcion == 2:
                print("Ha selecconado la opción Capuchino por 1.800$ c/u")
                cantidad = int(
                    input("Ingrese la cantidad de productos que desesa:\n"))
                cantidad_capuchino = cantidad_capuchino + cantidad
                contador = contador + cantidad * 1800
                print(
                    f"Ha saleccionado {cantidad} café Capuchino por {cantidad * 1800}$")
                presione()
            elif opcion == 3:
                print("Ha selecconado la opción Latte por 1.600$ c/u")
                cantidad = int(
                    input("Ingrese la cantidad de productos que desesa:\n"))
                cantidad_latte = cantidad_latte + cantidad
                contador = contador + cantidad * 1600
                print(
                    f"Ha saleccionado {cantidad} café espresso por {cantidad * 1600}$")
                presione()
            elif opcion == 4:
                print("Ha selecconado la opción Moca por 1.700$ c/u")
                cantidad = int(
                    input("Ingrese la cantidad de productos que desesa:\n"))
                cantidad_moca = cantidad_moca + cantidad
                contador = contador + cantidad * 1700
                print(
                    f"Ha saleccionado {cantidad} café espresso por {cantidad * 1700}$")
                presione()
            elif opcion == 5:
                os.system("cls")
                print("Ha seleccionado terminar con la compra")
                print(f"El subtotal de su compra es de ${contador}")
                presione()
                return contador, cantidad_espresso, cantidad_capuchino, cantidad_latte, cantidad_moca
            elif opcion == 6:
                print("Ha seleccionado la opcion cancelar la compra")
                confirmar = input(
                    "¿Está seguro que desea cancelar? S = Sí   N = No \n")
                confirmar = confirmar.lower()
                if confirmar == "s":
                    contador = 0
                    cantidad_espresso = 0
                    cantidad_capuchino = 0
                    cantidad_latte = 0
                    cantidad_moca = 0
                    presione()
                elif confirmar == "n":
                    presione()
                else:
                    print("La opción seleccionada no es válida, volviendo al menú")
                    presione()
            else:
                print("La opcion seleccionada no está disponible")
                presione()
        except ValueError:
            print("La opción ingresada no es válida")
            presione()


def presione():
    input("Presiona enter para continuar...")


def descuento(contador):
    if contador >= 3000:
        print(
            f"Su compra por un total de ${contador} es igual o superior a 3000$, se ha aplicado un descuento del 10%")
        contador = contador * 0.9
        contador = int(contador)
        print(f"Quedando en ${contador}")
        presione()
        return contador
    else:
        print(f"No se ha aplicado ningún descuento, el total es {contador}")


def imprimir_boleta(contador, cantidad_espresso, cantidad_capuchino, cantidad_latte, cantidad_moca):
    print(" ---------- boleta ----------")
    print(
        f"Cantidad de Espresso ----------> {cantidad_espresso} unidades ----------> ${cantidad_espresso * 1500}")
    print(
        f"Cantidad de Capuchino ---------> {cantidad_capuchino} unidades ----------> ${cantidad_capuchino * 1800}")
    print(
        f"Cantidad de Latte -------------> {cantidad_latte} unidades ----------> ${cantidad_latte * 1600}")
    print(
        f"Cantidad de Moca --------------> {cantidad_moca} unidades -----------> ${cantidad_moca * 1700}")
    print(
        f"Subtotal de compra ${(cantidad_espresso * 1500) + (cantidad_capuchino * 1800) + (cantidad_latte * 1600) + (cantidad_moca * 1700)}")
    descuentos = ((cantidad_espresso * 1500) + (cantidad_capuchino * 1800) +
                  (cantidad_latte * 1600) + (cantidad_moca * 1700)) - contador
    print(f"Total descuentos ----------> ${descuentos}")
    print(f"Total a pagar -------------> ${contador}")
