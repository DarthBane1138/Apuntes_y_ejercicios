# Se pide que construya un programa en Python que consulte la edad de una persona, y de acuerdo a lo ingresado indique si la persona tiene mayoría de edad o no.

nom = input("¡Hola! Por favor dime tu nombre:\n")
print(f"{nom} seas muy bienvenido")
edad = int(input("¿Que edad tienes?\n"))

if edad >= 18:
    print(f"Tienes {edad}, lo que quiere decir que eres mayor de edad")
else:
    print(f"Tienes solo {edad}, todavía no eres adulto")
