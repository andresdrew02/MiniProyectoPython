import sys
import os
import pytest
import uuid
# Agrego al path el directorio padre para poder acceder a las Clases
current_directory = os.path.dirname(__file__)
parent = os.path.dirname(current_directory)
sys.path.append(parent)

from utils.calculos import *
from clases.entidades import *

cliente = Cliente("Pepe", "Gonzalez", True)
paquete = Paquete(fragil=True, peso=2.5)
envio = Envio(distancia=2.5, cliente=cliente, seguro=True, paquete=paquete)
cliente_2 = Cliente("Jose", "Gomez", False)
paquete_2 = Paquete(fragil=False, peso=15)
envio_2 = Envio(distancia=810, cliente=cliente_2, seguro=False, paquete=paquete_2)

def test_valid_types():
    assert isinstance(envio, Envio)
    assert isinstance(paquete, Paquete)
    assert isinstance(cliente, Cliente)
    assert isinstance(calcular_pedido(envio), float) # 24.54
    assert isinstance(calcular_pedido(envio_2), int) # 1695

def test_valid_result():
    assert calcular_pedido(envio) == 24.54
    assert calcular_pedido(envio_2) == 1695