productos = []


def grabar_producto():
    while True:
        while True:
            numero_producto = input("Ingrese el número de producto:\n")
            existe_producto = False
            for producto in productos:
                if producto["Número Producto"] == numero_producto:
                    existe_producto = True
            if existe_producto:
                print("El número de producto ya existe. Ingrese otro número")
            else:
                break  # AQUI
        nombre_producto = input(
            "Ingrese el nombre del producto:\n")
        descripcion_producto = input("Ingrese una desripción del producto:\n")
        if validar_numero_nombre_producto(numero_producto, nombre_producto):
            break
        else:
            print("El número de producto ingresado no es válido, el número debe tener 6 números y el nombre debe ser alfanumérico de a lo menos 6 caracteres alfanuméricos")
    while True:
        try:
            precio = int(input("Ingrese el precio del producto:\n"))
            if precio > 0:
                break
            else:
                print("El precio debe ser mayor a 0")
        except ValueError:
            print("El precio ingresado no es válido. Intente nuevamente.")

    producto = {
        "Número Producto": numero_producto,
        "Nombre Producto": nombre_producto,
        "Descripcion": descripcion_producto,
        "Precio": precio
    }

    productos.append(producto)
    print("Producto grabado exitosamente")
    # Este append se utiliza para almacenar un nuevo par clave-valor


def validar_numero_nombre_producto(numero_producto, nombre_producto):
    # Validar si el número de producto y el nnombre del producto cumplen con los requisitos
    # largo numero_producto = 6, nombre = alfanumérico y largo mayor o igual a 6
    if len(numero_producto) == 6 and len(nombre_producto) >= 6:
        return True
    return False


def buscar_producto():
    numero_producto = input(
        "Ingrese el número de parte del producto a buscar:\n")
    encontrado = False
    for producto in productos:
        if producto["Número Producto"] == numero_producto:
            encontrado = True
            if producto["Precio"] >= 500:
                print("Información del producto")
                print("Número de producto:", producto["Número Producto"])
                print("Nombre de producto:", producto["Nombre Producto"])
                print("Descripción del producto:", producto["Descripcion"])
                print("Precio de producto:", producto["Precio"])
        else:
            print("Producto sin stock")
    if not encontrado:
        print("Producto no encontrado")


def imprimir_reporte():
    for producto in productos:
        print("----------Información del producto----------")
        print("Número de Producto ----->", producto["Número Producto"])
        print("Nombre del producto ---->", producto["Nombre Producto"])
        print("Descripción del producto:", producto["Descripcion"])
        print("Precio de producto ----->", producto["Precio"])
        print("--------------------------------------------")
        input("Presione Enter para continuar")


def mensaje_salida():
    print("Gracias por usar este programa")
    print("Autor: Patricio Leiva")
    print("Versión del programa: 1.0")
    input("Presione enter para continuar")


def menu_seleccion():
    print("Seleccione una opción de la siguiente lista:")
    print("1 ----------> Grabar")
    print("2 ----------> Buscar")
    print("3 ----------> Imprimir")
    print("4 ----------> Salir")
    opcion = input("Ingrese el número de opción: ")
    print("---------------------------------------------")
    return opcion
