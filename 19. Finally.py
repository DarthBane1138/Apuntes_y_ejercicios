# En Python, la instrucción "Finally" se utiliza enn conjunto con la estructura "Try/Except" para definir un bloque de código que se ejecutará siempre, independiente de si se produjo o no una excepción la Sintaxis básica de un bloque "try/except/finally" es.

# try:
# Bloque de código que se puede generar una excepción
# except TipoDeExcepcion:
# Bloque de código que se ejecuta si se produce una excepción del tipo TipoDeExcepcion
# finally:
# Bloque de código que se ejecuta siempre, independientemente de si se produjo una excepción o no

# El bloque finally se utiliza para ejecutar cualquier código que sea necesario después de que se haya terminado el bloque "try/except".

try:
    # Código que puede producir una excepción
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
finally:
    # Código que siempre se ejecutará, sin importar si se produjo una excepción o no.
    print("Gracias por utilizar la calculadora.")
