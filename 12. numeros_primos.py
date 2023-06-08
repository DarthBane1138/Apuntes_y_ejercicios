# Solicitar número
num = int(input("ingrese número primo:\n"))
x = range(2, num)
contador = 0
for n in x:
    if (num%n == 0):
        contador += 1       

if(contador > 0):
    print ("El numero no es primo")
else:
    print("número es primo")
    