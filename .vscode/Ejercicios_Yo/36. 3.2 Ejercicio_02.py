# Investiga con tus compañeros sobre operaciones con String, por ejemplo

# 1. "upper()", convierte todos los caracteres de una cadena a mayúsculas
print("upper()")
cadena1 = "Hola mundo"
cadena1_mayusculas = cadena1.upper()
print(cadena1_mayusculas)  # Imprime "HOLA MUNDO"
# 2. "lower()", convierte todos los caracteres de una cadena a minúsculas
print("lower()")
cadena2 = "Hola Mundo"
cadena2_minusculas = cadena2.lower()
print(cadena2_minusculas)  # Imprime "hola mundo"
# 3. "find()", busca la primera aparición de una subcadena dentro de una cadena y devuelve su posición (índice). Si no se encuentra, devuelve -1
cadena3 = "Hola Mundo"
posicion = cadena3.find("Mundo")
print(posicion)  # Imprime 5
# 4. "replace()", reemplaza todas las apariciones de una subcadena por otra subcadena dentro de una cadena
cadena4 = "Hola Mundo"
nueva_cadena4 = cadena4.replace("Mundo", "Amigo")
print(nueva_cadena4)  # Imprime "Hola Amigo"
# 5. "split()" Divide una cadena en una lista de subcadenas utilizando un caracter delimitador. Por defecto el espacio delimitador es un espacio en blanco
cadena5 = "Hola,Amigo,Bienvenido"
lista_subcadenas = cadena5.split(",")
print(lista_subcadenas)  # Imprime ["Hola", "Amigo", "Bienvenido"]
# 6. "strip()", elimina los espacios en blanco (o caracteres especificados) al comienzo y final de una cadena.
cadena6 = "   Hola Mundo   "
print(cadena6)
cadena6_limpia = cadena6.strip()
print(cadena6_limpia)  # Imprime "Hola Mundo"
# 7. "startswith()" y "endswith()", verifican si una cadena comienza o termina con una subcadena específica respectivamente. Devuelven "True" o "False"
cadena7 = "Hola Mundo"
cadena7 = "Hola Mundo"
comienza_con_hola = cadena7.startswith("Hola")
termina_con_mundo = cadena7.endswith("Mundo")
print(comienza_con_hola)  # Imprime True
print(termina_con_mundo)  # Imprime True
