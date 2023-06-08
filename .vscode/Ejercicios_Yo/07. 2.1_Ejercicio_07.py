# Genere un convertidor de:
# Dólar australiano a pesos chilenos
# Peso Argentino a peso chileno
# Yen a pesos chilenos
# Considere que los valores son variables.


print("\n")
print("Bienvenido al convertidor de divisas")
print("\n")
print("Aquí podrá convertir Dolar Australiano a Peso Chileno")
print("Peso Argentino a Peso Chileno")
print("Y Yen a Peso Chileno")

# 1 dolar australiano = 529.67 Pesos Chilenos
# 1 Peso Argentino = 3.62 pesos chilenos
# 1 Yen = 6 pesos chilenos
# Precios de monedas observadas el 24/04/2023

print("\n")

moneda = input("Ingrese la moneda que desea convertir a pesos chilenos:\n")

if moneda.lower == "Dolar Australiano" or "Dolares Australianos":
    cantidad = float(
        input("Ingrese cantidad de Dolares Australianos a convertir:\n"))
    clp = round((cantidad*529.67)/1, 1)
    print(f"El resultado son {clp} Pesos Chilenos")
elif moneda.lower == "Peso Argentino" or "Pesos Argentinos":
    cantidad = float(
        input("Ingrese cantidad de Pessos Argentinos a convertir:\n"))
    clp = round((cantidad*3.62)/1, 1)
    print(f"El resultado son {clp} Pesos Chilenos")
elif moneda.lower == "Yen" or "Yenes":
    cantidad = float(
        input("Ingrese cantidad de Yenes a convertir:\n"))
    clp = round((cantidad*6)/1, 1)
    print(f"El resultado son {clp} Pesos Chilenos")
else:
    print("La moneda seleccionada no se encuentra disponible para calculo")
