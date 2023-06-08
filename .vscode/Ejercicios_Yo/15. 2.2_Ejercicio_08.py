# La empresa dedicada a la venta de zapatos, ha decidido fabricar zapatos de hombre para la venta online. Los zapatos tienen un valor de $20.000 (cualquier número), pero podría variar según la demanda.
# Si la compra es igual o superior a $40.000 el envío es gratis, en caso contario, debe cancelar un monto extra de $3.000
# Determine el total a pagar por una persona que requiere X cantidad de zapatos.

print("\n")
print("Bienvenido a tu tienda de zapatos")
print("Todos los zapatos están a 20000")
print("Si tu compra es de 40000 o más, el envío es gratis")
cantidad = int(input("¿Cuantos pares de zapatos desea comprar?:\n"))
print("\n")

compra = 20000 * cantidad

if compra >= 40000:
    envio = 0
    print("Enhorabuena tu envío es gratis")
else:
    envio = 3000
    print("Envio = 3000")

mensaje = f"""
El detalle de tu compra es:
---> Subtotal:     {compra}
---> envío:        {envio}
---> Total:        {compra + envio}"""

print(mensaje)
print("\n")
