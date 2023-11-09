from model.Vuelo import *

class PuertaDeEmbarque:
    def __init__(self, id, ubi):
        self.vuelo_asignado = None
        self.disponible = True
        self.identificacion = id
        self.ubicacion = ubi
        self.hora_embarque = "Sin asignar"
        self.historial = []

    def get_vuelo_asignado(self):
        return self.vuelo_asignado

    def set_vuelo_asignado(self, vuelo):
        self.vuelo_asignado = vuelo

    def get_disponible(self):
        return self.disponible

    def set_disponible(self, dispo):
        self.disponible = dispo

    def get_identificacion(self):
        return self.identificacion

    def set_identificacion(self, id):
        self.identificacion = id

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubi):
        self.ubicacion = ubi

    def get_hora_embarque(self):
        return self.hora_embarque

    def set_hora_embarque(self, horaEmb):
        self.hora_embarque = horaEmb

    def get_historial(self):
        return self.historial

    def agregar_historial(self, vuelo):
        self.historial.append(vuelo)

    def agregar_historial(self, vuelo):
        self.historial.append(vuelo)

    def remover_historial(self):
        if self.historial:
            self.historial.pop()

    def imprimir_info(self):
        print(f"id: {self.identificacion} | ubicacion: {self.ubicacion} | disponible: {'Si' if self.disponible else 'No'}")
        if not self.disponible:
            print(f"  Id vuelo: {self.vuelo_asignado.numero_de_identificacion} | hora embarque: {self.hora_embarque}")

    def imprimir_historial(self):
        for i, vuelo in enumerate(self.historial, start=1):
            print(f"{i}. {vuelo.numero_de_identificacion} | {vuelo.ciudad_origen} - {vuelo.ciudad_destino}. Fecha: {vuelo.fecha}")
