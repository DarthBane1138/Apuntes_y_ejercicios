# Para crear funciones ocupar la palabra reservada def
def calcularimc(peso, estatura):
    imc = peso/(estatura**2)
    return imc

def indicadorimc(imc):
    if imc < 18.5:
        print("Bajo peso")
        print(imc)
    elif imc >= 18.5 and imc <24.9:
        print("Adecuado")
        print(imc)
    elif imc >= 25 and imc <29.9:
        print("Sobrepeso")
        print(imc)
    elif imc >= 30 and imc <34.9:
        print("Obesidad")
        print(imc)
    elif imc >= 35:
        print("Obesidad morbida")
        print(imc)  
