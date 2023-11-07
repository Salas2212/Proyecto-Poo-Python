from SistemaPrincipal import *
import random
'''
def generar_string_aleatorio(largo):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(largo))

def generar_entero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

def generar_aeronave_al_azar(cantidad, sys):
    random.seed()
    while cantidad:
        registro = generar_string_aleatorio(6)
        capacidad = generar_entero_aleatorio(10, 200)
        velMax = generar_entero_aleatorio(400, 2500)
        aut = generar_entero_aleatorio(10, 70)
        yFabric = generar_entero_aleatorio(1960, 2023)
        state = "En servicio"
        dado = random.randint(0, 2)

        if dado == 0:
            altitudMaxima = generar_entero_aleatorio(5000, 20000)
            cantidadMotores = generar_entero_aleatorio(1, 6)
            categoria = "Comercial"
            avion = Avion(registro, capacidad, velMax, aut, yFabric, state, altitudMaxima, cantidadMotores, categoria)
            sys.ingresar_aeronave(avion)
        elif dado == 1:
            cantidadRotores = generar_entero_aleatorio(2, 7)
            capacidadElevacion = generar_entero_aleatorio(3000, 13000)
            usoEspecifico = "Combate"
            helicoptero = Helicoptero(registro, capacidad, velMax, aut, yFabric, state, cantidadRotores, capacidadElevacion, usoEspecifico)
            sys.ingresar_aeronave(helicoptero)
        else:
            propietario = "propietario " + str(generar_entero_aleatorio(1, 60))
            listaDeServiciosABordo = "Servicios: "
            canti = generar_entero_aleatorio(1, 5)
            listaDeDestinosFrecuentes = "Destinos frecuentes: "
            canti = generar_entero_aleatorio(1, 5)
            jet_privado = JetPrivado(registro, capacidad, velMax, aut, yFabric, state, propietario, listaDeServiciosABordo, listaDeDestinosFrecuentes)
            sys.ingresar_aeronave(jet_privado)
        cantidad -= 1
'''
if __name__ == "__main__":
    sys = SistemaPrincipal(10)
    #generar_aeronave_al_azar(10, sys)

    while True:
        ans = sys.ejecutar_menu()
        if ans == 0:
            break
