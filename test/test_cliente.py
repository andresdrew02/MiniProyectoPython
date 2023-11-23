import sys
import os
import pytest
import uuid
# Agrego al path el directorio padre para poder acceder a las Clases
current_directory = os.path.dirname(__file__)
parent = os.path.dirname(current_directory)
sys.path.append(parent)

from clases.entidades import Cliente

def exec_tests():
    all_functions = globals()
    for name in all_functions:
        if name.startswith("test_"):
            all_functions[name]()

def test_null_name():
    with pytest.raises(ValueError):
        cliente = Cliente(None, "Gonzalez")
    with pytest.raises(ValueError):
        cliente = Cliente("", "Gonzalez")

def test_null_lastname():
    with pytest.raises(ValueError):
        cliente = Cliente("Pepe", None)
    with pytest.raises(ValueError):
        cliente = Cliente("Pepe", "")
    
def test_default_vip():
    cliente = Cliente("Pepe", "Gonzalez")
    assert cliente.vip == False

def test_invalid_vip():
    with pytest.raises(ValueError):
        cliente = Cliente("Pepe", "Gonzalez", "True")
    
def test_trimmed_name_lastname():
    cliente = Cliente("  Pepe  ", "Gonzalez    ")
    assert cliente.nombre == "Pepe"
    assert cliente.apellidos == "Gonzalez"

def test_uid():
    cliente = Cliente("Pepe", "Gonzalez")
    assert isinstance(cliente.id, uuid.UUID)