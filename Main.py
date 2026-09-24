import random


CIFRA_MIN = 1

DADO_D4 = 4
DADO_D6 = 6
DADO_D8 = 8
DADO_D10 = 10
DADO_D12 = 12
DADO_D20 = 20

menu = True

while menu:
    input("1.- Lanzar Dados")
    input("2.- Salir")
    opcion = int(input("Elija una opcion"))
    if opcion == 1:
        dadosLanzar = int(input("Cuantos dados quieres lanzar"))
        if dadosLanzar > 0:
            for i in range(0, dadosLanzar, 1):
                dado_seleccionado = int(input("Introduzca el dado entre D4, D6, D8, D10, D12, D20"))

        elif dadosLanzar <= 0:
            input("Numero no valido")
        else:
            input("Dato no valido")


    elif opcion == 2:
        menu = False
    else:
        input("Opcion no valida")

input("Cerrando el programa...")



