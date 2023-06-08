# Realiza un código que permita calcular la factorial de un número ingresado por pantalla, para ello debe
# tener en consideración que un número factorial se calcula de la siguiente manera:
# Ejemplo Factorial de 5
# 5! = 5*4*3*2*1 = 120

num = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1

if num == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("El factorial de",num,"es",factorial)
    
# se utiliza for para calcular el factorial y se imprime el resultado.