# En un delivery se venden 4 tipos de pan: 
# Amasado $1.500
# Molde $1.000
# Baguette $2.000
# Integral $3.000

# Determine el total a pagar por un cliente, el cual puede comprar diferentes tipos y cantidad de pan.
# Si el total de la venta es superior a $5000 el envío es gratis, sino se cobra el 10% adicional.
# Muestre los mensajes correspondientes.

import os
menu = """Bienvenido a delivery PanTástico, nuestras variedades de pan son las siguientes
1. Pan Amasado ----------> $ 1500
2. Pan de Molde ---------> $ 1000
3. Baguette -------------> $ 2000
4. Pan Integral ---------> $ 3000
5. Terminar compra --------------
6. Cancelar compra --------------"""
subtotal = 0
cant1 = 0
cant2 = 0
cant3 = 0
cant4 = 0
subtotal1 = 0
subtotal2 = 0
subtotal3 = 0
subtotal4 = 0
opcion = 1

while opcion != 5 and opcion != 6:
    try:
        os.system("cls")
        print(f"{menu}")
        subtotal = subtotal1 + subtotal2 + subtotal3 + subtotal4
        print(f"Subtotal hasta el momento: ${subtotal}")
        opcion = int(input("Seleccione el número de la opción que desea:\n"))
        if opcion == 1:
            pan = 1500
            print("Ha seleccionado la opción 1. Pan Amasado - $1500 c/u")
            try:
                cant1 = int(input("¿Cuantas unidades desea?\n"))
            except ValueError:
                print("Valor ingresado no válido")
            subtotal1 = subtotal + (pan * cant1)
            print(f"Subtotal compra: ${subtotal1}")
            input("Presione cualquier tecla para continuar")
        elif opcion == 2:
            pan = 1000
            print("Ha seleccionado la opción 2. Pan de Molde - $1000 c/u")
            try:
                cant2 = int(input("¿Cuantas unidades desea?\n"))
            except ValueError:
                print("Valor ingresado no válido")
            subtotal2 = subtotal + (pan * cant2)
            print(f"Subtotal compra: ${subtotal2}")
            input("Presione cualquier tecla para continuar")
        elif opcion == 3:
            pan = 2000
            print("Ha seleccionado la opción 3. Baguette - $2000 c/u")
            try:
                cant3 = int(input("¿Cuantas unidades desea?\n"))
            except ValueError:
                print("Valor ingresado no válido")
            subtotal3 = subtotal + (pan * cant3)
            print(f"Subtotal compra: ${subtotal3}")
            input("Presione cualquier tecla para continuar")
        elif opcion == 4:
            pan = 3000
            print("Ha seleccionado la opción 4. Pan Integral - $3000 c/u")
            try:
                cant4 = int(input("¿Cuantas unidades desea?\n"))
            except ValueError:
                print("Valor ingresado no válido")
            subtotal4 = subtotal + (pan * cant4)
            print(f"Subtotal compra: ${subtotal4}")
            input("Presione cualquier tecla para continuar")
        elif opcion == 5:
            print("Ha terminado su compra")
            input("Presione cualquier tecla para continuar")
        elif opcion == 6:
            print("Ha cancelado la compra")
            subtotal = 0
            break
        else:
            print("Ha seleccionado una opción no válida")
            input("Presione cualquier tecla para continuar")
    except ValueError:
        print("Ha ingresado un valor no válido")

if subtotal > 5000:
    envio = 1
    enviop = "Gratis"
else:
    envio = 1.1
    enviop = "10% de la compra"

total = subtotal * envio
envio = total - subtotal
envio = int(envio)
total = int(total)

if opcion == 5 and total > 0:
    os.system("cls")
    print("El detale de su boleta es el siguiente")
    if cant1 > 0:
        print(f"Pan Amasado ----- {cant1} unidades ----- ${subtotal1}")
    if cant2 > 0:
        print(f"Pan de Molde ---- {cant2} unidades ----- ${subtotal2}")
    if cant3 > 0:
        print(f"Baguette -------- {cant3} unidades ----- ${subtotal3}")
    if cant4 > 0:
        print(f"Pan Integral ---- {cant4} unidades ----- ${subtotal4}")
    print("-------------------------------------------------------")
    print(f"Subtotal de la compra ------------> ${subtotal}")
    print(f"Envio-----------------------------> {enviop}")
    print(f"Costo de envío -------------------> ${envio}")
    print(f"Total de la compra ---------------> ${total}")
else:
    os.system("cls")
    print("Vuelva pronto, pero pa la otra compre")
