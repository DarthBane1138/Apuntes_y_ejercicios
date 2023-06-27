# Crear un programa que contenga un menú con las siguientes opciones:

# Área de un circulo
# Perímetro de un cuadrado
#  
# Ingrese los valores necesarios para calcular y entregar resultados utilizando funciones.

from Funciones_Ejercicios_ultimaclase import *

print("Hola, soy una programita que sirvo para calcular")
print("El área de un circulo -------------> 1")
print("El perímetro de un cuadrado -------> 2")

opcion = 0
radio = -1
lado = -1


while opcion != 1 and opcion != 2:
    try:
        opcion = int(input("Por favor, seleccione la opción que desea:\n"))
        if opcion == 1:
            print("Ha seleccionado la opción para calcular el área de un círculo")
            while radio < 0:
                radio = float(input("Ingrese el radio del círculo en cm:\n"))
                if radio > 0:
                    resultado_area = area(radio)
                    resultado_area = round(resultado_area, 4)
                    print(
                        f"El área del circulo de radio {radio}, es de {resultado_area} cm^2")
                else:
                    print("El valor ingresado es un número negativo")
        elif opcion == 2:
            print("Ha seleccionado la opción para calcular el perímetro de un cuadrado")
            while lado < 0:
                lado = float(
                    input("Ingrese el valor del lado del cuadrado en cm:\n"))
                if lado > 0:
                    resultado_perimetro = perimetro(lado)
                    print(
                        f"El perímetro del cuadrado de lado {lado}cm, es de {resultado_perimetro}cm")
                else:
                    print("El valor ingresado es un número negativo")
        else:
            print("La opción seleccionada no está disponible")
    except ValueError:
        print("El valor ingresado no es válido")
