from model.Pasajero import *

class Vuelo:
    def __init__(self, num_identificacion="", fecha_vuelo="", origen="", destino="", puerta=0):
        self.tripulacion = []
        self.pasajeros = []
        self.numero_de_identificacion = num_identificacion
        self.fecha = fecha_vuelo
        self.ciudad_origen = origen
        self.ciudad_destino = destino
        self.puerta_embarque = puerta
        self.idAeronave = 0

    def agregar_tripulante(self, tripulante):
        self.tripulacion.append(tripulante)

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)
    def disponible_para_compra(self):
        return self.puerta_embarque != "En vuelo" and self.puerta_embarque != "En pista de Despegue"
