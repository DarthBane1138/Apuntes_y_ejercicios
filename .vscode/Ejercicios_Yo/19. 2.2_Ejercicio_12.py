# Se requiere implementar un sistema para el mesón de CineDuoc, en el cual, va desde el sistema de venta de boletos, hasta los agregados (palomitas y bebidas.).
# Una simulación del sistema comienza con consultar al cliente si pertenece a Duoc (estudiante o funcionario), el cliente muestra la placa o identificación (en caso de tener)
# por lo que el vendedor registra en el sistema True o False (Pertenece, no pertenece). Luego le consulta que entrada desea: Las posibles entradas son:
# Estreno → $4.800
# Normal → $2.900
# El cliente al seleccionar una, también debe indicar la cantidad que desea, luego el sistema le consultará si desea agregar palomitas de maíz a su pedido, si la respuesta es “si”, entonces el sistema muestra las siguientes promociones:
# Palomitas Pequeña → $2.500
# Palomitas Mediana → $4.500
# Palomitas Grande → $7.800

import time


print("Bienvenido a Cine Duoc")
pduoc = input(
    "¿Pertenece usted a la institución de Duoc? sí/no:\n")
if pduoc.lower() == "sí" or pduoc.lower() == "si":
    codigo = input(
        "Por favor, presente su credencial ingresando su código de 6 dígitos\n")
    if (len(codigo)) == 6:
        pduoc = 0.7
        print("Usted pertenece a Duoc UC")
    else:
        pduoc = 1
        print("Código no válido, usted no pertenece a Duoc UC")
else:
    pduoc = 1
    print("\n")
    print("Usted no pertenece a Duoc UC, pero no importam igual nomás podrá ingresar")

print("\n")
print("Tenemos dos tipos de entradas")
print("1. Estreno ----------> $4800")
print("2. Normal -----------> $2900")
print("\n")

opcion = ""
while opcion not in ["1", "2"]:
    opcion = input(
        "Seleccione 1 para entrada estreno, y 2 para entrada normal:\n")
    if opcion == "1":
        entrada = 4800
        print(f"Ha seleccionado entrada estreno por ${entrada}")
        funcion = "Estreno"
    elif opcion == "2":
        entrada = 2900
        print(f"Ha seleccionado entrada normal por ${entrada}")
        funcion = "Normal"
    else:
        print("Selección no válida, por favor seleccione una opción válida")
        print("\n")

cantidade = 0
while cantidade <= 0:
    cantidade = int(input("¿Cuantas entradas desea?\n"))
    if cantidade > 0:
        totale = cantidade * entrada
        print(
            f"Usted lleva {cantidade} entradas para función {funcion} por subtotal de ${totale}")
    else:
        print("Ha ingresado una cantidad igual o menor a 1, por favor ingrese valores de 1 hacia arriba")

print("\n")
palomitas = input("¿Desea agregar palomitas de maíz?\n")
if palomitas.lower() == "sí" or palomitas.lower() == "si":
    tpalomita = ""
    while tpalomita != "palomita pequeña" and tpalomita != "palomita mediana" and tpalomita != "palomita grande":
        print("\n")
        print("Contamos con las siguientes promociones")
        print("1. Palomitas Pequeñas ----------> $2500")
        print("2. Palomitas Medianas ----------> $4500")
        print("3. Palomitas Grandes -----------> $7800")
        print("\n")
        tpalomita = input(
            "Selección el número correspondiente a la opción que desea:\n")
        if tpalomita == "1":
            tpalomita = "palomita pequeña"
            palomita = 2500
            print(f"Ha seleccionado palomitas pequeñas por ${palomita}")
        elif tpalomita == "2":
            tpalomita = "palomita mediana"
            palomita = 4500
            print(f"Ha seleccionado palomitas medianas por ${palomita}")
        elif tpalomita == "3":
            tpalomita = "palomita grande"
            palomita = 7800
            print(f"Ha seleccionado palomitas grandes por ${palomita}")
        else:
            print(
                "Ha seleccionado una opción no válida, por favor selecciona una opción válida")
            time.sleep(2)
else:
    print("No lleva palomitas, cagón")
    totalp = 0

if palomitas.lower() == "sí" or palomitas.lower() == "si":
    cantidadp = 0
    while cantidadp <= 0:
        cantidadp = int(input("¿Cuantas unidades desea llevar?\n"))
        if cantidadp > 0:
            totalp = cantidadp * palomita
            print(
                f"Usted lleva {cantidadp} {tpalomita} por subtotal de ${totalp}")
        else:
            print(
                "Ha ingresado una cantidad igual o menor a 1, por favor ingrese valores de 1 hacia arriba")


print("\n")
bebidas = input("¿Desea llevar bebestibles? sí o no\n")
if bebidas.lower() == "si" or bebidas.lower() == "sí":
    tbebidas = ""
    while tbebidas != "bebida pequeña" and tbebidas != "bebida mediana" and tbebidas != "bebida grande":
        print("\n")
        print("Contamos con las siguientes promociones")
        print("1. Bebida Pequeña ----------> $1000")
        print("2. Bebida Mediana ----------> $1250")
        print("3. Bebida Grande -----------> $2000")
        print("\n")
        tbebidas = input(
            "Seleccione el número correspondiente a la opción que desea:\n")
        if tbebidas == "1":
            tbebidas = "bebida pequeña"
            bebida = 1000
            print(f"Ha seleccionado bebida pequeña por ${bebida}")
        elif tbebidas == "2":
            tbebidas = "bebida mediana"
            bebida = 1250
            print(f"Ha seleccionado bebida mediana por ${bebida}")
        elif tbebidas == "3":
            tbebidas = "bebida grande"
            bebida = 2000
            print(f"Ha seleccionado bebida grande por ${bebida}")
        else:
            print(
                "Ha seleccionado un opción no válida, por favor seleccione una opción válida")
else:
    print("No lleva bebidas, cagón")
    totalb = 0

if bebidas.lower() == "sí" or bebidas.lower() == "si":
    cantidadb = 0
    while cantidadb <= 0:
        cantidadb = int(input("¿Cuantas unidades desea llevar?\n"))
        if cantidadb > 0:
            totalb = cantidadb * bebida
            print(
                f"Usted lleva {cantidadb} {tbebidas} por subtotal de ${totalb}")
        else:
            print(
                "Ha ingresado una cantidad igual o menor a 1, por favor ingrese valores de 1 hacia arriba")


total = (totale * pduoc) + totalp + totalb
total = round(total)

print("\n")
print("------------detalle de compra------------")
print(f"Total entradas ---------------------> ${entrada * cantidade}")
print(f"Descuento aplicado a entrada -------> {100-pduoc * 100}%")
print(f"Total palomitas --------------------> ${totalp}")
print(f"Total bebidas ----------------------> ${totalb}")
print("-----------------------------------------------------")
print(f"Total de compra --------------------> ${total}")

efectivo = 0
while total > efectivo:
    efectivo = int(input("Ingrese cantidad de efectivo a pagar:\n"))
    if efectivo >= total:
        vuelto = efectivo - total
    else:
        falta = total - efectivo
        print(
            f"Cantidad de dinero insuficiente, le faltan ${falta}, ingrese nuevamente una cantidad igual o mayor a ${total}")

print("Gracias por su compra")
print(f"Su vuelto es de ${vuelto}, disfrute de la función")
