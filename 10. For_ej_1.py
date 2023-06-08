x = range(5)
con_mas_cero = 0
con_menos_cero = 0
con_cero = 0

for i in x:
    i = int(input("ingrese número\n"))
    if i > 0:
        con_mas_cero = con_mas_cero + 1
    elif i < 0:
        con_menos_cero = con_menos_cero + 1
    else:
        con_cero = con_cero + 1
        
print (f"Los números mayores a 0 son: {con_mas_cero}")
print (f"Los números menores a 0 son: {con_menos_cero}")
print (f"Los números igual a 0 son: {con_cero}")

# En el rango se define cuantas veces se me va a pedir un número, de acuerdo a esto y a los valores estándares se me pedirá un número 5 veces (0, 1, 2, 3, 4)