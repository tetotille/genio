from procesamiento import procesar
from time import time
from search import search
from coincidencias import contarCoincidencias
import pyautogui
import os
from clave import palabraClave




########################################PROCESAMIENTO DE IMAGEN#########################
def procesamientoImagen():
    pregunta, respuestas=procesar()
    return pregunta,respuestas

########################################BUSQUEDA####################################
def busqueda(palabras_claves):
    resultados = search(palabras_claves, 1)
    definitivo = ""
    for resultado in resultados:
        definitivo = definitivo+resultado.description
    return definitivo

##########################################COINCIDENCIAS##############################
def coincidencias(definitivo,respuestas):
    texto = definitivo.lower()
    contarCoincidencias(texto, respuestas)

#########################################FIN########################################


########################################FUNCIONES DEL MAIN##############################
def busquedaPregunta():
    pregunta,respuestas = procesamientoImagen()#Llama a la IA que procesa la imagen y lo transforma en texto
    palabras_claves=palabraClave(pregunta)#busca las palabras claves a buscar se puede obviar esta parte y buscar solo la pregunta
    definitivo = busqueda(palabras_claves)#realiza la búsqueda en google
    coincidencias(definitivo,respuestas)#cuenta e imprime las coincidencias de respuestas generadas

def busquedaImagen():
    screenshot = pyautogui.screenshot(region=(1089, 210, 277, 440))
    definitivo=googleImages(screenshot)#falta implementar
    input("\npresione para hacer screenshot\n")
    pregunta,respuestas = procesamientoImagen()
    coincidencias(definitivo,respuestas)

def busquedaManual():
    palabras_claves = input("\nEscriba la palabra clave\n")
    try:
        pregunta,respuestas = procesamientoImagen()
    except:
        pass
    definitivo = busqueda(palabras_claves)
    print(definitivo)
    coincidencias(definitivo,respuestas)

##############################MAIN####################################
while True:
    try:#Pregunta la opcion que se quiere
        n = int(input("Bienvenido señor, espero órdenes\n1.Búsqueda Automática\n2.Busqueda de Imagen\n3.Búsqueda Manual\n0.Salir\n"))
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
