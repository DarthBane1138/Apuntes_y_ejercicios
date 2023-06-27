# En una cafetería se venden 4 tipos de cafés:
# Espresso 			$1.500
# Capuchino 		$1.800
# Latte 			$1.600
# Moca 			$1.700

# Determine el total a pagar por un cliente que puede llevar varios cafés y aplique el descuento del 10% al total a pagar, si su compra es superior o igual a $3.000.

# Considere crear un menú de opciones y calcule el monto utilizando función.

from Funciones_06 import *

print("Bienvenidos a cafetería Chokita")
mostrar_menu()

contador = 0
cantidad_espresso = 0
cantidad_capuchino = 0
cantidad_latte = 0
cantidad_moca = 0
opcion = 0

resultado_compra = compra_cafe(
    opcion, contador, cantidad_espresso, cantidad_capuchino, cantidad_latte, cantidad_moca)

contador = resultado_compra[0]
cantidad_espresso = resultado_compra[1]
cantidad_capuchino = resultado_compra[2]
cantidad_latte = resultado_compra[2]
cantidad_moca = resultado_compra[3]

contador = descuento(contador)

print("holi", contador)

imprimir_boleta(contador, cantidad_espresso,
                cantidad_capuchino, cantidad_latte, cantidad_moca)
