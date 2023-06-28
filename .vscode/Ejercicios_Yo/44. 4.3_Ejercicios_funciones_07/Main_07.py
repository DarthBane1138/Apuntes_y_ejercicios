# Un número de parte es un identificador único para cada parte de un producto que los fabricantes utilizan cuando lo diseñan (MPN - Manufacturing Part Number). 

# Su objetivo es simplificar la referencia a esa parte. Un número de referencia identifica inequívocamente un diseño de la pieza dentro de una sola empresa, y en ocasiones la mayoría de las empresas. 

# Ejemplos de Números de Partes válidos: 
# 867961-B21 Servidor Huaweii Next Generation 2 
# 840369-A21 Servidor Huaweii Generation One 
# 777876-H55-H6 Servidor HP Proliant Intel 

# En una empresa de venta de Servidores y Hardware, se necesita un programa que realice las siguiente opciones: 

# Opción 1: Grabar
# Opción 2: Buscar 
# Opción 3: Imprimir 
# Opción 4: Salir

# Las opciones tienen las siguientes especificaciones:

# Opción 1: Grabar
# Se refiere a guardar:
# Número de Parte (Validar número de parte. Puede crear varios, mínimo 10).
# Nombre del producto (6 caracteres mínimo).
# Precio del producto (Precio mayor a cero).

# Opción 2: Buscar
# Se refiere a:
# Buscar un producto por su número de Parte válido.
# Mostrar toda su información almacenada del producto si su precio es mayor o igual a $500, en caso contrario indicar producto sin stock.

# Opción 3: Imprimir
# Se refiere a Imprimir un reporte con el nombre del producto, el número de parte y la descripción del producto junto con el valor del producto.

# Opción 4
# Se refiere a Salir del programa, considerando emitir mensaje de salida, además de incluir su nombre y apellido y la versión del programa.

from Funciones_07 import *

print("Bienvenido al programa de gestión de productos")
print("----------------------------------------------")

opcion = "0"

while opcion != "4":
    # print(productos)
    opcion = menu_seleccion()
    if opcion == "1":
        grabar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        imprimir_reporte()
    elif opcion == "4":
        mensaje_salida()
    else:
        print("Opción inválida. Intentelo nuevamente")
print("------------------------------------------")
