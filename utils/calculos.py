from clases.entidades import Envio

    #Cada kg de peso del paquete son 5€.
    #Cada kilómetro de distancia son 2€.
    #Si son clientes VIP quieren hacer un descuento del 15% en el coste total del envío.
    #Si eligen el servicio de seguro de envío, se le añade un coste adicional de 5%
    #Si el paquete es frágil, le añadimos un coste adicional de 10€
def calcular_pedido(envio: Envio) -> float:
    precio_envio = envio.paquete.peso * 5 + envio.distancia * 2 + (10 if envio.paquete.fragil else 0)
    precio_envio += 5*precio_envio/100 if envio.seguro else 0
    descuento_vip = 15*precio_envio/100 if envio.cliente.vip else 0
    return round(precio_envio - descuento_vip, 2)