import streamlit as st
from controller.SistemaPrincipal import *



class todoView:
    def __init__(self, numeroDePuertas = 10):

        st.title("Sistema de Aeropuerto")
        self.aeropuerto = SistemaPrincipal(numeroDePuertas)
        self.admin = False
        self.terminado = True
        self.opciones1 = ["Comprar un vuelo", "Consultar puertas de embarque", "Consultar vuelos"]
        self.opciones_administrador = ["Comprar un vuelo", "Consultar puertas de embarque", "Consultar vuelos", "Agregar una nave", "Consultar información de las naves", "Editar la información de una nave",
                "Generar un vuelo", "Ingresar una tripulación al sistema", "Consultar tripulaciones",
                "Consultar historial de una puerta de embarque", "Finalizar un vuelo", "Realizar mantenimiento Aeronave",
                "Ver coordenadas Aeronaves", "Atrás"]

    def opcion_a_indice_opcion(self, opcion_en_texto):
         for i in range(len(self.opciones_administrador)):
              if self.opciones_administrador[i] == opcion_en_texto:
                   return i
              
        
    def main(self):
        
        admin_password_input = st.text_input("Por favor, ingrese la contraseña de administrador:", type="password")
        if admin_password_input == 'pass':
                self.admin = True

        if not self.admin:
            self.option = st.selectbox("Seleccione la acción que desea realizar:", self.opciones1, key='1')
        else:
            self.option = st.selectbox("Seleccione la acción que desea realizar: ", self.opciones_administrador, key='2')
        if self.terminado:     
            self.respuesta = self.aeropuerto.ejecutar_menu(self.opcion_a_indice_opcion(self.option))
            print("Done!")
            self.terminado = False
        else:
            st.text(self.respuesta)
            st.text("ok")
            click = st.button("Ok", disabled = bool(self.terminado))
            if click:
                self.terminado = True

