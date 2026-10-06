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
            
        dadosLanzar = int(input("Cuantos dados quieres lanzar"))
        valor_total = 0

        if dadosLanzar > 0:
            for i in range(0, dadosLanzar, 1):

                console.print("El dado [green]" + str(i) + "[/green] ha salido " )

                with Live(console=console, refresh_per_second=10) as animacion:
                    repetirAnimacion = 0
                    while repetirAnimacion < 15:
                        valor_animacion = random.randint(1, valor_dado)
                        animacion.update(Panel(
                            "[blue]" + str(valor_animacion) + "[/blue]"
                        ))
                        repetirAnimacion += 1

                        contador_espera = 0
                        while contador_espera < 3000000:
                            contador_espera = contador_espera + 1
                    

            valor_total += valor_animacion  

            console.print(Panel(
                "La suma total de los dados es: [blue]" + str(valor_total) +
                "\n[/blue]El valor promedio de los dados es: [blue]" + str(valor_total/dadosLanzar) + "[/blue]"
            ))

        elif dadosLanzar <= 0:
            console.print("[red]Numero no valido[red]")
        else:
            console.print("[red]Dato no valido[red]")


    elif opcion == 2:
        menu = False
    else:
        print("[red]Opcion no valida[red]")

console.print("[green]Cerrando el programa...[green]")



