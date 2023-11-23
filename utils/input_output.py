import os 
import sys
import inquirer
from inquirer import Text
import utils.database as database

current_directory = os.path.dirname(__file__)
parent = os.path.dirname(current_directory)
sys.path.append(parent)

def get_choice_cliente():
    clientes = database.get_clientes()
    choices = []
    for i, cliente in enumerate(clientes):
        choices.append(
            ("%s %s" %(cliente.nombre , cliente.apellidos), cliente.id)
        )
    preguntas = [
        inquirer.List("idCliente", message="¿Quien eres?", choices=choices)
    ]
    respuesta = inquirer.prompt(preguntas)
    return respuesta["idCliente"]

def mostrar_envios(idCliente):
    for envio in database.get_envios(idCliente):
        print("El paquete con id %s pesa %s kg, tiene una distancia de %s km y tiene %s" %(envio.paquete.id, envio.paquete.peso, envio.distancia, "seguro" if envio.seguro else "no seguro"))
    
def realizar_otro_envio():
    confirm = [
        inquirer.Confirm("respuesta", message="¿Quiere realizar otro envio?")
    ]

    # No quiere realizar otro envio
    return inquirer.prompt(confirm)["respuesta"]

def get_choice_paquete():
    paquetes = database.get_paquetes()
    choices = []
    for i, paquete in enumerate(paquetes):
        choices.append(
            ("id: %s fragil: %s peso: %s " % (paquete.id, "Si" if paquete.fragil else "No" , paquete.peso), paquete.id)
        )
    preguntas = [
        inquirer.List("idPaquete", message="¿Cual es el paquete?", choices=choices)
    ]
    respuesta = inquirer.prompt(preguntas)
    return respuesta["idPaquete"]

def is_float_and_positive(string):
    try:
        float(string)
        if float(string) > 0:
            return True
        return False
    except ValueError:
        return False

# En este puntos solo nos falta si el envio tiene seguro o no, y la distanica
def get_datos_envio():
   questions = [
       Text("distancia", message="¿Cual es la distancia del envio?", validate=lambda _, x: is_float_and_positive(x)),
       Text("seguro", message="¿Tiene seguro? (Si o No)", validate=lambda _, x: x.lower() in ["si", "no"]),
   ]

   answers = inquirer.prompt(questions)
   return answers

def reiniciar_programa():
    questions = [
        inquirer.Confirm("reiniciar", message="¿Quiere reiniciar el programa?")
    ]
    if inquirer.prompt(questions)["reiniciar"]:
        return True
    return False