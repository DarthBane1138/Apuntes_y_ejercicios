Usuario1 = "Pedro"
Contrasena1 = "1234"
Usuario2 = "Angel"
Contrasena2 = "a4s1"

# Usuario1 --> pedro / Contraseña1 --> 1234
# Usuario2 --> angel / Contraseña2 --> a4s1

user = input("Ingrese usuario:\t")
clave = input("Ingrese contraseña:\t")

if(user == Usuario1 and clave == Contrasena1 or user == Usuario2 and clave == Contrasena2):
    print(f"bienvenido {user}")
else:
    print("No tienes permiso para acceder")
    

