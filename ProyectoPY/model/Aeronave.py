import random
from view.streamlitFunctions import formulario, seleccionMultiple
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
        return "Información específica no disponible para esta aeronave.\n"

    def editar_informacion_especifica(self):
        return "Información específica no disponible para esta aeronave.\n"

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
        self.estado = "En espera"


class Avion(Aeronave):
    def __init__(self, registro = "ABC123", capacidad=300, velMax=10000, aut=50, yFabric=2010, state="Disponible", AltMax = 7000, cantMotores=2, category = "Comercial"):
        super().__init__(registro, capacidad, velMax, aut, yFabric, state)
        self.altitud_maxima = AltMax
        self.cantidad_de_motores = cantMotores
        self.categoria = category
        self.tipo = "Avion"

    def imprimir_informacion_especifica(self):
        ret = ''
        
        ret += f"Altitud máxima: {self.altitud_maxima}\n"
        ret += f"Cantidad de motores: {self.cantidad_de_motores}\n"
        ret += f"Categoría: {self.categoria}\n"
        return ret

    def editar_informacion_especifica(self):
        caracteristica = seleccionMultiple(["1. Altitud maxima", "2. Cantidad de motores", "3. Categoria"], 3, 'Que caracteristica deseas modificar?')
        if caracteristica == False:
            return False
        ans = int(caracteristica[0])
        nuevoValor = formulario(["Ingrese el nuevo valor: "], 4)
        if nuevoValor == False:
            return False
        if ans == 1:
            self.altitud_maxima = int(nuevoValor)
        elif ans == 2:
            self.cantidad_de_motores = int(nuevoValor)
        elif ans == 3:
            self.categoria = nuevoValor
        else:
            return "Opción no válida."
        return "Cambio realizado exitosamente."

class Helicoptero(Aeronave):
    def __init__(self, registro, capacidad, velMax, aut, yFabric, state, cantRotores, capacidadElevacion, usoEspecifico):
        super().__init__(registro, capacidad, velMax, aut, yFabric, state)
        self.cantidad_de_rotores = cantRotores
        self.capacidad_de_elevacion = capacidadElevacion
        self.uso_especifico = usoEspecifico
        self.tipo = "Helicoptero"

    def imprimir_informacion_especifica(self):
        ret = ''
        ret += f"Cantidad de rotores: {self.cantidad_de_rotores}\n"
        ret += f"Capacidad de elevación: {self.capacidad_de_elevacion}\n"
        ret += f"Uso específico: {self.uso_especifico}\n"
        return ret

    def editar_informacion_especifica(self):
        caracteristica = seleccionMultiple(["1. Cantidad de rotores", "2. Capacidad de elevacion", "3. Uso especifico"], 3, 'Que caracteristica deseas modificar?')
        if caracteristica == False:
            return False
        ans = int(caracteristica[0])
        nuevoValor = formulario(["Ingrese el nuevo valor: "], 4)
        if nuevoValor == False:
            return False
        if ans == 1:
            self.cantidad_de_rotores = int(nuevoValor)
        elif ans == 2:
            self.capacidad_de_elevacion = int(nuevoValor)
        elif ans == 3:
            self.uso_especifico = nuevoValor
        else:
            return "Opción no válida."
        return "Cambio realizado exitosamente."


class JetPrivado(Aeronave):
    def __init__(self, registro, capacidad, velMax, aut, yFabric, state, owner, listaDeServiciosABordo, listaDeDestinosFrecuentes):
        super().__init__(registro, capacidad, velMax, aut, yFabric, state)
        self.propietario = owner
        self.lista_de_servicios_a_bordo = listaDeServiciosABordo
        self.lista_de_destinos_frecuentes = listaDeDestinosFrecuentes
        self.tipo = "JetPrivado"

    def imprimir_informacion_especifica(self):
        ret = ''
        ret += f"Propietario: {self.propietario}\n"
        ret += f"Lista de servicios a bordo: {self.lista_de_servicios_a_bordo}\n"
        ret += f"Lista de destinos frecuentes: {self.lista_de_destinos_frecuentes}\n"
        return ret

    def editar_informacion_especifica(self):
        caracteristica = seleccionMultiple(["1. Propietario", "2. Lista de servicios a bordo", "3. Lista de destinos frecuentes"], 3, 'Que caracteristica deseas modificar?')
        if caracteristica == False:
            return False
        ans = int(caracteristica[0])
        nuevoValor = formulario(["Ingrese el nuevo valor: "], 4)
        if nuevoValor == False:
            return False
        if ans == 1:
            self.propietario = nuevoValor
        elif ans == 2:
            self.lista_de_servicios_a_bordo = nuevoValor
        elif ans == 3:
            self.lista_de_destinos_frecuentes = nuevoValor
        else:
            return "Opción no válida."
        return "Cambio realizado exitosamente."
