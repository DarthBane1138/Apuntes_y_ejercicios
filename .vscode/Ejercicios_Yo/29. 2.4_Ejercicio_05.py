# Ingrese un número entero mayor a cero por teclado e indique si es o no “Primo”.

num = 0
x = 2
cont = 0

while num < x:
    try:
        num = int(input("Ingrese un número primo:\n"))
        if num < 0:
            print("El número ingresado es menor a 0")
        while x < num:
            if num % x == 0:
                cont = cont + 1
            x = x + 1
    except ValueError:
        print("Debe ingresar un número entero")

if cont > 0:
    print("El número no es primo")
else:
    print("El número es primo")


# num = int(input("ingrese número primo:\n"))
# x = range(2, num)
# contador = 0
# for n in x:
#     if (num%n == 0):
#         contador += 1

# if(contador > 0):
#     print ("El numero no es primo")
# else:
#     print("número es primo")
