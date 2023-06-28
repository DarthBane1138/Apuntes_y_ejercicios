from Funciones import *

# Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
# Calcular_Iva
# Descuento
# Calcular_Imc

# Las cuales deben ser desarrolladas en funciones (métodos).

# Donde:
# Calcular_Iva: Es el precio del producto, multiplicado por el 19% (0.19)
# descuento: Es el precio del producto menos el descuento por aplicar. Mostrar el valor final del producto.
# Calcular_Imc: Índice de masa corporal. Su fórmula es: pseo/estatura^2

print("Hola, soy una calculadora con dos funciones en su vida: calcular el IVA de cada producto, calcular el descuento de un producto, o Calcular IMC")
print("Seleccione la alternativa que desee:")
print("Para calcular el IVA digite --------------------------> 1")
print("Para calcular el descuento de un producto digite -----> 2")
print("Para calcular IMC digite -----------------------------> 3")

opcion = 0

while opcion != 1 and opcion != 2 and opcion != 3:
    print("\n")
    try:
        opcion = int(input("Ingrese la opción que desea ejecutar:\n"))
        if opcion == 1:
            precio = int(input("Ingrese precio bruto para calcular el IVA:\n"))
            calculoiva(precio, iva=1.19)
        elif opcion == 2:
            precio = int(
                input("Escriba el precio del producto del cual desea calcular el descuento:\n"))
            descuentoprod = float(
                input("Escriba porcentaje de descuento que desea aplicar al producto:\n"))
            descuento(precio, descuentoprod)
        elif opcion == 3:
            peso = float(input("Ingrese su peso actual en Kg:\n"))
            altura = float(input("Ingrese su altura en metros:\n"))
            imc(peso, altura)
            indicadorimc(imc(peso, altura))
        else:
            print("Opción no válida")
    except ValueError:
        print("Error: tipo de dato no válido, por favor seleccione una opción válida")
