import sys
import os
import pytest
import uuid
# Agrego al path el directorio padre para poder acceder a las Clases
current_directory = os.path.dirname(__file__)
parent = os.path.dirname(current_directory)
sys.path.append(parent)

from clases.entidades import *

cliente = Cliente("Pepe", "Gonzalez", vip=True)
paquete = Paquete(fragil=True, peso=2)

def test_invalid_distance():
    with pytest.raises(ValueError):
        envio = Envio(distancia=-1, cliente=cliente, seguro=True, paquete=paquete)

def test_invalid_client():
    with pytest.raises(ValueError):
        envio = Envio(distancia=1, cliente=None, seguro=True, paquete=paquete)

def test_invalid_package():
    with pytest.raises(ValueError):
        envio = Envio(distancia=1, cliente=cliente, seguro=True, paquete=None)

def test_invalid_seguro():
    with pytest.raises(ValueError):
        envio = Envio(distancia=1, cliente=cliente, seguro=None, paquete=paquete)

def test_valid():
    envio = Envio(distancia=1, cliente=cliente, seguro=True, paquete=paquete)
    envio_2 = Envio(distancia=1.25, cliente=cliente, seguro=False, paquete=paquete)
    assert isinstance(envio, Envio)
    assert isinstance(envio_2, Envio)

def test_uid():
    envio = Envio(distancia=1, cliente=cliente, seguro=True, paquete=paquete)
    assert isinstance(envio.id, uuid.UUID)