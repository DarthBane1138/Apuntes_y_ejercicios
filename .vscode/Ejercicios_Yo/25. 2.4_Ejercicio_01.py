# num = int(input("Ingrese un número:\n"))
# fact = 1
# i = 1
# while i <= num:
#     fact = fact * i
#     i = i + 1
# print(f"El factorial de {num} es: {fact}")

# num = int(input("Ingrese un número:\n"))
# fact = 1
# i = 1
# while i < num:
#     i = i + 1
#     fact = fact * i
# print(f"El factorial de {num} es: {fact}")

# num = int(input("Ingrese un número:\n"))
# fact = num
# i = num
# while i > 1:
#     i = i - 1
#     fact = fact * i

# print(f"El factorial de {num} es: {fact}")

num = int(input("Ingrese un número:\n"))
fact = num
i = num - 1
while i >= 1:
    fact = fact * i
    i = i - 1

print(f"El factorial de {num} es: {fact}")
