# Ingrese por teclado 5 números enteros positivos, súmelos y muestre el resultado de la suma.

print("En este ejercicio se te pedirá que ingreses 5 números enteros positivos, se sumarán y se monstrará el resultado de la suma")
i = 1
suma = 0

while i < 6:
    num = input("Ingrese un número entero positivo:\n")
    try:
        num = int(num)
        if num > 0:
            i = i + 1
            suma = suma + num
        else:
            print("El número ingresado es menor a 0")
    except ValueError:
        print("El valor ingresado es un valor con decimales")


print(f"La suma es {suma}")
