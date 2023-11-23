import sys
import os
from uuid import UUID

# Agrego al path el directorio padre para poder acceder a las Clases
current_directory = os.path.dirname(__file__)
parent = os.path.dirname(current_directory)
sys.path.append(parent)

from clases.entidades import *

# Clientes y envios hardcodeados para simular una bbdd detrás
clientes = [
    Cliente('Pepe', 'Gonzalez', True),
    Cliente('Jose', 'Gierre', True),
    Cliente('Farruquito', 'Perez', False),
    Cliente('Alson', 'Hernandez', False)
]

paquetes = [
    Paquete(True, 20),
    Paquete(True, 2.5),
    Paquete(False, 31.52),
    Paquete(False, 25.12)
]

envios = [
    Envio(100, clientes[0], True, paquetes[0]),
    Envio(120.75, clientes[1], True, paquetes[1]),
    Envio(35, clientes[2], True, paquetes[2]),
    Envio(12.25, clientes[3], True, paquetes[3])
]

def get_clientes():
    return clientes

def get_cliente(uid: UUID):
    for cliente in clientes:
        if cliente.id == uid:
            return cliente

def get_paquete(uid: UUID):
    for paquete in paquetes:
        if paquete.id == uid:
            return paquete

def get_envios(uid: UUID):
    envios_cliente = []
    for envio in envios:
        if envio.cliente.id == uid:
            envios_cliente.append(envio)
    return envios_cliente

def get_paquetes():
    return paquetes

def add_envio(envio: Envio):
    envios.append(envio)

def create_envio(idCliente, idPaquete, seguro, distancia):
    envio = Envio(float(distancia), get_cliente(idCliente), True if seguro == "si" else False, get_paquete(idPaquete))
    add_envio(envio)
    print("[OK] Se ha creado el envio con id %s" % envio.id)
    return envio