import random


CIFRA_MIN = 1

DADO_D4 = 4
DADO_D6 = 6
DADO_D8 = 8
DADO_D10 = 10
DADO_D12 = 12
DADO_D20 = 20

menu = True

valor_dado = 0

while menu:
    print("1.- Lanzar Dados")
    print("2.- Salir")
    opcion = int(input("Elija una opcion(Introduzca el numero de la opcion): "))
    if opcion == 1:
        dado_seleccionado = int(input("Introduzca el dado entre D4, D6, D8, D10, D12, D20, solo introduce el numero"))
        match dado_seleccionado:
            case 4:
                valor_dado = DADO_D4
            case 6:
                valor_dado = DADO_D6
            case 8:
                valor_dado = DADO_D8
            case 10:
                valor_dado = DADO_D10
            case 12:
                valor_dado = DADO_D12
            case 20:
                valor_dado = DADO_D20
            case _:
                print("Valor no valido")
        dadosLanzar = int(input("Cuantos dados quieres lanzar"))
        if dadosLanzar > 0:
            for i in range(0, dadosLanzar, 1):
                e = 1


        elif dadosLanzar <= 0:
            print("Numero no valido")
        else:
            print("Dato no valido")


    elif opcion == 2:
        menu = False
    else:
        print("Opcion no valida")

print("Cerrando el programa...")



