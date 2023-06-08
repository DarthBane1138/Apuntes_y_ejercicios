# En un local de hamburguesas se venden 6 tipos de hamburguesas: 
# Italiana $5000
# 4 Quesos $6000
# Ecuatoriana $6500
# Vegana $4000
# A lo pobre $6500
# Loussiana $7000

# Además venden 4 tipos de bebidas
# Coca-cola $1500
# Té helado $1200
# Jugo natural $1600
# Cerveza #2000

# Determine el total a pagar por un cliente, el cual puede comprar diferentes tipos y cantidad de Hamburguesas y bebestibles.
# Pregunte si es retiro o delivery, el retiro es gratis, el delivery tiene un costo de $2000
# Si el cliente es socio se le hará un descuento diferenciado de un 20% al total de hamburguesas y un 10% en las bebidas
# Además, si se lleva un total mayor a $100000 después de los descuentos anteriores, se le hace un 10% de descuento en el último precio
# Muestre los mensajes correspondientes.

import os

menup = """Bienvenido a Hamburguesas TapaArterias, nuestras opciones son
1. Menú de Hamburguesas
2. Menú de bebidas
3. Finalizar compra
4. Cancelar compra"""

menuh = """Nuestras hamburhuesas son:
1. Italiana ---------------> $5000
2. 4 Quesos ---------------> $6000
3. Ecuatoriana ------------> $6500
4. Vegana -----------------> $4000
5. A lo pobre -------------> $6500
6. Louissiana -------------> $7000
7. Volver al menu principal
8. Cancelar Selección"""

menub = """Nuestras bebidas disponibles son:
1. Coca-cola --------------> $1500
2. Té helado --------------> $1200
3. Jugo natural -----------> $1600
4. Cerveza ----------------> $2000
5. Volver al menú principal
6. Cancelar Selección"""

presione = "Presione Enter para continuar"

opp = 0
oph = 0
opb = 0
conth1 = 0
conth2 = 0
conth3 = 0
conth4 = 0
conth5 = 0
conth6 = 0
contb1 = 0
contb2 = 0
contb3 = 0
contb4 = 0
subh = 0
subb = 0
subt = 0
conth1t = 0
conth2t = 0
conth3t = 0
conth4t = 0
conth5t = 0
conth6t = 0
contb1t = 0
contb2t = 0
contb3t = 0
contb4t = 0


while opp != 3 and opp != 4:
    oph = 0
    opb = 0
    os.system("cls")
    print(f"{menup}")
    print(f"Subtotal Haburguesas -----> ${subh}")
    print(f"Subtotal Bebidas ---------> ${subb}")
    try:
        opp = int(
            input("Escriba el número correspondiente a la opción que desea:\n"))
        if opp == 1:
            os.system("cls")
            print("Ha seleccionado el menú de hamburguesas")
            while oph != 7 and oph != 8:
                subh = conth1t + conth2t + conth3t + conth4t + conth5t + conth6t
                try:
                    os.system("cls")
                    print(f"{menuh}")
                    print(f"Subtotal Haburguesas -----> ${subh}")
                    print(f"Subtotal Bebidas ---------> ${subb}")
                    oph = int(
                        input("Escriba el número correspondiente a la opción que desea:\n"))
                    if oph == 1:
                        oph = "Italiana"
                        print("Ha seleccionado Hamburguesa Italiana por $5000")
                        try:
                            canth1 = int(input("¿Cuantas unidades desea?\n"))
                            conth1 = 5000 * canth1
                            conth1t = conth1t + conth1
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {canth1} Hamburguesas {oph} por un total de ${conth1}")
                        input(f"{presione}")
                    elif oph == 2:
                        oph = "4 Quesos"
                        print("Ha seleccionado Hamburguesa 4 Quesos por $6000")
                        try:
                            canth2 = int(input("¿Cuantas unidades desea?\n"))
                            conth2 = 6000 * canth2
                            conth2t = conth2t + conth2
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {canth2} Hamburguesas {oph} por un total de ${conth2}")
                        input(f"{presione}")
                    elif oph == 3:
                        oph = "Ecuatoriana"
                        print("Ha seleccionado Hamburguesa Ecuatoriana por $6500")
                        try:
                            canth3 = int(input("¿Cuantas unidades desea?\n"))
                            conth3 = 6500 * canth3
                            conth3t = conth3t + conth3
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {canth3} Hamburguesas {oph} por un total de ${conth3}")
                        input(f"{presione}")
                    elif oph == 4:
                        oph = "Vegana"
                        print("Ha seleccionado Hamburguesa Vegana por $4000")
                        try:
                            canth4 = int(input("¿Cuantas unidades desea?\n"))
                            conth4 = 4000 * canth4
                            conth4t = conth4t + conth4
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {canth4} Hamburguesas {oph} por un total de ${conth4}")
                        input(f"{presione}")
                    elif oph == 5:
                        oph = "A lo Pobre"
                        print("Ha seleccionado Hamburguesa A lo Pobre por $6500")
                        try:
                            canth5 = int(input("¿Cuantas unidades desea?\n"))
                            conth5 = 6500 * canth5
                            conth5t = conth5t + conth5
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {canth5} Hamburguesas {oph} por un total de ${conth5}")
                        input(f"{presione}")
                    elif oph == 6:
                        oph = "Louissiana"
                        print("Ha seleccionado Hamburguesa Louissiana por $7000")
                        try:
                            canth6 = int(input("¿Cuantas unidades desea?\n"))
                            conth6 = 7000 * canth6
                            conth6t = conth6t + conth6
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {canth6} Hamburguesas {oph} por un total de ${conth6}")
                        input(f"{presione}")
                    elif oph == 7:
                        print("Ha seleccionado la opción Volver al Menú Principal")
                        input(f"{presione}")
                    elif oph == 8:
                        print(
                            "Ha seleccionado la opción Cancelar compra Hamburguesas")
                        subh = 0
                        input(f"{presione}")
                    else:
                        print("La opción elegida no existe")
                        input("Presione Enter par continuar")
                except ValueError:
                    print("Ha seleccionado una opción no valida")
                    input(f"{presione}")
        elif opp == 2:
            while opb != 5 and opb != 6:
                subb = contb1t + contb2t + contb3t + contb4t
                try:
                    os.system("cls")
                    print("Ha seleccionado el menú de bebidas")
                    print(f"{menub}")
                    print(f"Subtotal Haburguesas -----> ${subh}")
                    print(f"Subtotal Bebidas ---------> ${subb}")
                    opb = int(
                        input("Escriba el número correspondiente a la opción que desea:\n"))
                    if opb == 1:
                        opb = "Coca-Cola"
                        print("Ha seleccionado Bebida Coca-Cola por $1500")
                        try:
                            cantb1 = int(input("¿Cuantas unidades desea?\n"))
                            contb1 = 1500 * cantb1
                            contb1t = contb1t + contb1
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {cantb1} Hamburguesas {oph} por un total de ${contb1}")
                        input(f"{presione}")
                    if opb == 2:
                        opb = "Té Helado"
                        print("Ha seleccionado Té Helado por $1200")
                        try:
                            cantb2 = int(input("¿Cuantas unidades desea?\n"))
                            contb2 = 1200 * cantb2
                            contb2t = contb2t + contb2
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {cantb2} Bebida {opb} por un total de ${contb2}")
                        input(f"{presione}")
                    if opb == 3:
                        opb = "Jugo Natural"
                        print("Ha seleccionado Jugo Natural por $1600")
                        try:
                            cantb3 = int(input("¿Cuantas unidades desea?\n"))
                            contb3 = 1600 * cantb3
                            contb3t = contb3t + contb3
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {cantb3} Bebida {opb} por un total de ${contb3}")
                        input(f"{presione}")
                    if opb == 4:
                        opb = "Cerveza"
                        print("Ha seleccionado Cerveza por $2000")
                        try:
                            cantb4 = int(input("¿Cuantas unidades desea?\n"))
                            contb4 = 2000 * cantb4
                            contb4t = contb4t + contb4
                        except ValueError:
                            print("El valor ingresado es un valor no válido")
                        print(
                            f"Ha agregado {cantb4} Bebida {opb} por un total de ${contb4}")
                        input(f"{presione}")
                    elif opb == 5:
                        print("Ha seleccionado la opción Volver al Menú Principal")
                        input(f"{presione}")
                    elif opb == 6:
                        subb = 0
                        print("Ha seleccionado la opción Cancelar compra bebidas")
                        print("Volviendo al menú principal")
                        input(f"{presione}")
                    else:
                        print("La opción elegida no existe")
                        input("Presione Enter par continuar")
                except ValueError:
                    print("Ha seleccionado una opción no valida")
                    input(f"{presione}")
        elif opp == 3:
            print("Ha seleccionado finalizar su compra")
            subt = subh + subb
            input(f"{presione}")
        elif opp == 4:
            print("Ha seleccionado cancelar su compra")
            subb = 0
            subh = 0
            input(f"{presione}")
        else:
            print("La opción elegida no existe")
            input("Presione Enter par continuar")
    except ValueError:
        print("Ha seleccionado una opción no válida")
        input("Presione cualquier tecla para continuar")

if opp == 4:
    print("Usted ha cancelado su compra, adiós!")
elif opp == 3 and subt > 0:
    os.system("cls")
    print(f"Subtotal Haburguesas -----> ${subh}")
    print(f"Subtotal Bebidas ---------> ${subb}")
    print(f"Subtotal compra ----------> ${subt}")
    deli = 0
    delic = 0
    while deli != 1 and deli != 2:
        try:
            deli = int(input(
                "Como desea recibir su compra 1. Delivery ($2000) 2. Retiro en tienda (Sin costo):\n"))
            if deli == 1:
                delic = 2000
                print("Su compra será despachada por un costo de $2000")
                input(f"{presione}")
            elif deli == 2:
                delic = 0
                input("Ha elegido retiro en tienda sin costo")
                input(f"{presione}")
        except ValueError:
            print("Ha ingresado una opción no válida")
            input(f"{presione}")
    socio = 0
    while socio != 1 and socio != 2:
        try:
            socio = int(
                input("¿Es usted socio de Hamburguesas TapaArterias? 1. Sí 2.No:\n"))
            if socio == 1:
                desham = 0.8
                deshamp = "20%"
                desbeb = 0.9
                desbebp = "10%"
                print(
                    "Se ha aplicado un descuento de 20% a el total de hamburguesas y un 10% al total de Bebidas")
                input(f"{presione}")
            elif socio == 2:
                print(
                    "Usted no es socio de Hamburguesas TapaArterias, no tiene descuentos")
                desham = 1
                deshamp = "Sin descuento"
                desbeb = 1
                desbebp = "Sin descuento"
                input(f"{presione}")
        except ValueError:
            print("Ha ingresado una opción no válida")
            input(f"{presione}")

    totalh = subh * desham
    deshamdin = subh - totalh
    totalb = subb * desbeb
    desbebdin = subb - totalb
    total = totalh + totalb + delic
    destotalp = 0
    totaldesf = 0

    if total >= 100000:
        totald = total * 0.9
        totald = int(totald)
        destotalp = "10%"
        totaldesf = total - totald
        print("Su compra supera los $100000")
        print("Se ha aplicado un descuento del 10% en el total de su compra")
        input(f"{presione}")

    desbebdin = int(desbebdin)
    deshamdin = int(deshamdin)
    totalb = int(totalb)
    totalh = int(totalh)
    totaldesf = int(totaldesf)

    print("Detalle de boleta")
    print("--------------------------------------------------")
    print(f"Subtotal Hamburguesas ------------> $ {subh}")
    print(f"descuento Hamburguesas % ---------> {deshamp}")
    print(f"descuento Hamburguesas $ ---------> $ {deshamdin}")
    print(f"Total Hamburguesas ---------------> $ {totalh}")
    print("--------------------------------------------------")
    print(f"Subtotal Bebidas -----------------> $ {subb}")
    print(f"descuento Bebidas % --------------> {desbebp}")
    print(f"descuento Bebidas $ --------------> $ {desbebdin}")
    print(f"Total Bebidas --------------------> $ {totalb}")
    print("--------------------------------------------------")

    print(f"Subtotal compra ------------------> $ {total}")
    print(f"Descuentos al total---------------> % {destotalp}")
    print(f"Total descuento final ------------> $ {totaldesf}")
    print(f"Total final ----------------------> $ {totald}")

elif opp == 3:
    print("Ha finalizado su compra sin agregar nada al carrito")
