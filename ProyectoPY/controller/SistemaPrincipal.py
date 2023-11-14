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
from view.streamlitFunctions import *
import random
import time
import io
import sys

class SistemaPrincipal:
    
    def __init__(self, numero_de_puertas_de_embarque: int):
        self.torre_principal = TorreDeControl(numero_de_puertas_de_embarque)
        self.vuelos = self.torre_principal.vuelos
        self.tripulacion = []
        self.aeronaves = self.torre_principal.aero
        self.password = 'aeropuerto'
        self.contadorAcciones = 0
        self.esAdmin = False

    def get_cantidad_aeronaves(self):
        return len(self.aeronaves)

    
        
    def actualizar_torre_de_control(self):
        
        self.contadorAcciones += 1
        if self.contadorAcciones % 53 == 0 : 
            if not self.torre_principal.pista_disponible():
                # Si la pista de despegue esta ocupada.
                self.torre_principal.despegar()
        if self.contadorAcciones % 31 == 0 and self.torre_principal.disponibilidad_pista_de_despegue:
            self.torre_principal.usar_pista_de_despegue()


        if self.torre_principal.hay_puertas_disponibles()[0] and not len(self.vuelos) == 0:
            # Llenamos las puertas de embarque que se encuentran disponibles, con vuelos segun su fecha.
            self.torre_principal.asignar_todas_las_puertas()

        
            
        


    def obtener_info_aeronave(self, idx):
        ret = ""
        if 0 <= idx < len(self.aeronaves):
            aeronave = self.aeronaves[idx]
            ret += f"Registro de marca: {aeronave.registro_de_marca}\n" 
            ret += f"Capacidad de pasajeros: {aeronave.capacidad_de_pasajeros}\n"
            ret += f"Velocidad máxima: {aeronave.velocidad_max}\n"
            ret += f"Autonomía: {aeronave.autonomia}\n"
            ret += f"Año de fabricación: {aeronave.ano_fabricacion}\n"
            ret += f"Asignacion: {aeronave.asignacion}\n"
            ret += f"Estado: {aeronave.estado}\n"
            ret += f"Coordenadas: ({aeronave.coordenadas[0]}, {aeronave.coordenadas[1]})\n"

            ret += "\nInformación específica:\n"
            ret += f"Tipo = {aeronave.get_tipo()}\n"
            ret += aeronave.imprimir_informacion_especifica()
            return ret
        else:
            return "Indice de aeronave fuera de rango."


    def comprar_un_vuelo(self):
        if not self.hay_vuelos_disponibles():
            return "Por el momento, no hay vuelos disponibles :("
        txt = ''
        txt += "Para comprar un vuelo debe iniciar sesión.\n"
        txt += "Vamos a crear tu perfil.\n"
        st.text(txt)
        usuario = self.crear_pasajero()
        if usuario == False:
            return False
        txt = ''
        txt += "\n" * 3
        txt += "Vale, ahora selecciona el vuelo que deseas comprar:\n"
        
        txt += self.consultar_vuelos(False, True)
        st.text(txt)

        ans = formulario(["(Digita el número al principio del vuelo, o digita -1 para cancelar)"], 2)
        if ans == False:
            return False
        ans = int(ans)
        if ans == -1:
            return "Cancelado"
        if 0 <= ans < len(self.vuelos):
            if self.aeronaves[self.vuelos[ans].id_aeronave].sillas_restantes <= 0:
                return "Este vuelo está completo. Por favor selecciona otro."
            elif not self.vuelos[ans].disponible_para_compra:
                return "Este vuelo ya no se encuentra disponible. Por favor seleccione otro."
        
        self.aeronaves[self.vuelos[ans].id_aeronave].asignar_silla()
        self.vuelos[ans].agregar_pasajero(usuario)
        return "Compra realizada exitosamente."


    def consultar_puertas_de_embarque(self):
        ret = ''
        for puerta_embarque in self.torre_principal.puertas_embarques:
            ret += puerta_embarque.imprimir_info()
            ret += '\n'
        return ret

    def consultar_vuelos(self, expandible, imprimir_sillas):
        if not self.hay_vuelos_disponibles(False):
            return "Por el momento, no hay vuelos disponibles :("
        txt = ''
        txt += f"Existen {len(self.vuelos)} vuelos disponibles:\n"
        for i, vuelo in enumerate(self.vuelos):
            if not vuelo.disponible_para_compra() and imprimir_sillas:
                continue
            txt += f"{i}. {vuelo.numero_de_identificacion} | {vuelo.ciudad_origen}-{vuelo.ciudad_destino}\n"
            puerta = vuelo.puerta_embarque
            if puerta == -1:
                txt += f"Fecha: {vuelo.fecha}. Puerta de embarque: Sin definir. \n"
            elif puerta == "En vuelo":
                txt += f"Fecha: {vuelo.fecha}. En vuelo.\n"
            elif puerta == "En pista de Despegue":
                txt += f"Fecha: {vuelo.fecha}. En pista de despegue\n"
            else: 
                txt += f"Fecha: {vuelo.fecha}. Puerta de embarque: {puerta} ({self.torre_principal.puertas_embarques[vuelo.puerta_embarque].get_ubicacion()}).\n"
            if imprimir_sillas:
                txt += f"Sillas disponibles: {self.aeronaves[vuelo.id_aeronave].sillas_restantes}\n"

        if not expandible or not self.vuelos:
            return txt
        txt += "\n"
        txt += "Si desea consultar información adicional sobre vuelos en específico\n"
        st.text(txt)
        ans = seleccionMultiple(["Si", "No"], 0, "Desea consultar información adicional sobre vuelos en específico?")
        if ans == False:
            return False
        if ans != 'Si':
            return ""
        if not self.admin():
            return "Intento de hackeo descubierto. Llamando administrador"
        idx = formulario(["Digite el numero del vuelo entre las opciones dadas:"], 1)
        if idx == False:
            return False
        idx = int(idx)
        if 0 <= idx < len(self.vuelos):
            txt = ''
            txt += f"Vuelo {idx} escogido.\n"
            txt += f"id de la aeronave: {self.vuelos[idx].id_aeronave}\n"
            txt += "Tripulación:\n"
            for tripulante in self.vuelos[idx].tripulacion:
                txt += f"{tripulante.cedula} - {tripulante.nombres} {tripulante.apellidos}\n"
            txt += "Pasajeros:\n"
            for pasajero in self.vuelos[idx].pasajeros:
                txt += f"{pasajero.nombres} {pasajero.apellidos}. Maletas: {pasajero.numero_maletas}\n"
            return txt
        else:
            return "Opción no válida"


    def construir_aeronave(self):
        temp = seleccionMultiple(["Si", "No"], 0, "Desea construir una Aeronave con atributos por defecto?")
        if temp == False:
            return False
        ans = temp
        if ans == "Si":
            avion = Avion()
            self.torre_principal.agregar_aeronave(avion)
            return 'Avion creado exitosamente.'
        textos = []
        textos.append("Ingrese el registro de la Aeronave: ")
        textos.append("Ingrese la capacidad de la Aeronave: ")
        textos.append("Ingrese la velocidad máxima: ")
        textos.append("Ingrese la autonomía: ")
        textos.append("Ingrese el año de fabricación: ")
        temp = formulario(textos, 1)
        if temp == False:
            return False
        
        registro, capacidad, vel_max, aut, y_fabric = temp
        
        state = "Disponible"

        respuesta = formulario(["¿Qué tipo de aeronave deseas construir? (Avion, Helicoptero, JetPrivado)"], 2)
        if not respuesta:
            return False
        info = []
        if respuesta == "Avion":
            info.append("Ingrese la altitud máxima: ")
            info.append("Ingrese la cantidad de motores: ")
            info.append("Ingrese la categoría: ")
            altitud_maxima, cantidad_motores, categoria = [0, 0, 0]
            temp = formulario(info, 3)
            if not temp:
                return False
            altitud_maxima, cantidad_motores, categoria = temp
            avion = Avion(registro, capacidad, vel_max, aut, y_fabric, state, altitud_maxima, cantidad_motores, categoria)
            self.torre_principal.agregar_aeronave(avion)
            
            
        elif respuesta == "Helicoptero":
            info.append("Ingrese la cantidad de rotores: ")
            info.append("Ingrese la capacidad de elevación: ")
            info.append("Ingrese el uso específico: ")
            temp = formulario(info, 3)
            if not temp:
                return False
            cantidad_rotores, capacidad_elevacion, uso_especifico = temp
            helicoptero = Helicoptero(registro, capacidad, vel_max, aut, y_fabric, state, cantidad_rotores, capacidad_elevacion, uso_especifico)
            self.torre_principal.agregar_aeronave(helicoptero)
            return "Helicoptero creado correctamente"
        elif respuesta == "JetPrivado":
            info.append("Ingrese el propietario: ")
            info.append("Ingrese la lista de servicios a bordo: ")
            info.append("Ingrese la lista de destinos frecuentes: ")
            temp = formulario(info, 3)
            if not temp:
                return False
            propietario, lista_servicios_abordo, lista_destinos_frecuentes = temp
            jet_privado = JetPrivado(registro, capacidad, vel_max, aut, y_fabric, state, propietario, lista_servicios_abordo, lista_destinos_frecuentes)
            self.torre_principal.agregar_aeronave(jet_privado)
            return "Jet creado correctamente."
        else:
            return "Tipo no válido!"


    def consultar_informacion_aeronaves(self):
        if not self.aeronaves:
            return "Hasta ahora, no hay ninguna aeronave registrada en el sistema."
        ret = ''
        st.write(f"Existen {len(self.aeronaves)} aeronaves registradas en el sistema.")
        idx = formulario([f"Digite el número de la aeronave que desea consultar (1 - {len(self.aeronaves)}): "], 4)
        if idx == False:
            return False
        idx = int(idx) - 1
        ret += self.obtener_info_aeronave(idx) + "\n"
        return ret
    
    
    

    def editar_informacion_aeronave(self, i = None):
        if i is None:
            if(len(self.aeronaves) == 0):
                return "Hasta ahora, no hay ninguna aeronave registrada en el sistema."
            st.text(f"Existen {len(self.aeronaves)} aeronaves registradas en el sistema.\n")
            info = []
            info.append(f"Digite el numero de la aeronave que desea editar ( 1 - {len(self.aeronaves)} ): ")
            idx = formulario(info, 0)
            if idx == False:
                return False
            idx = int(idx)
            idx -= 1
            return self.editar_informacion_aeronave(idx)
            
        if 0 <= i < len(self.aeronaves):
            options = []
            options.append("1. Registro de marca")
            options.append("2. Capacidad de pasajeros")
            options.append("3. Velocidad máxima")
            options.append("4. Autonomía")
            options.append("5. Año de fabricación")
            options.append("6. Modificar atributos específicos")
            options.append("7. Cancelar")
            
            opcion = seleccionMultiple(options, 1, 'Que caracteristica deseas modificar?')
            if opcion == False:
                return False
            nuevoValor = True
            if int(opcion[0]) <= 5:
                nuevoValor = formulario([f"Ingrese el nuevo valor de {opcion[3:]}: "], 2)
                if nuevoValor == False:
                    return False
            
            if int(opcion[0]) == 1:
                self.aeronaves[i].registro_de_marca = nuevoValor
            elif int(opcion[0]) == 2:
                self.aeronaves[i].capacidad_de_pasajeros = int(nuevoValor)
            elif int(opcion[0]) == 3:
                self.aeronaves[i].velocidad_max = int(nuevoValor)
            elif int(opcion[0]) == 4:
                self.aeronaves[i].autonomia = int(nuevoValor)
            elif int(opcion[0]) == 5:
                self.aeronaves[i].ano_fabricacion = int(nuevoValor)
            elif int(opcion[0]) == 6:
                # Modifica atributos específicos según el tipo de aeronave
                return self.aeronaves[i].editar_informacion_especifica()
            elif int(opcion[0]) == 7:
                return "Operación cancelada."
            else:
                return "Opción no válida."
        else:
            return "Indice de aeronave fuera de rango."

    def generar_vuelo(self):
        
        
        nuevo_vuelo = Vuelo()
        nuevo_vuelo.ciudad_origen = formulario(["Digite la ciudad de origen"], 0)
        if nuevo_vuelo.ciudad_origen == False:
            return False
        
        es_de_cali = nuevo_vuelo.ciudad_origen == 'Cali'

        disp_aeronaves, aeronave_disponible = self.torre_principal.hay_aeronaves_disponibles(es_de_cali)

        if not disp_aeronaves or not self.tripulacion:
            ret = "ERROR:\n"
            if not disp_aeronaves:
                ret += "No hay aeronaves disponibles por el momento."
            if not self.tripulacion:
                ret += "No hay tripulaciones registradas en el sistema.\n"
            return ret
        
        
        
        
        nuevo_vuelo.ciudad_destino = formulario(["Digite la ciudad de destino"], 1)
        if nuevo_vuelo.ciudad_destino == False:
            return False
        
        formato = "%d/%m/%Y"  # Formato para parsear la fecha
        var = True
        nuevo_vuelo.fecha = formulario(["Digite la fecha del vuelo"], 2)
        if nuevo_vuelo.fecha == False:
            return False
        try:
            fecha = datetime.strptime(nuevo_vuelo.fecha, formato)
        except ValueError:
            return "La fecha no es valida"
    

        if len(nuevo_vuelo.ciudad_destino) < 2 or len(nuevo_vuelo.ciudad_origen) < 2 or len(nuevo_vuelo.fecha) < 2:
            return "La información dada no es válida"

        # Generar un ID único para el vuelo
        id = nuevo_vuelo.ciudad_origen[:2] + nuevo_vuelo.ciudad_destino[:2] + nuevo_vuelo.fecha[:2]
        id += str(random.randint(0, 99999)).zfill(5)
        nuevo_vuelo.numero_de_identificacion = id
        txt = ''
        txt += "Las aeronaves disponibles son:\n"
        for i, aeronave in enumerate(self.aeronaves):
            if aeronave.disponible() and (not es_de_cali or aeronave.vuelos_desde_cali == 0):
                txt += f"{i}. {aeronave.get_tipo()} | autonomía: {aeronave.autonomia} | capacidad de pasajeros: {aeronave.capacidad_de_pasajeros}\n"
        st.text(txt)
        ans_aero = formulario(["Digite el numero de la aeronave a usar. (Para cancelar, digite -1)"], 3)
        if ans_aero == False:
            return False
        ans_aero = int(ans_aero)
        if ans_aero == -1:
            return "Cancelado."
        if 0 <= ans_aero < len(self.aeronaves) and self.aeronaves[ans_aero].disponible() and (not es_de_cali or aeronave.vuelos_desde_cali == 0):
            pass
        else:
            return "La aeronave seleccionada no es valida."
        txt = ''
        txt += f"Se ha escogido la aeronave {ans_aero}:\n"
        txt += self.obtener_info_aeronave(ans_aero)
        txt += "\n\n"
        txt += f"Existen {len(self.tripulacion)} tripulaciones registradas en el sistema:\n"
        tripulantes = []
        for i, tripulante in enumerate(self.tripulacion):
            txt += f"{i+1}: {tripulante.apellidos}: Cantidad máxima de horas: {tripulante.cant_max_horas_diarias}\n"
            tripulantes.append(tripulante.apellidos)
        st.text(txt)

        ans = checkBox(tripulantes, 4, ("Seleccione los tripulantes a agregar" + ('Minimo 1' if es_de_cali else '')), es_de_cali)
        if ans == False:
            return False
        for i, tripulante in enumerate(self.tripulacion):
            if ans[i]:
                nuevo_vuelo.agregar_tripulante(self.tripulacion[i])
                self.tripulacion[i].NoVuelo = nuevo_vuelo.numero_de_identificacion

        nuevo_vuelo.puerta_embarque = -1
        nuevo_vuelo.id_aeronave = self.aeronaves[ans_aero].id
        if es_de_cali:
            self.aeronaves[ans_aero].vuelos_desde_cali += 1
        self.aeronaves[ans_aero].asignar_vuelo()
        self.vuelos.append(nuevo_vuelo)
        return "Vuelo generado con éxito."

    def agregar_tripulacion_al_sistema(self):
        creado = self.crear_tripulacion()
        if creado == False:
            return False
        self.tripulacion.append(creado)
        return "Tripulación guardada exitosamente"

    def crear_pasajero(self):
        ans = seleccionMultiple(["Si", "No"], 0, "Desea usar datos guardados en las cookies?")
        if ans == False:
            return False
        if ans == 'Si':
            return self.pasajero_precreado()

        pasajero = Pasajero()
        ans = formulario(["Ingrese la nacionalidad:", "Ingrese el número de maletas:", "Ingrese el URL a su información médica:", "Ingrese el número de su cédula:", "Ingrese su Nombre:",
                          "Ingrese su apellido:", "Ingrese el número de su fecha de nacimiento:", "Ingrese su género:", "Ingrese su dirección:", 
                          "Ingrese su número de teléfono:", "Ingrese su correo:"], 1)
        if ans == False:
            return ans
        
        pasajero.nacionalidad, pasajero.numero_maletas, pasajero.resumen_infomedica, pasajero.cedula, pasajero.nombres, pasajero.apellidos, pasajero.fecha_de_nacimiento, pasajero.genero, pasajero.direccion, pasajero.numero_telefono, pasajero.correo = ans

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
        ans = seleccionMultiple(["Si", "No"], 0, "Desea usar datos guardados en las cookies?")
        if ans == False:
            return False
        
        ans = ans[0]

        if ans == 'S':
            return self.tripulacion_precreada()

        tripulante = Tripulacion()

        data = formulario(["Ingrese la nacionalidad: ", "Ingrese el URL a su informacion medica", "Ingrese el número de su cédula:",
                           "Ingrese su Nombre: ", "Ingrese su Apellido: ", "Ingrese el número de su fecha de nacimiento:",
                           "Ingrese su género:", "Ingrese su dirección:", "Ingrese su número de teléfono:", "Ingrese su correo:",
                           "Ingrese el puesto:", "Ingrese los años de experiencia:", "Ingrese la cantidad máxima de horas diarias:"], 1)
        if data == False:
            return False
        tripulante.nacionalidad, tripulante.resumen_infomedica, tripulante.cedula, tripulante.nombres, tripulante.apellidos, tripulante.fecha_de_nacimiento, tripulante.genero, tripulante.direccion, tripulante.numero_telefono, tripulante.correo, tripulante.puesto, tripulante.anios_experiencia, tripulante.cant_max_horas_diarias = data

        tripulante.numero_maletas = 3

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
            return self.tripulacion[idx].imprimir_info()
        if not self.tripulacion:
            return "Hasta ahora, no hay ninguna tripulación registrada en el sistema."
        st.text(f"Existen {len(self.tripulacion)} tripulaciones registradas en el sistema.")
        idx = formulario([f"Digite el número de la tripulación que desea consultar (1 - {len(self.tripulacion)}):"], 0)
        if idx == False:
            return False
        idx = int(idx) - 1
        return self.consultar_tripulaciones(idx)


    def consultar_historial_puerta(self, idx = None):
        if idx is None:
            st.text(f"Digite el número de la puerta de embarque que desea consultar (1 - {len(self.torre_principal.puertas_embarques) }):")
            idx = formulario([f"Digite el número de la puerta de embarque que desea consultar (1 - {len(self.torre_principal.puertas_embarques) }):"], 0)
            if idx == False:
                return False
            idx = int(idx) - 1
            if idx < 0 or idx >= len(self.torre_principal.puertas_embarques):
                return "Indice inválido."
            return self.consultar_historial_puerta(idx)
        else:
            return self.torre_principal.puertas_embarques[idx].imprimir_historial()

    def finalizar_vuelo(self):
        hayEnVuelo = False
        for i in self.vuelos:
            if i.puerta_embarque == "En vuelo":
                hayEnVuelo = True
        if len(self.vuelos) == 0 or not hayEnVuelo:
            return "No hay ningun vuelo en el aire\n"
        
        for i, vuelo in enumerate(self.vuelos):
            if not vuelo.puerta_embarque == "En vuelo":
                continue
            st.text(f"{i}. {vuelo.numero_de_identificacion} | {vuelo.ciudad_origen}-{vuelo.ciudad_destino}")
            #print()
        
        ans = formulario(["Digite el numero del vuelo a despachar: "], 0)
        if ans == False:
            return False
        ans = int(ans)
        if ans < 0 or ans >= len(self.vuelos) or self.vuelos[ans].puerta_embarque != "En vuelo":
            return "El numero digitado no es valido."
        
        self.aeronaves[self.vuelos[ans].id_aeronave].vaciar_aeronave()
        self.vuelos.pop(ans)
        return "El vuelo ha sido reiniciado exitosamente."


    def admin(self):
        return self.esAdmin

    def ejecutar_menu(self, respuesta):
        self.actualizar_torre_de_control()
        restartForms()
        
        if respuesta >= 4:
            respuesta += 1
        if respuesta == 0:
            return
        if respuesta == 1:
            return self.comprar_un_vuelo()
        elif respuesta == 2:
            return self.consultar_puertas_de_embarque()
        elif respuesta == 3:
            return self.consultar_vuelos(True, False)
        elif respuesta == 5:
            return self.construir_aeronave()
        elif respuesta == 6:
            return self.consultar_informacion_aeronaves()
        elif respuesta == 7:
            return self.editar_informacion_aeronave()
        elif respuesta == 8:
            return self.generar_vuelo()
        elif respuesta == 9:
            return self.agregar_tripulacion_al_sistema()
        elif respuesta == 10:
            return self.consultar_tripulaciones()
        elif respuesta == 11:
            return self.consultar_historial_puerta()
        elif respuesta == 12:
            return self.finalizar_vuelo()
        elif respuesta == 13:
            return self.mantenimiento_aeronaves()
        elif respuesta == 14:
            return self.torre_principal.ver_coordenadas_aeronaves()

    def ingresar_aeronave(self, aeron):
        self.torre_principal.agregar_aeronave(aeron)
    def mantenimiento_aeronaves(self):
        
        txt = "Las aeronaves en espera son: \n"

        for i in range(len(self.aeronaves)):
            aeronave = self.aeronaves[i]
            if aeronave.estado == "En espera" and aeronave.numeroDeVuelosAsignados == 0:
                txt += f"{i}. id: {aeronave.id}, estado: {aeronave.asignacion}\n"
        

        txt += "\n\n Digite el indice (no el id) de la aeronave que quiere hacer mantenimiento\no que quiere detener el mantenimiento (presione -1 para cancelar)\n"
        st.text(txt)
        ans = formulario(["Indice aeronave: "], 0)
        if ans == False:
            return False
        ans = int(ans)
        if ans == -1:
            return "Cancelado"
        if self.aeronaves[ans].estado != "En espera" or aeronave.numeroDeVuelosAsignados != 0:
            return "La Aeronave elegida no es una opcion"
        if self.aeronaves[ans].asignacion == 'Disponible':
            self.aeronaves[ans].asignacion = 'En mantenimiento'
        else:
            self.aeronaves[ans].asignacion = 'Disponible'
        return f"Ahora la aeronave {self.aeronaves[ans].id} se encuenta {self.aeronaves[ans].asignacion}"

    def hay_vuelos_disponibles(self, necesitaComprar = True):
        if len(self.vuelos) == 0:
            return False
        if not necesitaComprar:
            return True
        for i in self.vuelos:
            if i.disponible_para_compra():
                return True
        return False