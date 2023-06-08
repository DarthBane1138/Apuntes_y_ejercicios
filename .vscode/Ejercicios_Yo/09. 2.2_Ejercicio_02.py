# Ingrese por teclado dos números enteros positivos, súmelos y entregue su resultado.

num1 = float(input("Ingrese un número entero positivo:\n"))
num2 = float(input("Ingrese otro número entero positivo:\n"))

if isinstance(num1, int) and isinstance(num1, int) and num1 >= 0 and num2 >= 0:
    resultado = num1 + num2
    print(f"El resultado de la suma de los números ingresados es: {resultado}")
else:
    print("Uno o los dos números ingresados son negativos, o no son enteros")
