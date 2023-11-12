import streamlit as st
import requests

def espereHastaInput(inp):
    while inp == '':
        pass
def espereHastaOpcion(inp, opcion):
    while not inp in opcion:
        pass

def pedirDato(textoAImprimir, opciones = None):
    #print('asking')
    dato = st.text_input(textoAImprimir)
    if opciones == None:
        espereHastaInput(dato)
    else:
        espereHastaOpcion(dato, opciones)
    return dato
def pedirDatos(textos):
    array = []
    for i in range(len(textos)):
        k = st.text_input(textos[i])
        array.append(k)
    for i in range(len(textos)):
        #print('esperando ', i)
        espereHastaInput(array[i])
    return array

def forceRestartForms(idx = None):
    if idx == None:
        st.session_state.formState = [False, False, False, False, False]
        st.session_state.ansForm = [None, None, None, None, None]
    else:
        st.session_state.formState[idx] = False
        st.session_state.ansForm[idx] = None
def restartForms():
    if 'formState' not in st.session_state:
        st.session_state.formState = [False, False, False, False, False]
    if 'ansForm' not in st.session_state:
        st.session_state.ansForm = [None, None, None, None, None]

def formulario(textos, slot):
    if 'formState' in st.session_state and st.session_state.formState[slot]:
        #print('returnin', st.session_state.ansForm)
        if len(textos) == 1:
            return st.session_state.ansForm[slot][0]
        return st.session_state.ansForm[slot]
    #print('gen form', textos)
    
    with st.form("my_form" + str(slot)):
        array = []
        for i in range(len(textos)):
            k = st.text_input(textos[i])
            array.append(k)
        if st.form_submit_button("Aceptar"):
            st.session_state.formState[slot] = True
            st.session_state.ansForm[slot] = array
            #print('guardado', st.session_state.ansForm[slot])
            st.rerun()
    return False
def seleccionMultiple(opciones, slot, pregunta = 'Seleccione: '):
    if 'formState' in st.session_state and st.session_state.formState[slot]:
        #print('returnin', st.session_state.ansForm)
        return st.session_state.ansForm[slot]
    #print('gen form')
    with st.form("my_form" + str(slot)):
        array = []
        selection = st.selectbox(
            pregunta,
            opciones,
        )
        if st.form_submit_button("Aceptar"):
            st.session_state.formState[slot] = True
            st.session_state.ansForm[slot] = selection
            print('guardado', st.session_state.ansForm[slot])
            st.rerun()
    return False

def checkBox(opciones, slot, pregunta = 'Seleccione: ', alMenosUno = False):
    if 'formState' in st.session_state and st.session_state.formState[slot]:
        #print('returnin', st.session_state.ansForm)
        return st.session_state.ansForm[slot]
    #print('gen form', opciones)
    
    with st.form("my_form" + str(slot)):
        array = []
        for i in range(len(opciones)):
            k = st.checkbox(opciones[i])
            array.append(k)
        if st.form_submit_button("Aceptar"):
            valid = True
            if alMenosUno:
                valid = False
                for i in array:
                    if i:
                        valid = True
            if valid:
                #print ('VALID')
                st.session_state.formState[slot] = True
                st.session_state.ansForm[slot] = array
                #print('guardado', st.session_state.ansForm[slot])
                st.rerun()
    return False

def infoPais(nombre_pais):
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
    response = requests.get(url)
    data = response.json()
    return data[0] 

def printInfoPais(data):
    st.title("Información del País")

    nombre_pais = st.text_input("Ingrese el nombre del país:")

    if nombre_pais:
        info_pais = infoPais(nombre_pais)

        if info_pais:
            st.write(f"Nombre del País: {info_pais['name']['common']}")
            st.write(f"Moneda: {info_pais['currencies'].get('primary')}")
            st.write(f"Capital: {info_pais['capital'][0]}")
            st.write(f"Región: {info_pais['region']}")
            st.write(f"Población: {info_pais['population']}")
            st.image(info_pais['flags']['png'], caption='Bandera', use_column_width=True)
        else:
            st.warning("No se encontró información para el país ingresado.")
