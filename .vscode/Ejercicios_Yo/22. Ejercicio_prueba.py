menu = """Bienvenido a club Buena Ventura
Los valores de las entradas son los siguientes, con decuentos los viernes
|   Tipo de entrada   |     Detalle     |     Precio     |Descuentos viernes|
|1.      Menores      | De 5 a 12 años  |     $2500      |       10%        |
|2.      Adultos      | De 13 a 64 años |     $5000      |       5%         |
|3.  Adultos Mayores  | Desde 65 y más  |     $1000      |       --         |
\n"""

respuesta = ""

while respuesta.lower() != "aceptar":

    print(f"{menu}")

    menor = 1
    adulto = 1
    dia = ""
    cantm = 0
    canta = 0
    cantam = 0
    contadorm = 0
    contadora = 0
    contadoram = 0
    menort = 0
    adultot = 0
    adultomt = 0
    total = 0
    vmenor = 1
    vadulto = 1
    vadultom = 1

    while dia.lower() not in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "sabado", "domingo"]:
        dia = input("Para que día desea las entradas:\n")
        if dia.lower() == "viernes":
            print("Se han aplicado descuentos")
            print("\n")
            menor = menor * 0.9
            adulto = adulto * 0.95
        elif dia.lower() in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "sabado", "domingo"]:
            print("Los precios serán los regulares")
            print("\n")
        else:
            print("El día que ha escrito no existe")

    opcion = ""
    while opcion.lower() != "terminar" and opcion.lower() != "salir":
        opcion = input(
            "Seleccione el número de la opción que desea comprar, si desea completar la compra escriba \"terminar\" o \"salir\":\n")
        if opcion == "1":
            vmenor = 2500 * menor
            vmenor = int(vmenor)
            print(f"Ha seleccionado la opción de entrada menor por ${vmenor}")
            cantm = int(input("¿Cuantas entradas de menor desea?\n"))
            contadorm = (vmenor * cantm) + contadorm
            menort = contadorm/vmenor
            menort = int(menort)
        elif opcion == "2":
            vadulto = 5000 * adulto
            vadulto = int(vadulto)
            print(
                f"Ha seleccionado la opción de entrada Adulto por ${vadulto}")
            canta = int(input("¿Cuantas entradas de Adulto desea?\n"))
            contadora = (vadulto * canta) + contadora
            adultot = contadora/vadulto
            adultot = int(adultot)
        elif opcion == "3":
            vadultom = 1000
            print(
                f"Ha seleccionado la opción de entrada Adulto Mayor por ${vadultom}")
            cantam = int(input("¿Cuantas entradas de Adulto Mayor desea?\n"))
            contadoram = (vadultom * cantam) + contadoram
            adultomt = contadoram/vadultom
            adultomt = int(adultomt)
        elif opcion.lower() == "terminar" or opcion.lower() == "salir":
            print("Ha seleccionado la opción terminar")
        else:
            print("Ha seleccionado una opcion no válida")

    total = contadorm + contadora + contadoram

# Se están evaluando 6 condiciones distintas, y no todas se van a mostrar, por eso hay tres if seguidos

    if menort > 0 or adultot > 0 or adultomt > 0:
        if menort > 0:
            print(f"Entradas menores --------------------->  {menort}")
            print(f"Subtotal entradas menores-------------> ${contadorm}")
        if adultot > 0:
            print(f"Entradas adultos --------------------->  {adultot}")
            print(f"Subtotal entradas adultos-------------> ${contadora}")
        if adultomt > 0:
            print(f"Entradas adultos mayores ------------->  {adultomt}")
            print(f"Subtotal entradas adultos mayores ----> ${contadoram}")
    else:
        print("Ha finalizado su compra sin agregar nada al carrito")

    print("¿Está de acuerdo con el detalle de su compra?")
    print("Si está de acuerdo escriba \"aceptar\"")
    print("Si desea anular la compra escriba \"anular\"")
    respuesta = input("¿Que desea hacer?\n")

subtotal = (menort * 2500) + (adultot * 5000) + (contadoram)
descuentost = subtotal - total

print("\n")
print("Gracias por su compra, el detalle de su boleta es el siguiente")
print("----------Entradas----------")
print(f"{menort} entradas Menores ------------------> $ {contadorm}")
print(f"{adultot} entradas Menores ------------------> $ {contadora}")
print(f"{adultomt} entradas Adulto Mayor -------------> $ {contadoram}")
print("-----------------------------------------------------")
print(f"Subtotal de la compra -----------------------> $ {subtotal}")
print(f"Descuentos ----------------------------------> $ {descuentost}")
print(f"Total a pagar -------------------------------> $ {total}")
