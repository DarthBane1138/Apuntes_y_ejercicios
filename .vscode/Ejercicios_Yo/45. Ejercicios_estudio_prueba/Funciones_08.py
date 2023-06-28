from datetime import datetime
import os
afiliados = []


def menus():
    print("Bienvenido a ISAPRE TKG, por favor seleccione una de las opciones disponibles")
    print("1. Agregar a un afiliado")
    print("2. Buscar a un afiliado")
    print("3. Listar afiliad@s por estado civil")
    print("4. Mostrar el listado completo de los afiliados")
    print("5. Salir")


def validar_rut(rut):
    # Esta función reemplaza los puntos y los guiones por espacios vacios, para dejar todos en formato estándar
    rut = rut.replace(".", "").replace("-", "")
    if len(rut) < 2:  # Aquí, se verifica el largo del rut, si este es menor a 2 se vuelve False, debido a que el rut debe tener una longitud de 2 (Cuerpo y dígito verificador)
        return False
    # Acá se separa el cuerpo del rut y el dígito verificador. El cuerpo se guarda el la variable cuerpo
    cuerpo = rut[:-1]
    # El dígito verificador se guarda el la variable dv y se le convierte en mayúscula
    dv = rut[-1].upper()
    suma = 0  # Se inicializan variables para calculo de dígito verificador
    multiplo = 2  # Se inicializan variables para calculo de dígito verificador
    # Este bucle for recorre el cuerpo del rut en orden inverso utilizando la función reversed.
    for c in reversed(cuerpo):
        # Por cada iteración, se multiplica el dígito actual por el valor de multiplo y se suma al valor acumulado en suma
        suma += int(c) * multiplo
        multiplo += 1  # El múltiplo se incrementa en 1
        if multiplo == 8:  # Si el múltiplo alcanza el valor de 8, se reinicia a 2
            multiplo = 2  # Esto se hace para calcular la suma ponderada de los dígitos del cuerpo del RUT
    # Luego del bucle, se calcula el resultado de la fórmula para determinar el dígito verificador válido. Se resta el resultado de "suma" modulo 11 a 11. El resultado se guarda en la variable "resultado"
    resultado = 11 - (suma % 11)
    if resultado == 11:  # Se realizan comprobaciones
        resultado = "0"  # Si el resultado es igual a 11 se asigna string "0" a resultado
    elif resultado == 10:  # Si el resultado es igual a 10, se asigna el string "K" a resultado
        resultado = "K"
    else:
        # En otros casos se convierte "resultado" a string utilizando la función str()
        resultado = str(resultado)
    # Finalmente, se verifica si el "resultado" calculado es igual al dígito verificador original "dv" Si son iguales, se devuelve "True, lo que indica que el Rut es válido. De l contrario se devuelve "False.
    return resultado == dv

# En resumen, esta función toma un Rut como entrada, realiza cálculos para determinar el dígito verificador válido


def agregar_afiliado():
    os.system("cls")
    existe_rut = True
    while existe_rut == True:
        rut = input("Por favor ingrese el rut del nuevo afiliado:\n")
        rut = rut.replace(".", "").replace("-", "")
        existe_rut = False
        for afiliado in afiliados:
            if afiliado["Rut"] == rut:
                existe_rut = True
                break
        if existe_rut:
            print("El rut del afiliado ya existe, ingrese un rut válido")
            presione()
            os.system("cls")
        else:
            break
    while validar_rut(rut) != True:
        print("El rut ingresado no es válido. Por favor ingrese un rut válido")
        rut = input("Ingrese el rut del nuevo afiliado:\n")

    nombre = input("Por favor ingrese el nombre del nuevo afiliado:\n")
    edad = 0
    while edad < 18:
        try:
            edad = int(input("Ingrese la edad del nuevo afilidado:\n"))
            if edad < 18:
                print(
                    "El nuevo afiliado debe ser mayor de edad, ingrese una edad válida")
        except ValueError:
            print("El valor ingresado para el campo \"edad\" no es válido")
            edad = int(
                input("Ingrese una edad válida para el nuevo afilidado:\n"))

    estado_civil = estado_civil_afiliado()

    fecha_afiliacion = ingreso_fecha()

    afiliado = {
        "Rut": rut,
        "Nombre": nombre,
        "Edad": edad,
        "Estado Civil": estado_civil,
        "Fecha de Afiliación": fecha_afiliacion
    }

    afiliados.append(afiliado)
    print("Registro almacenado exitosamente")
    print("Rut ------------------------->", rut)
    print("Nombre ---------------------->", nombre)
    print("Edad ------------------------>", edad)
    print("Estado Civil ---------------->", estado_civil)
    print("Fecha de afiliación --------->", fecha_afiliacion)
    presione()


def buscar_afiliado():
    rut = input("Ingrese el Rut de la persona que desea buscar:\n")
    rut = rut.replace(".", "").replace("-", "")
    encontrado = False
    for afiliado in afiliados:
        if afiliado["Rut"] == rut:
            print("---------- Información de afiliado ----------")
            print("Rut -------------------->", afiliado["Rut"])
            print("Nombre ----------------->", afiliado["Nombre"])
            print("Edad ------------------->", afiliado["Edad"])
            print("Estado Civil ----------->", afiliado["Estado Civil"])
            print("Fecha de Afiliación ---->", afiliado["Fecha de Afiliación"])
            encontrado == True
            presione()
            break
    if encontrado == False:
        print("No existe una afiliado con el rut ingresado")


def estado_civil():
    estado_civil = input(
        "Ingrese el estado civil del cual necesita revisar sus afiliados:\n")
    while estado_civil not in ["C", "S", "V"]:
        print("El estado civil ingresado no es válido")
        estado_civil = input(
            "Ingrese su estado civil: (C = Casad@, S = Solter@, V = Viud@):\n")
        estado_civil = estado_civil.upper()
    afencontrado = 0
    for afiliado in afiliados:
        if afiliado["Estado Civil"] == estado_civil:
            afencontrado = afencontrado + 1
            print("---------- Información de afiliado ----------")
            print("Rut", afiliado["Rut"])
            print("Nombre", afiliado["Nombre"])
            print("Edad", afiliado["Edad"])
            print("Estado Civil", afiliado["Estado Civil"])
            print("Fecha de Afiliación", afiliado["Fecha de Afiliación"])
            print("---------------------------------------------")
    if afencontrado > 0:
        print(f"Afiliados {estado_civil} encontrados: {afencontrado}")
    else:
        print(
            f"No se ha encontrado un afiliado con estado civil {estado_civil}")
    presione()


def presione():
    input("Presione Enter para continuar...")


def opcion_salir(menu):
    op = 3
    while op != 1 and op != 2:
        print("Ha selecionado la opción salir")
        op = int(input("¿Está seguro que desea salir?\n1. Sí \n2. No\n"))
        if op == 1:
            print("Salida confirmada. Adiós")
            break
        elif op == 2:
            print("Regresando al menú de selección")
            input("Presione enter para continuar...")
        else:
            print("La opción seleccionada no es válida")


def estado_civil_afiliado():
    estado_civil = "Indeterminado"
    while estado_civil not in ["Casad@", "Solter@", "Viud@"]:
        estado_civil = input(
            "Ingrese su estado civil: (C = Casad@, S = Solter@, V = Viud@):\n")
        estado_civil = estado_civil.upper()
        if estado_civil == "C":
            estado_civil = "Casad@"
            return estado_civil
        elif estado_civil == "S":
            estado_civil = "Solter@"
            return estado_civil
        elif estado_civil == "V":
            estado_civil = "Viud@"
            return estado_civil
        else:
            print("El estado civil ingresado no es válido")
            presione()


def ingreso_fecha():
    while True:
        try:
            fecha_afiliacion = input(
                "Ingrese fecha con el formato (DD/MM/YYYY):\n")
            fecha_afiliacion = datetime.strptime(
                fecha_afiliacion, "%d/%m/%Y").date()
            print("Fecha ingresada:", fecha_afiliacion)
            return fecha_afiliacion
        except ValueError:
            print("Formato de fecha incorecto")


def mostrar_todo():
    for afiliado in afiliados:
        print("---------- Información de afiliado ----------")
        print("Rut", afiliado["Rut"])
        print("Nombre", afiliado["Nombre"])
        print("Edad", afiliado["Edad"])
        print("Estado Civil", afiliado["Estado Civil"])
        print("Fecha de Afiliación", afiliado["Fecha de Afiliación"])
        print("---------------------------------------------")
        presione()
