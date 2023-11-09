#include "Pasajero.h"
#include "Aeronave.h"
#include "Vuelo.h"
#include "PuertaDeEmbarque.h"
#include "TorreDeControl.h"
from model.Pasajero import *
from model.Aeronave import *
from model.Vuelo import *
from model.PuertaDeEmbarque import *
from model.TorreDeControl import *
import random
import time



class SistemaPrincipal:
    def __init__(self, numero_de_puertas_de_embarque: int):
        self.torre_principal = TorreDeControl(numero_de_puertas_de_embarque)
        self.vuelos = self.torre_principal.vuelos
        self.tripulacion = []
        self.aeronaves = self.torre_principal.aero
        self.password = 'aeropuerto'
        self.contadorAcciones = 0

    def get_cantidad_aeronaves(self):
        return len(self.aeronaves)

    
        
    def actualizar_torre_de_control(self):
        
        self.contadorAcciones += 1
        if self.contadorAcciones % 5 == 0 : 
            if not self.torre_principal.pista_disponible():
                # Si la pista de despegue esta ocupada.
                self.torre_principal.despegar()
        if self.contadorAcciones % 3 == 0 and self.torre_principal.disponibilidad_pista_de_despegue:
            self.torre_principal.usar_pista_de_despegue()


        if self.torre_principal.hay_puertas_disponibles()[0] and not len(self.vuelos) == 0:
            # Llenamos las puertas de embarque que se encuentran disponibles, con vuelos segun su fecha.
            self.torre_principal.asignar_todas_las_puertas()

        
            
        


    def obtener_info_aeronave(self, idx):
        if 0 <= idx < len(self.aeronaves):
            aeronave = self.aeronaves[idx]
            print(f"Registro de marca: {aeronave.registro_de_marca}")
            print(f"Capacidad de pasajeros: {aeronave.capacidad_de_pasajeros}")
            print(f"Velocidad máxima: {aeronave.velocidad_max}")
            print(f"Autonomía: {aeronave.autonomia}")
            print(f"Año de fabricación: {aeronave.ano_fabricacion}")
            print(f"Asignacion: {aeronave.asignacion}")
            print(f"Estado: {aeronave.estado}")
            print(f"Coordenadas: ({aeronave.coordenadas[0]}, {aeronave.coordenadas[1]})")

            print("\nInformación específica:")
            print(f"Tipo = {aeronave.get_tipo()}")
            aeronave.imprimir_informacion_especifica()
        else:
            print("Índice de aeronave fuera de rango.")

    '''
    def seleccion_menu(self):
        print("\nSeleccione la acción que desea realizar:")
        print("1. Comprar un vuelo.")
        print("2. Consultar puertas de embarque.")
        print("3. Consultar vuelos.")
        print("4. Ver opciones de administrador")
        print("0. Salir")
        ans = int(input())
        
        if ans == 0:
            return 0
        elif ans == 4:
            if not self.admin():
                return -1
            print("\n\nSeleccione la acción que desea realizar:")
            print("5. Agregar una nave.")
            print("6. Consultar información de las naves.")
            print("7. Editar la información de una nave.")
            print("8. Generar un vuelo.")
            print("9. Ingresar una tripulación al sistema.")
            print("10. Consultar tripulaciones")
            print("11. Consultar historial de una puerta de embarque")
            print("12. Finalizar un vuelo") # ! cambio importante.
            print("13. Realizar mantenimiento Aeronave")
            print("14. Ver coordenadas Aeronaves.")
            print("0. Atrás")
            ans = int(input())
            if ans < 5 or ans > 14:
                return -1
            return ans
        elif ans > 4 or ans < 1:
            return -1
        return ans
    '''


    def comprar_un_vuelo(self):
        if not self.hay_vuelos_disponibles():
            return "Por el momento, no hay vuelos disponibles :("
            return

        print("Para comprar un vuelo debe iniciar sesión.")
        print("Vamos a crear tu perfil.")
        usuario = self.crear_pasajero()
        print("\n" * 2)
        print("Vale, ahora selecciona el vuelo que deseas comprar:")
        self.consultar_vuelos(False, True)
        
        while True:
            ans = int(input("(Digita el número al principio del vuelo, o digita -1 para cancelar)\n"))
            if ans == -1:
                return
            if 0 <= ans < len(self.vuelos):
                if self.aeronaves[self.vuelos[ans].id_aeronave].sillas_restantes <= 0:
                    print("Este vuelo está completo. Por favor selecciona otro.")
                elif not self.vuelos[ans].disponible_para_compra:
                    print("Este vuelo ya no se encuentra disponible. Por favor seleccione otro.")
                else:
                    break
        
        self.aeronaves[self.vuelos[ans].id_aeronave].asignar_silla()
        self.vuelos[ans].agregar_pasajero(usuario)
        print("Compra realizada exitosamente.")


    def consultar_puertas_de_embarque(self):
        for puerta_embarque in self.torre_principal.puertas_embarques:
            puerta_embarque.imprimir_info()
            print()

    def consultar_vuelos(self, expandible, imprimir_sillas):
        if not self.hay_vuelos_disponibles(False):
            print("Por el momento, no hay vuelos disponibles :(")
            return

        print(f"Existen {len(self.vuelos)} vuelos disponibles:")
        for i, vuelo in enumerate(self.vuelos):
            if not vuelo.disponible_para_compra() and imprimir_sillas:
                continue
            print(f"{i}. {vuelo.numero_de_identificacion} | {vuelo.ciudad_origen}-{vuelo.ciudad_destino}")
            puerta = vuelo.puerta_embarque
            if puerta == -1:
                print(f"Fecha: {vuelo.fecha}. Puerta de embarque: Sin definir. ")
            elif puerta == "En vuelo":
                print(f"Fecha: {vuelo.fecha}. En vuelo.")
            elif puerta == "En pista de Despegue":
                print(f"Fecha: {vuelo.fecha}. En pista de despegue")
            else: 
                print(f"Fecha: {vuelo.fecha}. Puerta de embarque: {puerta} ({self.torre_principal.puertas_embarques[vuelo.puerta_embarque].get_ubicacion()}).")
            if imprimir_sillas:
                print(f"Sillas disponibles: {self.aeronaves[vuelo.id_aeronave].sillas_restantes}")

        if not expandible or not self.vuelos:
            return

        print("Si desea consultar información adicional sobre vuelos en específico, deberá iniciar sesión")
        ans = input("Desea continuar? (S/N)\n")
        if ans != 'S':
            return
        if not self.admin():
            return
        idx = int(input("Digite el número del vuelo entre las opciones dadas\n"))
        if 0 <= idx < len(self.vuelos):
            print(f"Vuelo {idx} escogido.")
            print(f"id de la aeronave: {self.vuelos[idx].id_aeronave}")
            print("Tripulación:")
            for tripulante in self.vuelos[idx].tripulacion:
                print(f"{tripulante.cedula} - {tripulante.nombres} {tripulante.apellidos}")
            print("Pasajeros:")
            for pasajero in self.vuelos[idx].pasajeros:
                print(f"{pasajero.nombres} {pasajero.apellidos}. Maletas: {pasajero.numero_maletas}")
        else:
            print("Opción no válida")


    def construir_aeronave(self):
        ans = input("Desea construir una Aeronave con atributos por defecto? (S/N)")
        if ans == 'S':
            avion = Avion()
            self.torre_principal.agregar_aeronave(avion)
            return 
        registro = input("Ingrese el registro de la Aeronave: ")
        capacidad = int(input("Ingrese la capacidad de pasajeros: "))
        vel_max = int(input("Ingrese la velocidad máxima: "))
        aut = int(input("Ingrese la autonomía: "))
        y_fabric = int(input("Ingrese el año de fabricación: "))
        
        state = "Disponible"

        print("¿Qué tipo de aeronave deseas construir? (Avion, Helicoptero, JetPrivado)")
        respuesta = input()

        if respuesta == "Avion":
            altitud_maxima = int(input("Ingrese la altitud máxima: "))
            cantidad_motores = int(input("Ingrese la cantidad de motores: "))
            categoria = input("Ingrese la categoría: ")

            avion = Avion(registro, capacidad, vel_max, aut, y_fabric, state, altitud_maxima, cantidad_motores, categoria)
            self.torre_principal.agregar_aeronave(avion)
        elif respuesta == "Helicoptero":
            cantidad_rotores = int(input("Ingrese la cantidad de rotores: "))
            capacidad_elevacion = int(input("Ingrese la capacidad de elevación: "))
            uso_especifico = input("Ingrese el uso específico: ")

            helicoptero = Helicoptero(registro, capacidad, vel_max, aut, y_fabric, state, cantidad_rotores, capacidad_elevacion, uso_especifico)
            self.torre_principal.agregar_aeronave(helicoptero)
        elif respuesta == "JetPrivado":
            propietario = input("Ingrese el propietario: ")
            lista_servicios_abordo = input("Ingrese la lista de servicios a bordo: ")
            lista_destinos_frecuentes = input("Ingrese la lista de destinos frecuentes: ")

            jet_privado = JetPrivado(registro, capacidad, vel_max, aut, y_fabric, state, propietario, lista_servicios_abordo, lista_destinos_frecuentes)
            self.torre_principal.agregar_aeronave(jet_privado)
        else:
            print("Tipo no válido!")


    def consultar_informacion_aeronaves(self):
        if not self.aeronaves:
            print("Hasta ahora, no hay ninguna aeronave registrada en el sistema.")
            return

        print(f"Existen {len(self.aeronaves)} aeronaves registradas en el sistema.")
        idx = int(input(f"Digite el número de la aeronave que desea consultar (1 - {len(self.aeronaves)}): ")) - 1
        self.obtener_info_aeronave(idx)
    
    
    

    def editar_informacion_aeronave(self, i = None):
        if i is None:
            if(len(self.aeronaves) == 0):
                print("Hasta ahora, no hay ninguna aeronave registrada en el sistema.")
                return 
            print(f"Existen {len(self.aeronaves)} aeronaves registradas en el sistema.")
            print(f"Digite el numero de la aeronave que desea consultar ( 1 - {len(self.aeronaves)} ): ")
            idx = int(input())
            idx -= 1
            self.editar_informacion_aeronave(idx)
            return 
        if 0 <= i < len(self.aeronaves):
            print("¿Qué característica deseas modificar?")
            print("1. Registro de marca")
            print("2. Capacidad de pasajeros")
            print("3. Velocidad máxima")
            print("4. Autonomía")
            print("5. Año de fabricación")
            #print("6. Asignacion")
            print("6. Modificar atributos específicos")
            print("7. Cancelar")
            opcion = int(input())

            if opcion == 1:
                self.aeronaves[i].registro_de_marca = input("Nuevo registro de marca: ")
            elif opcion == 2:
                self.aeronaves[i].capacidad_de_pasajeros = int(input("Nueva capacidad de pasajeros: "))
            elif opcion == 3:
                self.aeronaves[i].velocidad_max = int(input("Nueva velocidad máxima: "))
            elif opcion == 4:
                self.aeronaves[i].autonomia = int(input("Nueva autonomía: "))
            elif opcion == 5:
                self.aeronaves[i].ano_fabricacion = int(input("Nuevo año de fabricación: "))
            elif opcion == 6:
                # Modifica atributos específicos según el tipo de aeronave
                self.aeronaves[i].editar_informacion_especifica()
            elif opcion == 7:
                print("Operación cancelada.")
            else:
                print("Opción no válida.")
        else:
            print("Índice de aeronave fuera de rango.")

    def generar_vuelo(self):
        
        print("Digite la ciudad de origen")
        nuevo_vuelo = Vuelo()
        nuevo_vuelo.ciudad_origen = input()
        es_de_cali = nuevo_vuelo.ciudad_origen == 'Cali'
       
        disp_aeronaves, aeronave_disponible = self.torre_principal.hay_aeronaves_disponibles(es_de_cali)
        #disp_puertas, puerta_disponible = self.torre_principal.hay_puertas_disponibles()

        if not disp_aeronaves or not self.tripulacion:
            print("ERROR:")
            if not disp_aeronaves:
                print("No hay aeronaves disponibles por el momento.")
            if not self.tripulacion:
                print("No hay tripulaciones registradas en el sistema.")
            return
        
        
        
        print("Digite la ciudad de destino")
        nuevo_vuelo.ciudad_destino = input()
        
        formato = "%d/%m/%Y"  # Formato para parsear la fecha
        var = True
        while(var):
            print("Digite la fecha del vuelo")
            var = False
            nuevo_vuelo.fecha = input()
            try:
                fecha = datetime.strptime(nuevo_vuelo.fecha, formato)
            except ValueError:
                print("La fecha esta escrita incorrectamente. Por favor digitela en el formato dd/mm/yy")
                var = True

        
        if len(nuevo_vuelo.ciudad_destino) < 2 or len(nuevo_vuelo.ciudad_origen) < 2 or len(nuevo_vuelo.fecha) < 2:
            print("La información dada no es válida")
            return

        # Generar un ID único para el vuelo
        id = nuevo_vuelo.ciudad_origen[:2] + nuevo_vuelo.ciudad_destino[:2] + nuevo_vuelo.fecha[:2]
        id += str(random.randint(0, 99999)).zfill(5)
        nuevo_vuelo.numero_de_identificacion = id

        print("Las aeronaves disponibles son:")
        for i, aeronave in enumerate(self.aeronaves):
            if aeronave.disponible() and (not es_de_cali or aeronave.vuelos_desde_cali == 0):
                print(f"{i}. {aeronave.get_tipo()} | autonomía: {aeronave.autonomia} | capacidad de pasajeros: {aeronave.capacidad_de_pasajeros}")

        print("Por favor, digite el número de la aeronave a usar. (Para cancelar, digite -1)")
        valid = False
        ans_aero = -1
        while not valid:
            ans_aero = int(input())
            if ans_aero == -1:
                return
            if 0 <= ans_aero < len(self.aeronaves) and self.aeronaves[ans_aero].disponible()and (not es_de_cali or aeronave.vuelos_desde_cali == 0):
                valid = True
            else:
                print("El número digitado no corresponde a una opción")

        print(f"Se ha escogido la aeronave {ans_aero}:")
        self.obtener_info_aeronave(ans_aero)
        print("\n")

        print(f"Existen {len(self.tripulacion)} tripulaciones registradas en el sistema:")
        for i, tripulante in enumerate(self.tripulacion):
            print(f"{i+1}: {tripulante.apellidos}: Cantidad máxima de horas: {tripulante.cant_max_horas_diarias}")

        print("Digite los códigos de los tripulantes a agregar separados por enter:")
        print("Si no desea agregar más, digite 0")
        agregados = set()
        ans = -1
        while ans != 0:
            ans = int(input())
            if ans in agregados:
                print("Este tripulante ya fue agregado!")
            elif ans < 0 or ans > len(self.tripulacion):
                print("Opción inválida")
            elif ans != 0:
                nuevo_vuelo.agregar_tripulante(self.tripulacion[ans-1])
                self.tripulacion[ans-1].NoVuelo = nuevo_vuelo.numero_de_identificacion
                agregados.add(ans)
                print("Agregado!")

        nuevo_vuelo.puerta_embarque = -1
        nuevo_vuelo.id_aeronave = self.aeronaves[ans_aero].id
        if es_de_cali:
            self.aeronaves[ans_aero].vuelos_desde_cali += 1
        self.aeronaves[ans_aero].asignar_vuelo()
        self.vuelos.append(nuevo_vuelo)
        print("Vuelo generado con éxito.")

    def agregar_tripulacion_al_sistema(self):
        creado = self.crear_tripulacion()
        self.tripulacion.append(creado)
        print("Tripulación guardada exitosamente")

    def crear_pasajero(self):
        print("Desea usar datos guardados en las cookies? (S/N)")
        ans = input()
        if ans == 'S':
            return self.pasajero_precreado()

        pasajero = Pasajero()

        print("Ingrese la nacionalidad:")
        pasajero.nacionalidad = input()

        print("Ingrese el número de maletas:")
        pasajero.numero_maletas = int(input())

        print("Ingrese el URL a su información médica:")
        pasajero.resumen_infomedica = input()

        print("Ingrese el número de su cédula:")
        pasajero.cedula = input()

        print("Ingrese su Nombre (solo uno):")
        pasajero.nombres = input()

        print("Ingrese su apellido (solo uno):")
        pasajero.apellidos = input()

        print("Ingrese el número de su fecha de nacimiento:")
        pasajero.fecha_de_nacimiento = input()

        print("Ingrese su género:")
        pasajero.genero = input()

        print("Ingrese su dirección:")
        pasajero.direccion = input()

        print("Ingrese su número de teléfono:")
        pasajero.numero_telefono = input()

        print("Ingrese su correo:")
        pasajero.correo = input()

        return pasajero


    def pasajero_precreado(self):
        pasajero = Pasajero()
        pasajero.nacionalidad = "Colombiano"
        pasajero.numero_maletas = 2
        pasajero.resumen_infomedica = "https://www.mayoclinic.org/es/first-aid/emergency-health-information/basics/art-20134333"
        pasajero.cedula = 1023216346
        pasajero.nombres = "Juan"
        pasajero.apellidos = "Mendoza"
        pasajero.fecha_de_nacimiento = "03/02/1993"
        pasajero.genero = "Masculino"
        pasajero.direccion = "Cra 12 # 5-14"
        pasajero.numero_telefono = 313258356
        pasajero.correo = "miasaval@gmail.com"
        return pasajero

    def crear_tripulacion(self):
        print("Desea usar datos guardados en las cookies? (S/N)")
        ans = input()
        if ans == 'S':
            return self.tripulacion_precreada()

        tripulante = Tripulacion()

        print("Ingrese la nacionalidad:")
        tripulante.nacionalidad = input()

        tripulante.numero_maletas = 3

        print("Ingrese el URL a su información médica:")
        tripulante.resumen_infomedica = input()

        print("Ingrese el número de su cédula:")
        tripulante.cedula = input()

        print("Ingrese su Nombre (solo uno):")
        tripulante.nombres = input()

        print("Ingrese su apellido (solo uno):")
        tripulante.apellidos = input()

        print("Ingrese el número de su fecha de nacimiento:")
        tripulante.fecha_de_nacimiento = input()

        print("Ingrese su género:")
        tripulante.genero = input()

        print("Ingrese su dirección:")
        tripulante.direccion = input()

        print("Ingrese su número de teléfono:")
        tripulante.numero_telefono = input()

        print("Ingrese su correo:")
        tripulante.correo = input()

        print("Ingrese el puesto:")
        tripulante.puesto = input()

        print("Ingrese los años de experiencia:")
        tripulante.anios_experiencia = input()

        print("Ingrese la cantidad máxima de horas diarias:")
        tripulante.cant_max_horasdiarias = input()

        return tripulante


    def tripulacion_precreada(self):
        tripulante = Tripulacion()
        tripulante.nacionalidad = "Colombiano"
        tripulante.numero_maletas = 3
        tripulante.resumen_infomedica = "https://www.mayoclinic.org/es/first-aid/emergency-health-information/basics/art-20134333"
        tripulante.cedula = 2003340346
        tripulante.nombres = "Maria"
        tripulante.apellidos = "Nieves"
        tripulante.fecha_de_nacimiento = "03/02/1980"
        tripulante.genero = "Femenino"
        tripulante.direccion = "Cra 15 # 5-12"
        tripulante.numero_telefono = 322358264
        tripulante.correo = "MariaNieves@gmail.com"

        tripulante.puesto = "Capitan"

        tripulante.anios_experiencia = 8

        tripulante.cant_max_horasdiarias = 20
        return tripulante

    def consultar_tripulaciones(self, idx = None):
        if idx is not None:
            self.tripulacion[idx].imprimir_info()
            return 
        if not self.tripulacion:
            print("Hasta ahora, no hay ninguna tripulación registrada en el sistema.")
            return
        print("Existen", len(self.tripulacion), "tripulaciones registradas en el sistema.")
        print("Digite el número de la tripulación que desea consultar (1 -", len(self.tripulacion), "):")
        idx = int(input()) - 1
        self.consultar_tripulaciones(idx)


    def consultar_historial_puerta(self, idx = None):
        if idx is None:
            print("Se tienen", len(self.torre_principal.puertas_embarques), "puertas de embarque.")
            print("Digite el número de la que desea consultar (1 -", len(self.torre_principal.puertas_embarques), "):")
            idx = int(input()) - 1
            if idx < 0 or idx >= len(self.torre_principal.puertas_embarques):
                print("Índice inválido.")
                return
            self.consultar_historial_puerta(idx)
        else:
            self.torre_principal.puertas_embarques[idx].imprimir_historial()

    def finalizar_vuelo(self):
        if len(self.vuelos) == 0 or (i.puerta_embarque != "En vuelo" for i in self.vuelos):
            print("No hay ningun vuelo en el aire\n")
            return
        
        print(f"Existen {len(self.vuelos)} vuelos disponibles:")
        for i, vuelo in enumerate(self.vuelos):
            if not vuelo.puerta_embarque == "En vuelo":
                continue
            print(f"{i}. {vuelo.numero_de_identificacion} | {vuelo.ciudad_origen}-{vuelo.ciudad_destino}")
        ans = -1
        while ans < 0 or ans >= len(self.vuelos) or self.vuelos[ans].puerta_embarque != "En vuelo":
            print("Digite el número del vuelo a despachar:")
            ans = int(input())
            if ans < 0 or ans >= len(self.vuelos) or self.vuelos[ans].puerta_embarque != "En vuelo":
                print("Opción no válida.\n\n")
                continue
        
        self.aeronaves[self.vuelos[ans].id_aeronave].vaciar_aeronave()
        self.vuelos.pop(ans)


    def admin(self):
        cuenta = 3  # Se le dan 3 intentos.

        while cuenta:
            print("\nPor favor, ingrese la contraseña de administrador:")
            password = input()
            if password == self.password:
                return True
            else:
                print("Contraseña incorrecta!")
                print(f"Quedan {cuenta - 1} intentos.")
            cuenta -= 1

        print("Se ha bloqueado el sistema por seguridad. Llame al administrador.")
        return False

    def ejecutar_menu(self, respuesta):
        self.actualizar_torre_de_control()
        if respuesta == 0:
            return
        if respuesta == 1:
            return self.comprar_un_vuelo()
        elif respuesta == 2:
            self.consultar_puertas_de_embarque()
        elif respuesta == 3:
            self.consultar_vuelos(True, False)
        elif respuesta == 5:
            self.construir_aeronave()
        elif respuesta == 6:
            self.consultar_informacion_aeronaves()
        elif respuesta == 7:
            self.editar_informacion_aeronave()
        elif respuesta == 8:
            self.generar_vuelo()
        elif respuesta == 9:
            self.agregar_tripulacion_al_sistema()
        elif respuesta == 10:
            self.consultar_tripulaciones()
        elif respuesta == 11:
            self.consultar_historial_puerta()
        elif respuesta == 12:
            self.finalizar_vuelo()
        elif respuesta == 13:
            self.mantenimiento_aeronaves()
        elif respuesta == 14:
            self.torre_principal.ver_coordenadas_aeronaves()

    def ingresar_aeronave(self, aeron):
        self.torre_principal.agregar_aeronave(aeron)
    def mantenimiento_aeronaves(self):
        
        print("Las aeronaves en espera son: ")

        for i in range(len(self.aeronaves)):
            aeronave = self.aeronaves[i]
            if aeronave.estado == "En espera" and aeronave.numeroDeVuelosAsignados == 0:
                print(f"{i}. id: {aeronave.id}, estado: {aeronave.asignacion}")
        
        print("Digite los indices (no el id) de las aeronaves que quiere hacer mantenimiento")
        print("o que quiere detener el mantenimiento (presione -1 para terminar)")
        ans = None

        indices = set()
        while(True):
            ans = int(input())
            if ans == -1:
                break
            if self.aeronaves[ans].estado != "En espera" or aeronave.numeroDeVuelosAsignados != 0:
                print("La Aeronave elegida no es una opcion")
                continue
            indices.add(ans)

        for i in indices:
            if self.aeronaves[i].asignacion == 'Disponible':
                self.aeronaves[i].asignacion = 'En mantenimiento'
            else :
                self.aeronaves[i].asignacion = 'Disponible'
            print(f"Ahora la aeronave {self.aeronaves[i].id} se encuenta {self.aeronaves[i].asignacion}")

    def hay_vuelos_disponibles(self, necesitaComprar = True):
        if len(self.vuelos) == 0:
            return False
        if not necesitaComprar:
            return True
        for i in self.vuelos:
            if i.disponible_para_compra():
                return True
        return False