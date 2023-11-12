import streamlit as st
from controller.SistemaPrincipal import *



class todoView:
    paso = 0
    respuesta = ''
    escogido = ''
    aeropuerto = SistemaPrincipal(10)
    admin = False
    def __init__(self):
        st.title("Sistema de Aeropuerto")
        self.opciones1 = ["Comprar un vuelo", "Consultar puertas de embarque", "Consultar vuelos"]
        self.opciones_administrador = ["Comprar un vuelo", "Consultar puertas de embarque", "Consultar vuelos", "Agregar una nave", "Consultar información de las naves", "Editar la información de una nave",
                "Generar un vuelo", "Ingresar una tripulación al sistema", "Consultar tripulaciones",
                "Consultar historial de una puerta de embarque", "Finalizar un vuelo", "Realizar mantenimiento Aeronave",
                "Ver coordenadas Aeronaves", "Atrás"]

    def opcion_a_indice_opcion(self, opcion_en_texto):
         for i in range(len(self.opciones_administrador)):
              if self.opciones_administrador[i] == opcion_en_texto:
                   return i + 1

    def avanzar():
        todoView.paso += 1   
        todoView.paso %= 2       
    
    def main(self):
        main = st.empty()
        if todoView.paso == 0:
            with main.container():
                valor = ''
                if todoView.admin:
                    valor = 'pass'
                admin_password_input = st.text_input("Por favor, ingrese la contraseña de administrador:", type="password", value= valor)
                #admin_password_input = st.text_input("Por favor, ingrese la contraseña de administrador:", type="password")
                if admin_password_input == 'pass':
                    todoView.admin = True
                    todoView.aeropuerto.esAdmin = True
                else:
                    todoView.admin = False
                    todoView.aeropuerto.esAdmin = False
                if not self.admin:
                    todoView.escogido = st.selectbox("Seleccione la acción que desea realizar:", self.opciones1, key='1')
                else:
                    todoView.escogido = st.selectbox("Seleccione la acción que desea realizar: ", self.opciones_administrador, key='2')
                st.button("Continuar", disabled=bool(todoView.paso != 0) , on_click=todoView.avanzar)
                
        if todoView.paso == 1:
            main.empty()
            with main.container():
                todoView.respuesta = todoView.aeropuerto.ejecutar_menu(self.opcion_a_indice_opcion(todoView.escogido))
                if todoView.respuesta != False:
                    st.text(todoView.respuesta)
                    st.button("Aceptar", on_click= todoView.avanzar)
                    forceRestartForms()

                    
            
        

