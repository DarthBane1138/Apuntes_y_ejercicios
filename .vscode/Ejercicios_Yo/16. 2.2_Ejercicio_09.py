# En un delivery se venden 4 tipos de sándwich:
# Churrasco $1.500
# Completo $1.000
# Vegetariano $2.000
# Barros Luco $3.000
# Determine el total a pagar por un cliente, al indicar la cantidad de sándwiches que llevaría de cada tipo. Considere que si tiene un código de descuento se le realizará sólo un 10% al total de la venta.

print("\n")
print("1. Bienvido a sándwiches Mando, nuestras variedades son las siguientes")
print("2. Churrasco ----------> $1500")
print("3. Completo -----------> $1000")
print("4. Vegetariano --------> $2000")
print("5. Barros Luco --------> $3000")

churrasco = int(input("Ingrese la cantidad de churrascos que desea:\n"))
completo = int(input("Ingrese la cantidad de completos que desea:\n"))
vegetariano = int(input("Ingrese la cantidad de vegetarianos que desea:\n"))
barros = int(input("Ingrese la cantidad de barros luco que desea que desea:\n"))

subtotal = (1500 * churrasco) + (1000 * completo) + \
    (2000 * vegetariano) + (3000 * barros)

print("\n")
print(f"El subtotal de la compra es de {subtotal}")
desc = input("¿Tiene algún código de descuento? s/n:\n")

if desc == "s":
    total = subtotal * 0.9
    print("Ha obtenido un 10% de descuento en su compra")
    print(f"El total de su compra es de {total}")
else:
    print(f"El total de su compra es de {subtotal}")
