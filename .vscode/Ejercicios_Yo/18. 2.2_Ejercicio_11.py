# Usted es el encargado de generar un sistema de compra, el cual consiste en:
# Seleccionar si desea el producto o no, en el caso de llevar el producto, el total de la compra debe ir aumentando dependiendo de cuantos productos lleve y el valor de cada uno de ellos, también debe ingresar si el cliente es preferencial o no,
# en el caso de ser preferencial, al final al momento de pagar se debe realizar un descuento del 25% del total de la compra,
# finalmente se solicita que ingrese el efectivo, debe calcular cuánto es el vuelto del cliente en el caso de que el efectivo sea mayor al total a pagar,
# del caso contrario verificar que el monto no sea inferior al total a pagar o enviar una salida por pantalla que diga “ Dinero insuficiente, Guardias!”.
# Los productos detallados son los siguientes:
# Agua → $ 600
# Azúcar→ $1200
# Aceite → $1500
# Arroz → $1250
# Fideos → $ 790
# Bebida→ $1780
# Chocolate → $2500
# Pan molde → $1340

print("\n")
print("Bienvenido al supermercado Chokita")
print("\n")
agua = ""
azucar = ""
aceite = ""
arroz = ""
fideos = ""
bebidas = ""
chocolate = ""
pan = ""

while agua != "s" and agua != "n":
    agua = input(
        "¿Desea llevar agua? La botella tiene un costo de $600 s/n:\n ")
if agua == "s":
    cagua = int(input("¿Cuantas unidades desea llevar?:\n"))
    subagua = cagua * 600
    subtotal = cagua * 600
    print(f"Precio agua por {cagua} unidades: ${subagua}")
    print(f"subtotal:\t ${subtotal}")
else:
    cagua = 0

while azucar != "s" and azucar != "n":
    azucar = input(
        "¿Desea llevar azúcar? La bolsa tiene un costo de $1200 s/n:\n ")
if azucar == "s":
    cazucar = int(input("¿Cuantas unidades desea llevar?:\n"))
    subazucar = cazucar * 1200
    subtotal = subtotal + (cazucar * 1200)
    print(f"Precio azucar por {cazucar} unidades: ${subazucar}")
    print(f"subtotal:\t ${subtotal}")
else:
    cazucar = 0

while aceite != "s" and aceite != "n":
    aceite = input(
        "¿Desea llevar aceite? La botella tiene un costo de $1500 s/n:\n ")
if aceite == "s":
    caceite = int(input("¿Cuantas unidades desea llevar?:\n"))
    subaceite = caceite * 1500
    subtotal = subtotal + (caceite * 1500)
    print(f"Precio aceite por {caceite} unidades: ${subaceite}")
    print(f"subtotal:\t ${subtotal}")
else:
    caceite = 0

while arroz != "s" and arroz != "n":
    arroz = input(
        "¿Desea llevar arroz? La bolsa tiene un costo de $1250 s/n:\n ")
if arroz == "s":
    carroz = int(input("¿Cuantas unidades desea llevar?:\n"))
    subarroz = carroz * 1250
    subtotal = subtotal + (carroz * 1250)
    print(f"Precio por {carroz} unidades: ${subarroz}")
    print(f"subtotal:\t ${subtotal}")
else:
    carroz = 0

while fideos != "s" and fideos != "n":
    fideos = input(
        "¿Desea llevar fideos? La bolsa tiene un costo de $790 s/n:\n ")
if fideos == "s":
    cfideos = int(input("¿Cuantas unidades desea llevar?:\n"))
    subfideos = cfideos * 790
    subtotal = subtotal + (cfideos * 790)
    print(f"Precio fideos por {cfideos} unidades: ${subfideos}")
    print(f"subtotal:\t ${subtotal}")
else:
    cfideos = 0

while bebidas != "s" and bebidas != "n":
    bebidas = input(
        "¿Desea llevar bebidas? La botella tiene un costo de $1780 s/n:\n ")
if bebidas == "s":
    cbebidas = int(input("¿Cuantas unidades desea llevar?:\n"))
    subbebidas = cbebidas * 1780
    subtotal = subtotal + (cbebidas * 1780)
    print(f"Precio por {cbebidas} unidades: ${subbebidas}")
    print(f"subtotal:\t ${subtotal}")
else:
    cbebidas = 0

while chocolate != "s" and chocolate != "n":
    chocolate = input(
        "¿Desea llevar chocolates? La barra tiene un costo de $2500 s/n:\n ")
if chocolate == "s":
    cchocolate = int(input("¿Cuantas unidades desea llevar?:\n"))
    subchocolate = cchocolate * 2500
    subtotal = subtotal + (cchocolate * 2500)
    print(f"Precio por {cchocolate} unidades: ${subchocolate}")
    print(f"subtotal:\t ${subtotal}")
else:
    cchocolate = 0

while pan != "s" and pan != "n":
    pan = input(
        "¿Desea llevar pan de molde? La bolsa tiene un costo de $1340 s/n:\n ")
if pan == "s":
    cpan = int(input("¿Cuantas unidades desea llevar?:\n"))
    subpan = cpan * 1340
    subtotal = subtotal + (cpan * 1340)
    print(f"Precio por {cpan} unidades: ${subpan}")
    print(f"subtotal:\t ${subtotal}")
else:
    cpan = 0

clientep = input("¿Es usted cliente preferencial? s/n:\n")
if clientep == "s":
    dscto = 0.75
else:
    dscto = 1

total = subtotal * dscto
descontado = subtotal - total

round(subtotal)
round(descontado)
round(total)

print("El detalle de su compra es el siguiente:")
print(f"subtotal ----------> ${subtotal}")
print(f"descuento ---------> ${descontado}")
print(f"Total a pagar -----> ${total}")

efectivo = int(input("Ingrese efectivo:\n"))
if efectivo >= total:
    vuelto = efectivo - total
    print("Muchas gracias por comprar en supermercados Chokita")
    print(f"Su vuelto es de ${vuelto}")
else:
    falta = total - efectivo
    print(f"Faltan ${falta}, ¡guardias! acercarse a caja")
