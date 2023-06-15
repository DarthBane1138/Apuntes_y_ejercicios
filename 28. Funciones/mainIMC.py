from funcionesIMC import *

print("calculo Imc")
peso = float(input("Ingreso su peso (Kg):\n"))
estatura = float(input("Ingrese su estatura (m):\n"))
calcularimc(peso, estatura)
indicadorimc(calcularimc(peso, estatura))