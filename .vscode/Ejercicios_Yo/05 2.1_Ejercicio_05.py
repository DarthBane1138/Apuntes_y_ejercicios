# Debe crear un sistema que permita la validación de usuario y contraseña de un empleado en la Empresa XY, los únicos dos usuarios conectados son:
# User_1: pedro       Pass_1:1234
# User_2: angel       Pass_2: a4s1

user = input("Buenos días, para empezar por favor ingrese su usuario:\n")

if user.lower() == "pedro":
    contr = input("Por favor ingrese su contraseña:\n")
    if contr == "1234":
        print(f"Bienvenido {user}, Puede ingresar")
    else:
        print("contraseña incorrecta")
elif user.lower() == "angel":
    contr = input("Por favor ingrese su contraseña:\n")
    if contr == "a4s1":
        print(f"Bienvenido {user}, Puede ingresar")
    else:
        print("contraseña incorrecta")
else:
    print("El usuario no está registrado")
