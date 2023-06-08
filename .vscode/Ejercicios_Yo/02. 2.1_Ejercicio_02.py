# Utilizando un ingreso de variables de tipo numérica con Int (input()), se pide el valor de X para resolver la siguiente ecuación:
# ((x**2)+3*x+1)/4
# Muestre el resultado con un mensaje por pantalla.

nom = input("Bienvenido, por favor ingresa tu nombre para comenzar:\n")
print(f"Bienvenido {nom}, en esta ocasión vamos a resolver una ecuación")
print("((X^2) + 3x + 1) / 4")
x = int(input("Por favor ingrese el valor deseado para x:\n"))

y = ((x**2)+3*x+1)/4

print(f"El resultado de la operación es {y}")
