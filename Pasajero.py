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
        print("Nacionalidad:", self.nacionalidad)
        print("Número de maletas:", self.numero_maletas)
        print("Resumen información médica:", self.resumen_infomedica)
        print("Cédula:", self.cedula)
        print("Nombres:", self.nombres)
        print("Apellidos:", self.apellidos)
        print("Fecha de nacimiento:", self.fecha_de_nacimiento)
        print("Género:", self.genero)
        print("Dirección:", self.direccion)
        print("Número de teléfono:", self.numero_telefono)
        print("Correo:", self.correo)


class Tripulacion(Pasajero):
    def __init__(self, nacionalidad = "Colombiano", numero_maletas=2, resumen_infomedica="", cedula = 79752009, nombres="Alejandro", apellidos = "Garcia", fecha_de_nacimiento = "20/08/1994", genero = "Masculino", direccion = "Calle Pantera", numero_telefono = 3223295478, correo = "Alejandro@gmail.com", puesto = "Camarero", anios_experiencia = 0, cant_max_horas_diarias = 18):
        super().__init__(nacionalidad, numero_maletas, resumen_infomedica, cedula, nombres, apellidos, fecha_de_nacimiento, genero, direccion, numero_telefono, correo)
        self.puesto = puesto
        self.anios_experiencia = anios_experiencia
        self.cant_max_horas_diarias = cant_max_horas_diarias

    def imprimir_info_tripulacion(self):
        self.imprimirInfo()
        print("Puesto:", self.puesto)
        print("Años de experiencia:", self.anios_experiencia)
        print("Cantidad máxima de horas diarias:", self.cant_max_horas_diarias)
