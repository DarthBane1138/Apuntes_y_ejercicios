# En el contexto del coronavirus, una persona ha decidido fabricar mascarillas lavables para la venta online. Las mascarillas tienen un valor de $500 pero podría variar según la demanda. Si la compra es superior a $15.000 el envío es gratis, en caso contario:
# Si es de la misma comuna el envío es de $1.000
# Si es de una comuna aledaña $2.000
# En otro caso es de $3.000
# Determine el total a pagar por una persona que requiere X cantidad de mascarillas.

print("\n")
print("Bienvenido a la venta online de mascarillas")
print("El valor unitario por mascarilla es de $500")
print("Si su compra es mayor a $15000 el envío es gratis")
print("Si el despacho es dentro de la comuna el envío tendrá un costo de solo $1000")
print("Si el despacho es en comuna aledaña, el valor es de $2000")
print("Si el despacho es en comuna lejana, el valor es de $3000")

cantidad = int(input("Ingrese la cantidad de mascarillas que desea:\n"))
subtotal = cantidad * 500
envio = 0

if subtotal > 15000:
    envio = 0
    print("lleva más de $15000 en mascarillas, su envío será gratis")
elif subtotal <= 15000:
    print("¿Vive usted en la misma comuna o bien en una comuna aledaña?")
    print("1 ----------> Misma comuna")
    print("2 ----------> Comuna aledaña")
    print("3 ----------> Ninguna de las anteriores")
    comuna = input("Escriba la opción que corresponda:\n")
    if comuna == "1":
        envio = 1000
    elif comuna == "2":
        envio = 2000
    else:
        envio = 3000

total = subtotal + envio

print("Detalle boleta")
print(f"subtotal ----------> ${subtotal}")
print(f"envio -------------> ${envio}")
print(f"total -------------> ${total}")
