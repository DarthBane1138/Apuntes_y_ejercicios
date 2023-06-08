# Calcular la potencia de un número usando ciclos (no podrá usar el operador aritmético **), para ello el
# sistema solicitará por pantalla el valor de la base y el valor del exponente (ejemplo, base=4, exponente=
# 2 entonces el resultado será 16), una vez realizado el calculo se mostrará el resultado por una salida por
# pantalla mostrando la información de la siguiente manera ↓
# “El resultado de la potencia de base 4 y exponente 2 es 16.”

num = int(input("Ingrese el número el cual desea como base de la potencia:\n"))
exp = int(input("Ingrese el exponente al cual desea elevr el número ingresado:\n"))

res = 1

for i in range(exp):
    res = num * res

print(f"El resultado de la potencia de base {num} y exponente {exp} es {res}")