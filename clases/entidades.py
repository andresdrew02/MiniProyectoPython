from uuid import uuid4

class Envio:
    def __init__(self, distancia, cliente, seguro, paquete):
        self.id = uuid4()
        self.distancia = distancia
        self.cliente = cliente
        self.seguro = seguro
        self.paquete = paquete
        if (not Envio.__checkTypes(self)):
            raise ValueError("Comprueba los datos del envio")

    def __str__(self):
        return f'Envio: distancia={self.distancia}, cliente={self.cliente}, seguro={self.seguro}, paquete={self.paquete}'

    @staticmethod
    def __checkTypes(envio):
        if (isinstance(envio.distancia, float) or isinstance(envio.distancia,int)) and isinstance(envio.cliente, Cliente) and isinstance(envio.seguro, bool) and isinstance(envio.paquete, Paquete):
            if envio.distancia > 0:
                return True
            return False
        else:
            return False

class Cliente:
    def __init__(self, nombre: str, apellidos: str, vip=False):
        self.id = uuid4()
        self.nombre = nombre
        self.apellidos = apellidos
        self.vip = vip
        if (not Cliente.__checkTypes(self)):
            raise ValueError("Comprueba los datos del cliente")
        self.nombre = self.nombre.strip()
        self.apellidos = self.apellidos.strip()

    def __str__(self):
        return f'Cliente: nombre={self.nombre}, apellidos={self.apellidos}, vip={self.vip}'

    @staticmethod
    def __checkTypes(cliente):
        if isinstance(cliente.nombre, str) and isinstance(cliente.apellidos, str) and isinstance(cliente.vip, bool):
            if len(cliente.nombre) > 0 and len(cliente.apellidos) > 0:
                return True
            return False
        else:
            return False

class Paquete:
    def __init__(self, fragil, peso):
        self.id = uuid4()
        self.fragil = fragil
        self.peso = peso
        if (not Paquete.__checkTypes(self)):
            raise ValueError("Comprueba los datos del paquete")
        

    def __str__(self):
        return f'Paquete: fragil={self.fragil}, peso={self.peso}'

    @staticmethod
    def __checkTypes(paquete):
        if isinstance(paquete.fragil, bool) and (isinstance(paquete.peso, float) or isinstance(paquete.peso, int)):
            if paquete.peso > 0:
                return True
            return False
        else:
            return False