from Funciones import *

# # Sin argumentos y sin retorno
# saludo()

# # Sin argumentos y con retorno
# print("La suma es: ", sumar())

# # Con argumentos y sin retorno
# num1 = int(input("Ingrese primer número:\n"))
# num2 = int(input("Ingrese segundo número:\n"))
# sumar2(num1, num2)

# # Con argumentos y con retorno
# num3 = int(input("Ingrese tercer número:\n"))
# num4 = int(input("Ingrese cuarto número:\n"))
# print("El resultado de la suma es: ", sumar(num3, num4)) # Muestra mensaje y hace llamada a la función sumar() con argumentos

# Reto de video
unidad = 0
while unidad != "Kelvin" and unidad != "Fahrenheit":
    unidad = (input(
        "Seleccione a que unidad desea convertir la temperatura en grados Celsius: K para grados Kelvin o F para grados fahrenheit:\n")).lower()
    if unidad == "k":
        unidad = "Kelvin"
    elif unidad == "f":
        unidad = "Fahrenheit"
    else:
        print("La unidad ingresada no es una unidad válida")

temp = int(
    input(f"Ingrese la temperatura en grados {unidad} para realizar el cálculo:\n"))

convertircelsius(temp, unidad)
