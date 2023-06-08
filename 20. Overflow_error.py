# En Python, una excepción de "OverflowError" se produce cuando se realiza una operación que resulta en un número demasiado grande para ser representado en un número entero


a = 2
b = 0.3216815351681321321354316584631568465198641651681365136813516984513216843216354654 + \
    9849849876513168461651651321684651

try:
    c = a ** b
    print("El resultado de la potencia es:", c)
except OverflowError:
    print("Error: el resultado de la potencia es demasiado grande para ser representado en un objeto de tipo int.")
