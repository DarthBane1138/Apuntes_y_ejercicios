import numpy as np
import random

# 3).- Crear un Arreglo [10][4] en el cual simula un bus, tendrá que darle de forma automática los números	de	asiento	y	luego	mostrarlo	por	pantalla de la siguiente forma

# 1	2	3	4
# 5	6	7	8
# 9	10	11	12
# 13	14	15	16
# 17	18	19	20
# 21	22	23	24
# 25	26	27	28
# 29	30	31	32
# 33	34	35	36
# 37	38	39	40

matriz = np.zeros((10, 4))
print(matriz)

for asiento in range(10):
    for columna in range(4):
        matriz[asiento][columna] = random.randint(1, 41)

print(matriz)
