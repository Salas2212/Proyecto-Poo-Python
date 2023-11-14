import streamlit as st
from controller.SistemaPrincipal import *
from model.Paises import country_codes, country_names, nameToCode
import requests, json # Para usar la API


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
                "Ver coordenadas Aeronaves"]

    def opcion_a_indice_opcion(self, opcion_en_texto):
         for i in range(len(self.opciones_administrador)):
              if self.opciones_administrador[i] == opcion_en_texto:
                   return i + 1

    def avanzar():
        todoView.paso += 1   
        todoView.paso %= 2       
    




    def main(self):
        main = st.empty()

        '''
        En la variable de clase se pueden guardar variables que se mantienen a medida que pasan
        las iteraciones en la interfaz.

        Por esta razon en todoView.paso puedo guardar en que estado se encuentra el usuario del menu

        todoView.paso es 0 cuando el usuario no ha seleccionado nada en el menu principal
        Se mantiene asi hasta que seleccione algo y le de a aceptar.

        todoView.paso es 1 entonces, y ejecuta la opcion escogida dentro de la variable de clase
        aeropuerto que guarda la instancia del aeropuerto en general. Si el valor retornado es false,
        se mantiene realizando la misma operacion hasta que se le retorna un string que es el valor que
        se desea imprimir como resultado de la operacion realizada.

        Aqui se espera hasta que el usuario le de a aceptar lo que reinicia todoView.paso a 0.
        '''
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

        # Menú lateral en la parte izquierda
        with st.sidebar:
        
            st.title("Visor de paises")
            selection = st.selectbox(
                'Seleccione el pais que quiere ver',
                country_names,
            )
            code = nameToCode.get(selection)
            url = f"https://restcountries.com/v3.1/alpha/{code}?fields=currencies,capital,region,population,flags,name"
            response = requests.get(url)
            if response.status_code == 200:
                # Access the text content of the response
                page_text = response.text
                diccionario = json.loads(page_text)

                # Print or process the extracted text
                #st.text(diccionario)
                nombre = diccionario['name']['common']
                monedasDict = diccionario['currencies']
                capital = diccionario['capital']
                capitales = ''
                for cap in capital:
                    capitales += cap + ', '
                capitales = capitales[:-2]
                monedas = [moneda for moneda in monedasDict]
                listaDeMonedas = ''
                for moneda in monedas:
                    listaDeMonedas += "- " + diccionario['currencies'][moneda]['name'] + '\n'


                region = diccionario['region']
                poblacion = diccionario['population']
                bandera = diccionario['flags']['png']
                st.text(f'Monedas:')
                st.text(listaDeMonedas)
                st.text(f'Capitales: {capitales }')
                st.text(f'Region: {region}')
                st.text(f'Poblacion: {poblacion}')
                st.image(
                    bandera,
                    width=300, # Manually Adjust the width of the image as per requirement
                )
            else:
                st.text('Error en el uso de la API')
                    
            
        

