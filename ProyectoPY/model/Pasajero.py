class Pasajero:
    def __init__(self, nacionalidad = "Colombiano", numero_maletas=2, resumen_infomedica="", cedula = 79752009, nombres="Alejandro", apellidos = "Garcia", fecha_de_nacimiento = "20/08/1994", genero = "Masculino", direccion = "Calle Pantera", numero_telefono = 3223295478, correo = "Alejandro@gmail.com"):
        self.nacionalidad = nacionalidad
        self.numero_maletas = numero_maletas
        self.resumen_infomedica = resumen_infomedica
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.genero = genero
        self.direccion = direccion
        self.numero_telefono = numero_telefono
        self.correo = correo
        self.NoVuelo = ""

    def setVuelo(self, vuelo):
        self.NoVuelo = vuelo

    def obtener_numero_maletas(self):
        return self.numero_maletas

    def poner_numero_maletas(self, numeroMaletas):
        self.numero_maletas = numeroMaletas

    def imprimir_info(self):
        ret = ''

        ret += f"Nacionalidad: {self.nacionalidad}\n"
        ret += f"Número de maletas: {self.numero_maletas}\n"
        ret += f"Resumen información médica: {self.resumen_infomedica}\n"
        ret += f"Cédula: {self.cedula}\n"
        ret += f"Nombres: {self.nombres}\n"
        ret += f"Apellidos: {self.apellidos}"
        ret += f"Fecha de nacimiento: {self.fecha_de_nacimiento}\n"
        ret += f"Género: {self.genero}\n"
        ret += f"Dirección: {self.direccion}\n"
        ret += f"Número de teléfono: {self.numero_telefono}\n"
        ret += f"Correo: {self.correo}\n"
        return ret


class Tripulacion(Pasajero):
    def __init__(self, nacionalidad = "Colombiano", numero_maletas=2, resumen_infomedica="", cedula = 79752009, nombres="Alejandro", apellidos = "Garcia", fecha_de_nacimiento = "20/08/1994", genero = "Masculino", direccion = "Calle Pantera", numero_telefono = 3223295478, correo = "Alejandro@gmail.com", puesto = "Camarero", anios_experiencia = 0, cant_max_horas_diarias = 18):
        super().__init__(nacionalidad, numero_maletas, resumen_infomedica, cedula, nombres, apellidos, fecha_de_nacimiento, genero, direccion, numero_telefono, correo)
        self.puesto = puesto
        self.anios_experiencia = anios_experiencia
        self.cant_max_horas_diarias = cant_max_horas_diarias

    def imprimir_info_tripulacion(self):
        ret = self.imprimirInfo()
        ret += f"Puesto: {self.puesto}\n"
        ret += f"Años de experiencia: {self.anios_experiencia}\n"
        ret += f"Cantidad máxima de horas diarias: {self.cant_max_horas_diarias}\n"
        return ret
