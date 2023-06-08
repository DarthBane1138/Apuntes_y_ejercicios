# Ingresar por teclado 5 números enteros, luego debe indicar:
# Cuántos números son mayores a cero
# Cuántos números son menores a cero
# Cuántos números son iguales a cero

print("En estes programa ingresarás 5 número enteros y se te dirá cuantos números son mayores a 0, cuantos son menores a 0 y cuantos son iguales a 0")

mayores_cero = 0
menores_cero = 0
igual_cero = 0

for i in range(5):
    num = int(input("Ingrese un número entero:\n"))
    if num > 0:
        mayores_cero = mayores_cero + 1
    elif num < 0:
        menores_cero = menores_cero + 1
    else:
        igual_cero = igual_cero + 1

print(f"Hay en total {mayores_cero} números mayores a 0, {menores_cero} números menores a 0, y {igual_cero} números iguales a 0")
