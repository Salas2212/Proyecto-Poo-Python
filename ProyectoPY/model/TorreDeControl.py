# TorreDeControl.py
from model.Vuelo import *
from model.Aeronave import *
from model.PuertaDeEmbarque import PuertaDeEmbarque

import random
from datetime import datetime
from functools import cmp_to_key # Para poder ordenar vuelos de acuerdo a su fecha

def fecha1_menor_que_fecha2(fecha1, fecha2):
        # Devuelve True si fecha1 es antes que fecha2
        formato = "%d/%m/%Y"  # Formato para parsear la fecha
        fecha1 = datetime.strptime(fecha1, formato)
        fecha2 = datetime.strptime(fecha2, formato)
        return fecha1 < fecha2
def hora1_menor_que_hora2(hora1, hora2):
    formato_hora = "%H:%M"

    tiempo1 = datetime.strptime(hora1, formato_hora)
    tiempo2 = datetime.strptime(hora2, formato_hora)
    return tiempo1 < tiempo2

def comparadorFechas(tuplaA, tuplaB):
    if fecha1_menor_que_fecha2(tuplaA[0], tuplaB[0]):
        return -1
    else:
        return 1
def comparadorHoras(tuplaA, tuplaB):
    if hora1_menor_que_hora2(tuplaA[0], tuplaB[0]):
        return -1
    else:
        return 1



class TorreDeControl:
    def __init__(self, numero_de_puertas_embarque):
        self.coordenadas_aeronaves = []
        self.puertas_embarques = []
        self.vuelos = []
        self.aero = []
        self.disponibilidad_pista_de_despegue = True
        self.vuelo_por_despegar = None
        self.aeronave_por_despegar = None
        '''
         Para simular el sistema, se decidio que 1/3 de las puertas serian para vuelos nacionales
        y otras para internacionales.
        '''
        for i in range(numero_de_puertas_embarque):
            ubic = "Vuelos Nacionales" if i < numero_de_puertas_embarque / 3 else "Vuelos Internacionales"
            nueva = PuertaDeEmbarque(i, ubic)
            self.puertas_embarques.append(nueva)

    def actualizar_ubi_aero(self, id):
        self.coordenadas_aeronaves[id] = self.aero[id].obtener_coordenadas()
        for i in range(len(self.aero)):
            self.aero[i].consultar_coordenadas_aero(id, self.aero[id].obtener_coordenadas())

    def obtener_ubi(self, id):
        return self.coordenadas_aeronaves[id]

    def agregar_aeronave(self, nueva_aeronave):
        nueva_aeronave.id = len(self.aero)
        nueva_aeronave.guardar_coordenadas()
        self.aero.append(nueva_aeronave)
        self.coordenadas_aeronaves.append((0, 0))
        for i in range(len(self.aero)):
            self.aero[i].agregar_aeronave_al_sistema()
        for i in range(len(self.aero) - 1):
            self.aero[-1].agregar_aeronave_al_sistema()
        self.aero[-1].reiniciar(self.coordenadas_aeronaves)
        self.actualizar_ubi_aero(len(self.aero) - 1)

    def actualizar_todas_las_aeronaves(self):
        for i in range(len(self.aero)):
            self.aero[i].guardar_coordenadas()
            self.coordenadas_aeronaves[i] = self.aero[i].coordenadas
        for i in range(len(self.aero)):
            self.aero[i].reiniciar(self.coordenadas_aeronaves)

    def buscar_aeronave_por_id(self, id):
        for i in range(len(self.aero)):
            if self.aero[i].id == id:
                return i

    def asignar_puertas(self, flight):
        cual_puerta = None
        hay_disponibilidad, cual_puerta = self.hay_puertas_disponibles()
        if not hay_disponibilidad:
            print("El vuelo no fue asignado pues no hay puertas Disponibles")
            return -1
        else:
            flight.puerta_embarque = cual_puerta
            self.puertas_embarques[cual_puerta].set_disponible(False)
            hora = random.randint(0, 23)
            minuto = random.randint(0, 59)
            result = f"{hora}:{minuto}"
            self.puertas_embarques[cual_puerta].set_hora_embarque(result)
            self.puertas_embarques[cual_puerta].set_vuelo_asignado(flight)
            self.puertas_embarques[cual_puerta].agregar_historial(flight)
            self.aero[self.buscar_aeronave_por_id(flight.idAeronave)].estado = "En puerta de embarque"
            return cual_puerta

    def asignar_todas_las_puertas(self):
        todosLosVuelos = []
        for i in range(len(self.vuelos)):
            if self.vuelos[i].puerta_embarque != -1 or self.vuelos[i].ciudad_origen != 'Cali':
                continue
            todosLosVuelos.append([self.vuelos[i].fecha, i])
        
        todosLosVuelos.sort( key=cmp_to_key(comparadorFechas) )
        while(not len(todosLosVuelos) == 0):
            resultado = self.asignar_puertas(self.vuelos[todosLosVuelos[-1][1]])
            if resultado != -1:
                print(f"\n\n[Informacion del sistema: La puerta {resultado} fue asignada al vuelo {self.vuelos[todosLosVuelos[-1][1]].numero_de_identificacion}]\n\n")
                todosLosVuelos.pop()                    
            else:
                break


    def desocupar_puerta(self, cual_puerta):
        self.puertas_embarques[cual_puerta].set_disponible(True)
        self.puertas_embarques[cual_puerta].set_vuelo_asignado(None)
        self.puertas_embarques[cual_puerta].set_hora_embarque("Sin asignar")

    def hay_puertas_disponibles(self):
        hay_disponibilidad = False
        cual_puerta = 0
        for i in range(len(self.puertas_embarques)):
            if self.puertas_embarques[i].disponible:
                hay_disponibilidad = True
                cual_puerta = i
                break
        return hay_disponibilidad, cual_puerta

    def hay_aeronaves_disponibles(self, from_cali = False):
        hay_disponibilidad = False
        numero_de_aeronave_disponible = 0
        for i in range(len(self.aero)):
            if self.aero[i].disponible() and (not from_cali or self.aero[i].vuelos_desde_cali == 0):
                hay_disponibilidad = True
                numero_de_aeronave_disponible = i
                break
        return hay_disponibilidad, numero_de_aeronave_disponible

    def pista_disponible(self):
        return self.disponibilidad_pista_de_despegue
    def despegar(self):
        self.vuelo_por_despegar.puerta_embarque = "En vuelo"
        self.aeronave_por_despegar.estado = "En vuelo"
        print(f"\n\n[Informacion del sistema: El vuelo {self.vuelo_por_despegar.numero_de_identificacion} hacia {self.vuelo_por_despegar.ciudad_destino} ha despegado]\n\n")
        self.aeronave_por_despegar.guardar_coordenadas()
        self.disponibilidad_pista_de_despegue = True
        self.vuelo_por_despegar = None
        self.aeronave_por_despegar = None
        
    def usar_pista_de_despegue(self):
        todosLosVuelos = []

        for i in range(len(self.puertas_embarques)):
            if(not self.puertas_embarques[i].disponible):
                todosLosVuelos.append([self.puertas_embarques[i].hora_embarque, i])
        todosLosVuelos.sort( key=cmp_to_key(comparadorHoras))
        if not len(todosLosVuelos) == 0:
            vuelo = self.puertas_embarques[todosLosVuelos[0][1]].vuelo_asignado
            idAeronave = vuelo.idAeronave
            idxAeronave = None
            for i in range(len(self.aero)):
                if self.aero[i].id == idAeronave:
                    self.aero[i].estado = "En pista de Despegue"
                    idxAeronave = i
                    break
            vuelo.puerta_embarque = "En pista de Despegue"
            
            self.vuelo_por_despegar = vuelo
            print(f"\n\n[Informacion del sistema: El vuelo {self.vuelo_por_despegar.numero_de_identificacion} hacia {self.vuelo_por_despegar.ciudad_destino} se encuentra en pista de despegue]\n\n")
            self.aeronave_por_despegar = self.aero[idxAeronave]
            self.disponibilidad_pista_de_despegue = False
            self.desocupar_puerta(todosLosVuelos[0][1])
    def ver_coordenadas_aeronaves(self):
        ret = "Las coordenadas de las aeronaves son: \n"
        for aeronave in self.aero:
            if aeronave.estado == "En vuelo":
                ret += f'{aeronave.id}. Coordenadas: {aeronave.obtener_coordenadas()}\n'
        return ret





    
