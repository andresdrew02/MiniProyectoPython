from clases.entidades import *
import utils.input_output as io # Libreria para la entrada de datos y la salida
import utils.database as database
import sys
from os import name, system

def exit():
    print("[+] ¡Adios!")
    sys.exit(0)

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def main():
    clear()
    idCliente = io.get_choice_cliente()
    print("¡Actualmente tienes los siguientes envios!")
    io.mostrar_envios(idCliente)
    
    # No quiere realizar otro envio
    if not io.realizar_otro_envio():
        exit()

    # Realizamos otro envio, para ello, primero tenemos que saber de que paquete desea realizar el envio
    idPaquete = io.get_choice_paquete()
    print("Quieres realizar un nuevo envio del paquete: %s" % idPaquete)

    # input de Seguro y Distancia
    datos_paquete = io.get_datos_envio()

    # Creamos el envio y se añade a la "base de datos"
    database.create_envio(idCliente, idPaquete, datos_paquete["seguro"], datos_paquete["distancia"])
    if io.reiniciar_programa():
        clear()
        main()
    exit()

if __name__ == '__main__':
    main()