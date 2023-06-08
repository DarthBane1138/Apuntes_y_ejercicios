# Solicite un valor numérico por pantalla, el valor debe ser impar, por lo que cada vez que se ingrese un
# número par, el sistema deberá mostrar un mensaje de error y volver a solicitar la variable, para este
# ejercicio use un ciclo de condición y el operador aritmético ‘%’, al ingresar el número impar el sistema
# deberá mostrar por una salida de pantalla el valor multiplicado por 4.

num = 2
while num % 2 == 0:
    num = int(input("Ingrese un número impar:\n"))
    if num % 2 == 0:
        print("Error, debe ingresar un número impar")
    else:
        num1 = num * 4
        print(f"El número ingresado es {num}, multiplicado por 4 el valor es {num1}")
