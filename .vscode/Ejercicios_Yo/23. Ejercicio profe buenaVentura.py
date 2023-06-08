menu = True
while menu:
    print("***MENU ENTRADAS***")
    print("1. Entrada Infantil")
    print("2. Entrada General")
    print("3. Entrada 3era Edad")
    print("4. Imprimir Boleta")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese opcion\n"))
        if(opcion >0 and opcion < 6):
            if(opcion ==1):
                print("***Entrada Infantil***")
                nomI = 'Entrada Infantil'
                precioI= 2500
                dsctoI = 0.90
                cantI = int(input("Ingrese cantidad de entradas\n"))
                finalI = cantI * precioI
                op = int(input("Desea seguir comprando?  1.SI   2.NO\n"))
                if(op == 2):
                    menu = False
            elif(opcion ==2):
                print("***Entrada General***")
                nomG = 'Entrada General'
                precioG= 5000
                dsctoG = 0.95
                cantG = int(input("Ingrese cantidad de entradas\n"))
                finalG = cantG * precioG
                op = int(input("Desea seguir comprando?  1.SI   2.NO\n"))
                if(op == 2):
                    menu = False
            elif(opcion ==3):
                print("***Entrada 3era Edad***")
                nomT = 'Entrada 3era Edad'
                precioT= 1000
                cantT = int(input("Ingrese cantidad de entradas\n"))
                finalT = cantT * precioT
                op = int(input("Desea seguir comprando?  1.SI   2.NO\n"))
                if(op == 2):
                    menu = False
            elif(opcion ==4):
                print("Opción de Pago")
                dia= input("Ingrese dia de asistencia\n")
                if(dia == 'viernes' or dia == 'VIERNES'):
                    finalI = dsctoI * cantI * precioI
                    finalG = dsctoG * cantG * precioG
                    aplDscto = 'aplica dscto'
                    print("*******DETALLE BOLETA*******")
                    print(f"|CANTIDAD| NOMBRE | PRECIO |")
                    print(f"|{cantI} | {nomI} | {finalI}|")
                    print(f"|{cantG} | {nomG} | {finalG}|")
                    print(f"|{cantT} | {nomT} | {finalT}|")
                    totalD = finalI + finalG + finalT
                    print(f" Total a pagar: {totalD}")
                else:
                    print("*******DETALLE BOLETA*******")
                    print(f"|CANTIDAD| NOMBRE | PRECIO |")
                    print(f"|{cantI} | {nomI} | {finalI}|")
                    print(f"|{cantG} | {nomG} | {finalG}|")
                    print(f"|{cantT} | {nomT} | {finalT}|")
                    totalD = finalI + finalG + finalT
                    print(f" Total a pagar: {totalD}")
                menu = False
            elif(opcion ==5):
                menu = False
        else:
            print("no existe esa opcion")
    except:
        print("opcion invalida")
        
print("Gracias por su compra")
