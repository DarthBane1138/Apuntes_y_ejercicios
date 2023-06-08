print("Buen día alumno, ahoy sacaremos el promedio de tu semestre")
# Ingrese 3 notas por teclado (valide que sean entre 1 y 7) y calcule su promedio. Si la nota resultante es mayor o igual a 4.0 entonces indique que está aprobado, en caso contrario notifique que está reprobado.

nota1 = float(input("Ingresa tu primera nota:\n"))
nota2 = float(input("Ingresa tu segunda nota:\n"))
nota3 = float(input("Ingresa tu tercera nota:\n"))

promedio = round((nota1 + nota2 + nota3)/3, 1)

if promedio >= 4:
    print(f"Tu promedio es {promedio}, has aprobado")
else:
    print(f"Tu promedio es {promedio}, has reprobado")
