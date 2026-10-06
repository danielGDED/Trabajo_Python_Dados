#Importa random para usarse mas adelante a la hora de asignar valor al los dados
import random



from rich.panel import Panel
from rich.console import Console
from rich.live import Live

console = Console()




#Cifra minima que puede tener un dado, esta puesto por si se quiere cambiar mas adelante
CIFRA_MIN = 1
#Se asigna el valor de cada dato, para poder modificarse mas adelante
DADO_D4 = 4
DADO_D6 = 6
DADO_D8 = 8
DADO_D10 = 10
DADO_D12 = 12
DADO_D20 = 20
#Valor inicial del menu para el bucle
menu = True
# Valor del dado inicial
valor_dado = 0

#Inicio del menu
while menu:
    console.print(Panel(
        "1.- Lanzar Dados\n"
        "2.- Salir"
            ))
    #optiene la opcion entre 1 y 2, cualquier otro valor es invalido
    opcion = int(input("Elija una opcion(Introduzca el numero de la opcion): "))
    # Entra al menu en el que pides el dado necesario
    if opcion == 1:
        repetir = True
        #Para evitar que de un valor no disponible y repita hasta uno valido
        while repetir:
            repetir = False
            dado_seleccionado = int(input("Introduzca el dado entre D4, D6, D8, D10, D12, D20 \nSolo introduce el numero de caras: "))
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
                    console.print("[red]Valor no valido[red]")
                    valido = True

        #Para validar que sea una cantidad de dados valida
        dados_no_valido = True
        while dados_no_valido:
            dadosLanzar = int(input("Cuantos dados quieres lanzar"))
            valor_total = 0
            if(dadosLanzar >= 0):
                dados_no_valido = True
                console.print("[red]Cantidad de dados no valida[red]")
            elif(dadosLanzar > 0):
                dados_no_valido = False
            else:
                dados_no_valido = True
                console.print("[red]Dato no valido[red]")

        #Recorre los dados que se van a lanzan pedidos
        for i in range(0, dadosLanzar, 1):

            console.print("El dado [green]" + str(i) + "[/green] ha salido " )

            #La animacion recorre 14 numeros validos y se queda con el 15, pinta todos en el mismo punto
            with Live(console=console, refresh_per_second=10) as animacion:
                    repetirAnimacion = 0
                    while repetirAnimacion < 15:
                        valor_animacion = random.randint(1, valor_dado)
                        animacion.update(Panel(
                            "[blue]" + str(valor_animacion) + "[/blue]"
                        ))
                        repetirAnimacion += 1

                        #Esto hace que se puedan ver la animacion porque sino saldria todo muy rapido
                        contador_espera = 0
                        while contador_espera < 3000000:
                            contador_espera = contador_espera + 1
            #Coge el valor del ultimo y lo suma al total
            valor_total += valor_animacion  

        console.print(Panel(
                "La suma total de los dados es: [blue]" + str(valor_total) +
                "\n[/blue]El valor promedio de los dados es: [blue]" + str(valor_total/dadosLanzar) + "[/blue]"
        ))

    elif opcion == 2:
        #El salir solo cierra el while del menu
        menu = False
    else:
        print("[red]Opcion no valida[red]")

console.print("[green]Cerrando el programa...[green]")



