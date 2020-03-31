from procesamiento import procesar
import time
from search import search
from coincidencias import contarCoincidencias
import pyautogui
import os
from search import reverse_search




########################################PROCESAMIENTO DE IMAGEN#########################
def procesamientoImagen():
    titulo_string, lista_palabras=procesar()
    return titulo_string,lista_palabras
########################################PALABRA CLAVE##############################
#falta agregar una función que elija lo que haya que buscar
def palabraClave(titulo_string):
    a = titulo_string.find('"')
    if a != -1:
        a2 = titulo_string[a+1:-1].find('"')+a
        palabra_clave = titulo_string[a+1:a2]
    elif not titulo_string[2:-1].islower():
        aux = ""
        for i in range(len(titulo_string[2:-1])):
            letra = titulo_string[i+2]
            if letra.isupper():
                j = i
                i = titulo_string.find(" ")
                aux = aux+titulo_string[j:i]
        palabra_clave = aux
    elif "el" in titulo_string.lower() and "es":
        a = titulo_string.lower().find("el")
        b = titulo_string.find("es")
        palabra_clave = titulo_string[a+3:b-1]
    else:
        palabra_clave = titulo_string
    return palabra_clave
########################################BUSQUEDA####################################
def busqueda(titulo_string,palabra_clave):
    resultados = search(palabra_clave, 1)
    definitivo = ""
    for resul in resultados:
        definitivo = definitivo+resul.description
    return definitivo

##########################################COINCIDENCIAS##############################
def coincidencias(definitivo,lista_palabras):
    texto = definitivo.lower()
    contarCoincidencias(texto, lista_palabras)

####################################BUSQUEDA A TRAVES DE IMAGENES#########################
def queryImages(screenshot):
    dia = str(time.strftime("%d-%m-%y"))
    direccion = "./imagenes/"+str(time.time())+".png"
    try:
        screenshot.save(direccion)
    except:
        os.mkdir("./imagenes/"+time.strftime("%d-%m-%y"))
        screenshot.save(direccion)
    resultados = reverse_search(direccion)
    query = ""
    for resultado in resultados:
        query+=resultado.name
        query+=resultado.description
    return query

#########################################FIN########################################



def busquedaPregunta():
    titulo_string,lista_palabras = procesamientoImagen()
    palabra_clave=palabraClave(titulo_string)
    print(palabra_clave)
    definitivo = busqueda(titulo_string,titulo_string)
    coincidencias(definitivo,lista_palabras)

def busquedaImagen():
    screenshot = pyautogui.screenshot(region=(988, 55, 371, 596))
    definitivo=queryImages(screenshot)#falta implementar
    input("\npresione para hacer screenshot\n")
    titulo_string,lista_palabras = procesamientoImagen()
    coincidencias(definitivo,lista_palabras)

def busquedaShazam():
    palabra_clave = input("\nEscriba la palabra clave\n")
    try:
        titulo_string,lista_palabras = procesamientoImagen()
    except:
        pass
    definitivo = busqueda(titulo_string,palabra_clave)
    print(definitivo)
    coincidencias(definitivo,lista_palabras)

#start = time.time()
while True:
    try:
        n = int(input("\nBienvenido señor, espero órdenes\n1: Buscar pregunta\n2: Buscar imagen\n3: Buscar Shazam\n0:Salir\n\nOpción: "))
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
        busquedaShazam()
    input()
    os.system("cls")
