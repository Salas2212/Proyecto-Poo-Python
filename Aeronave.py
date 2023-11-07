import random

id = 0

class Aeronave:
    
    def __init__(self, registro, capacidad, velMax, aut, yFabric, state):
        self.registro_de_marca = registro
        self.capacidad_de_pasajeros = capacidad
        self.velocidad_max = velMax
        self.autonomia = aut
        self.ano_fabricacion = yFabric
        self.asignacion = state # Disponible, En mantenimiento, totalmente asignada
        self.coordenadas = (0.0, 0.0)
        self.coor_aeronaves = []
        global id
        self.id = id
        id += 1
        self.numeroDeVuelosAsignados = 0
        self.sillas_restantes = capacidad
        self.tipo = ""
        self.vuelos_desde_cali = 0
        self.estado = "En espera" # estados disponibles: En espera, En puerta de embarque, En pista de Despegue, En vuelo

    def guardar_coordenadas(self):
        x = random.uniform(-100.0, 100.0)
        y = random.uniform(-100.0, 100.0)
        self.coordenadas = (x, y)

    def obtener_coordenadas(self):
        return self.coordenadas

    def consultar_coordenadas_aero(self, idAeronave, ubi_aeronave):
        self.coor_aeronaves[idAeronave] = ubi_aeronave

    def reiniciar(self, coordenadas_aeronaves):
        self.coor_aeronaves = coordenadas_aeronaves

    def agregar_aeronave_al_sistema(self):
        self.coor_aeronaves.append((-1, -1))

    def get_tipo(self):
        return self.tipo

    def imprimir_informacion_especifica(self):
        print("Información específica no disponible para esta aeronave.")

    def editar_informacion_especifica(self):
        print("Información específica no disponible para esta aeronave.")

    def disponible(self):
        return "Disponible" == self.asignacion and (self.estado == "En espera" or self.estado == "En puerta de embarque")

    def asignar_vuelo(self):
        self.numeroDeVuelosAsignados += 1
        if self.numeroDeVuelosAsignados == 3:
            self.asignacion = "Totalmente asignada"

    def asignar_silla(self):
        self.sillas_restantes -= 1

    def vaciar_aeronave(self):
        self.sillas_restantes = self.capacidad_de_pasajeros
        self.numeroDeVuelosAsignados -= 1
        self.vuelos_desde_cali -= 1
        self.asignacion = "Disponible"


class Avion(Aeronave):
    def __init__(self, registro = "ABC123", capacidad=300, velMax=10000, aut=50, yFabric=2010, state="Disponible", AltMax = 7000, cantMotores=2, category = "Comercial"):
        super().__init__(registro, capacidad, velMax, aut, yFabric, state)
        self.altitud_maxima = AltMax
        self.cantidad_de_motores = cantMotores
        self.categoria = category
        self.tipo = "Avion"

    def imprimir_informacion_especifica(self):
        print("Altitud máxima:", self.altitud_maxima)
        print("Cantidad de motores:", self.cantidad_de_motores)
        print("Categoría:", self.categoria)

    def editar_informacion_especifica(self):
        print("¿Qué característica deseas modificar?")
        print("1. Altitud máxima")
        print("2. Cantidad de motores")
        print("3. Categoría")
        ans = int(input())
        if ans == 1:
            self.altitud_maxima = int(input("Nueva altitud máxima: "))
        elif ans == 2:
            self.cantidad_de_motores = int(input("Nueva cantidad de motores: "))
        elif ans == 3:
            self.categoria = input("Nueva categoría: ")
        else:
            print("Opción no válida.")


class Helicoptero(Aeronave):
    def __init__(self, registro, capacidad, velMax, aut, yFabric, state, cantRotores, capacidadElevacion, usoEspecifico):
        super().__init__(registro, capacidad, velMax, aut, yFabric, state)
        self.cantidad_de_rotores = cantRotores
        self.capacidad_de_elevacion = capacidadElevacion
        self.uso_especifico = usoEspecifico
        self.tipo = "Helicoptero"

    def imprimir_informacion_especifica(self):
        print("Cantidad de rotores:", self.cantidad_de_rotores)
        print("Capacidad de elevación:", self.capacidad_de_elevacion)
        print("Uso específico:", self.uso_especifico)

    def editar_informacion_especifica(self):
        print("¿Qué característica deseas modificar?")
        print("1. Cantidad de rotores")
        print("2. Capacidad de elevación")
        print("3. Uso específico")
        ans = int(input())
        if ans == 1:
            self.cantidad_de_rotores = int(input("Nueva cantidad de rotores: "))
        elif ans == 2:
            self.capacidad_de_elevacion = int(input("Nueva capacidad de elevación: "))
        elif ans == 3:
            self.uso_especifico = input("Nuevo uso específico: ")
        else:
            print("Opción no válida.")


class JetPrivado(Aeronave):
    def __init__(self, registro, capacidad, velMax, aut, yFabric, state, owner, listaDeServiciosABordo, listaDeDestinosFrecuentes):
        super().__init__(registro, capacidad, velMax, aut, yFabric, state)
        self.propietario = owner
        self.lista_de_servicios_a_bordo = listaDeServiciosABordo
        self.lista_de_destinos_frecuentes = listaDeDestinosFrecuentes
        self.tipo = "JetPrivado"

    def imprimir_informacion_especifica(self):
        print("Propietario:", self.propietario)
        print("Lista de servicios a bordo:", self.lista_de_servicios_a_bordo)
        print("Lista de destinos frecuentes:", self.lista_de_destinos_frecuentes)

    def editar_informacion_especifica(self):
        print("¿Qué característica deseas modificar?")
        print("1. Propietario")
        print("2. Lista de servicios a bordo")
        print("3. Lista de destinos frecuentes")
        ans = int(input())
        if ans == 1:
            self.propietario = input("Nuevo propietario: ")
        elif ans == 2:
            self.lista_de_servicios_a_bordo = input("Nueva lista de servicios a bordo: ")
        elif ans == 3:
            self.lista_de_destinos_frecuentes = input("Nueva lista de destinos frecuentes: ")
        else:
            print("Opción no válida.")
