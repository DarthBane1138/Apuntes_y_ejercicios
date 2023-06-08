# Ingrese por teclado 10 letras, indique cuantas de ellas son vocales y cuántas son consonantes.

print("En este programa se te pedirán 10 letras cualquieras, se contarán las consonantes y las vocales por separado")
consonantes = 0
vocales = 0

for i in range(10):
    letra = input("Ingrese una letra del abcdario:\n")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1

print(
    f"Hay en total {vocales} letras vocales y {consonantes} letras consonantes")
