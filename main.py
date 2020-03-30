from procesamiento import procesar
from time import time
from search import search
from coincidencias import contarCoincidencias
import pyautogui
import os

from clave import palabraClave



########################################PROCESAMIENTO DE IMAGEN#########################
def procesamientoImagen():
    screenshot = pyautogui.screenshot(region=(860, 50, 325, 620))
    screenshot.save("./Screens/"+str(time())+".jpg")
    pregunta, respuestas=procesar(screenshot)
    return pregunta,respuestas

########################################BUSQUEDA####################################
def busqueda(pregunta,palabras_claves):
    resultados = search(palabras_claves, 1)
    google = ""
    for resultado in resultados:
        google+=resultado.name
        google+=resultado.description
    return google

##########################################COINCIDENCIAS##############################
def coincidencias(google,respuestas):
    goole_min = google.lower()
    contarCoincidencias(google_min, respuestas)

#########################################FIN########################################


#########################################FUNCIONES DEL MAIN#############################
def busquedaPregunta():
    pregunta,respuestas = procesamientoImagen()
    palabras_claves=palabraClave(pregunta)
    google = busqueda(pregunta,palabras_claves)
    coincidencias(google,respuestas)

def busquedaImagen():
    screenshot = pyautogui.screenshot(region=(1089, 210, 277, 440))
    google=googleImages(screenshot)#falta implementar
    input("\npresione para hacer screenshot\n")
    pregunta,respuestas = procesamientoImagen()
    coincidencias(google,respuestas)

def busquedaManual():
    palabras_claves = input("\nEscriba la palabra clave\n")
    try:
        pregunta,respuestas = procesamientoImagen()
    except:
        pass
    google = busqueda(pregunta,palabras_claves)
    print(google)
    coincidencias(google,respuestas)


while True:
    try:
        n = int(input("Bienvenido señor, espero órdenes\n1.Busqueda Automática\n2.Busqueda Imagen\n3.Busqueda Manual\n"))
    except:
        continue
    if n == 0:
        os.system("cls")
        input("Hasta luego señor")
        break
    elif n == 1:
        busquedaPregunta()
    elif n == 2:
        busquedaImagen()
    elif n == 3:
        busquedaManual()
    input()
    os.system("cls")
