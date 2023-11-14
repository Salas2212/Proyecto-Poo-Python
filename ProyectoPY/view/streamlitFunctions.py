import streamlit as st

'''
Para que sea posible guardar variables que necesitamos a medida que avanza
la interaccion con el usuario, hay que hacer uso de el diccionario
st.session_state que nos permite guardar informacion que se mantiene aun asi
el codigo se ejecute nuevamente.


Cada vez que hay una interaccion del usuario con la pantalla, el codigo se vuelve a 
ejecutar por completo, lo que hace que las variables dentro de funciones se pierdan.

Por esta razon, se crean dos arreglos que mantienen la informacion que se necesita

st.session_state.formState nos dice si para un identificador de un formulario dado,
dicho formulario ya fue contestado por el usuario.

st.session_state.ansForm nos dice para un identificador de un formulario dado, 
la informacion que el usuario diligencio. esto puede ser un simple string, hasta
un arreglo de strings.
'''
def forceRestartForms(idx = None):
    '''
    Rutina para reiniciar todos los formularios despues de que el usuario
    termino de realizar una accion del menu.
    '''
    if idx == None:
        st.session_state.formState = [False, False, False, False, False, False]
        st.session_state.ansForm = [None, None, None, None, None, None]
    else:
        st.session_state.formState[idx] = False
        st.session_state.ansForm[idx] = None
def restartForms():
    '''
    Rutina para inicializar los arreglos, que solo es util en la primera iteracion del 
    programa, pues es cuando estos arreglos no han sido creados.
    '''
    if 'formState' not in st.session_state:
        st.session_state.formState = [False, False, False, False, False, False]
    if 'ansForm' not in st.session_state:
        st.session_state.ansForm = [None, None, None, None, None, None]

def formulario(textos, slot):
    '''
    Rutina para crear un cuadro donde se le pide al usuario
    diligenciar varios campos con texto.

    Para continuar, el usuario debe dar click al boton, que es el que termina
    guardando la informacion en st.session_state

    En textos se maneja lo que sale encima de los campos y en slot el indice
    para diferenciar los diferentes formularios que se llenan a medida que 
    avanza el usuario en algunos menus.

    En caso de que al llamar la funcion el usuario ya ha respondido, la funcion
    devuelve lo que el usuario respondio. Caso contrario retorna False, que indica
    que el usuario sigue respondiendo el formulario.
    '''
    # Verifica si el formulario ya fue respondido (Si ya le dio al boton).
    if 'formState' in st.session_state and st.session_state.formState[slot]:
        if len(textos) == 1:
            return st.session_state.ansForm[slot][0]
        return st.session_state.ansForm[slot]
    # Si no lo ha respondido, genera el formulario otra vez
    # Cabe destacar que la informacion diligenciada no se pierde
    # por como funciona el flujo del programa en streamlit.
    with st.form("my_form" + str(slot)):
        array = []
        for i in range(len(textos)):
            k = st.text_input(textos[i])
            array.append(k)
        if st.form_submit_button("Aceptar"): # Click al boton
            st.session_state.formState[slot] = True
            st.session_state.ansForm[slot] = array

            '''
            Cuando el usuario le da al boton aceptar, la informacion es guardada, pero
            el formulario se queda ahi, pues en esa iteracion el formulario fue creado
            y es necesario que haya otra iteracion para que el formulario desaparezca y 
            el programa continue. Para esto usamos st.rerun() para volver a correr todo
            el programa desde el principio en este momento.
            '''
            st.rerun()
    return False

def seleccionMultiple(opciones, slot, pregunta = 'Seleccione: '):
    '''
    El funcionamiento es casi igual a formuario, pero solo es una casilla
    de opcion multiple.
    
    La pregunta es lo que aparece encima de la casilla con las opciones.
    '''
    if 'formState' in st.session_state and st.session_state.formState[slot]:
        return st.session_state.ansForm[slot]
    with st.form("my_form" + str(slot)):
        array = []
        selection = st.selectbox(
            pregunta,
            opciones,
        )
        if st.form_submit_button("Aceptar"):
            st.session_state.formState[slot] = True
            st.session_state.ansForm[slot] = selection
            st.rerun()
    return False

def checkBox(opciones, slot, pregunta = 'Seleccione: ', alMenosUno = False):
    '''
    El funcionamiento es igual a formulario pero solo se trata de varias opciones
    que toman valores de si o no.

    alMenosUno se debe pasar en verdadero si es requerido que el usuario seleccione
    al menos una opcion como verdadera.
    
    '''
    if 'formState' in st.session_state and st.session_state.formState[slot]:
        return st.session_state.ansForm[slot]
    
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
                st.session_state.formState[slot] = True
                st.session_state.ansForm[slot] = array
                st.rerun()
    return False

