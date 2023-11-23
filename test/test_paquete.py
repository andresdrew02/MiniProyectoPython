import sys
import os
import pytest
import uuid
# Agrego al path el directorio padre para poder acceder a las Clases
current_directory = os.path.dirname(__file__)
parent = os.path.dirname(current_directory)
sys.path.append(parent)

from clases.entidades import Paquete

def test_invalid_bool():
    with pytest.raises(ValueError):
        paquete = Paquete(fragil="True", peso=2)

def test_invalid_float():
    with pytest.raises(ValueError):
        paquete = Paquete(fragil=True, peso="2")

def test_valid():
    paquete = Paquete(fragil=True, peso=2)
    paquete_2 = Paquete(fragil=False, peso=2.5)
    assert isinstance(paquete, Paquete)
    assert isinstance(paquete_2, Paquete)

def test_uid():
    paquete = Paquete(fragil=False, peso=2.5)
    assert isinstance(paquete.id, uuid.UUID)