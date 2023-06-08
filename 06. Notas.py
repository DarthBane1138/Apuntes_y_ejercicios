import os

os.system("cls")
nota1 = float(input("Ingrese primera nota:\n"))
nota2 = float(input("Ingrese segunda nota:\n"))
nota3 = float(input("Ingrese tercera nota:\n"))
if (nota1 > 0 and nota1 <= 7 and nota2 > 0 and nota2 <= 7 and nota3 > 0 and nota3 <= 7):
    promedio = round((nota1 + nota2 + nota3) / 3, 1)

# la función round más el número despues define la cantidad de decimales que se van a mostrar

if promedio >= 4:
    print(f"Usted a aprobado con nota {promedio}")
elif promedio < 4:
    print(f"Usted ha reprobado el ramo con nota {promedio}")
else:
    print("Las notas ingresadas no están en el rango entre 1 y 7")
