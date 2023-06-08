# Ingrese un número entero mayor a cero por teclado e indique si es o no “Perfecto”.

num = 0
suma_div = 0

while num < 1:
    try:
        num = int(input(
            "Ingrese un número para evaluar si este es perfecto, este debe ser entero y mayor a 0:\n"))
        if num > 1:
            for i in range(1, num):
                if num % i == 0:
                    suma_div = suma_div + i
        else:
            print("Ha ingresado un número igual o menor a 0")
    except ValueError:
        print("Debe ingresar un número entero")

if suma_div == num:
    print(f"El número {num} es un número perfecto")
else:
    print(f"El número {num} no es un número perfecto")


# Este código recorreo todos los números desde 1 hasta num, si el mod  de num dividido por i (el número que va incrementando)
# es 0 entonces entra al if, y si entra al if a la suma de divisores se le suma i, si la suma de los i que entran en el if es igual a
# num, entonces entra al segundo if y el número es perfecto, si no, es imperfecto
