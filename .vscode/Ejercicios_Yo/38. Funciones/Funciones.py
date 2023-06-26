# Las funciones dividen el programa en partes, considerando la parte principal y los diferentes métodos (tareas) que deben proporcionar resultados
# Se ejecutan solo cuando son llamadas
# Pueden ser llamadas las veces que sean necesarias
# La sintaxis es
# def mi_funcion():
#     instrucciones
# La sentencia def es una definición de función usada para crear objetos funciones definidas por el usuario.

# Existen 4 tipos de funciones:
# Sin Argumentos y sin retorno
# Sin Argumentos y con retorno
# Con argumentos y sin retorno
# Con argumentos y con retorno

# Sin Argumentos y sin retorno
def saludo():
    print("Saludando a mis estudiantes")
# Función saludo(), sin argumentos y emite mensaje propio de la función.

# Sin Argumentos y con retorno


def sumar():
    num1 = 3
    num2 = 5
    return (num1 + num2)
# La función sumar sin argumentos, posee dos variables con valor y retorna la suma de ellas.

# Con argumentos y sin retorno


def sumar2(a, b):
    sumar = a + b
    print(f"La suma de los argumentos es: {sumar}")
# Función sumar(): con argumentos, posee dos variables con valor y no retorna la suma de ellas sino que muestra el resultado en la misma función.

# Con argumentos y con retorno


def sumar3(a, b):
    suma = a + b
    return (suma)

# Reto de video


def convertircelsius(temp, unidad):
    # Aquí tienes tu docstring
    if unidad == "Kelvin":
        return print(f"{temp} grados {unidad} son igual a", (temp + 273), "grados Celcius")
    elif unidad == "Fahrenheit":
        return print(f"{temp} grados {unidad} son igual a ", ((temp - 32) * (5/9)), "grados Celcius")
