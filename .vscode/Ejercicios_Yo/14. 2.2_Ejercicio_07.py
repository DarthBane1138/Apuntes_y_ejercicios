# Se pide identificar el tipo de triángulo, para ello, ingrese el lado a, b y c, luego indique si es isósceles, equilátero o rectángulo.
# Es isósceles, si dos lados son iguales.
# Es equilátero, si sus tres lados son iguales.
# Es escaleno, sus tres lados son diferentes.

print("\n")
print("Hola soy  el identificador de triángulos")
print("Lo único malo es que soy ciego, toncs me tendrás que decir la medida de los tres ángulos")
suma = 0
a1 = 1
a2 = 1
a3 = 1

while a1 + a2 + a3 != 180:
    print("\n")
    a1 = int(input("Ingrese la medida del primer ángulo:\n"))
    a2 = int(input("Ingrese la medida del segundo ángulo:\n"))
    a3 = int(input("Ingrese la medida del tercer ángulo:\n"))

if a1 == a2 and a2 == a3:
    print("Es un triángulo equilátero")
elif a1 == a2 or a1 == a3 or a2 == a3:
    print("Es un triángulo isóceles")
elif a1 == 90 or a2 == 90 or a3 == 90:
    print("Es un triángulo rentángulo")
