from procesamiento import procesar

from search import search
from search import reverse_search
from coincidencias import contarCoincidencias
import pyautogui
import os
import time
from clave import palabraClave



########################################PROCESAMIENTO DE IMAGEN#########################
def procesamientoImagen():
    screenshot = pyautogui.screenshot(region=(860, 50, 325, 620))
    try:
        screenshot.save("./screens/"+time.strftime("%d-%m-%y")+"/"+str(time.time())+".png")
    except:
        os.mkdir("./screens/"+time.strftime("%d-%m-%y"))
        screenshot.save("./screens/"+time.strftime("%d-%m-%y")+"/"+str(time.time())+".png")
    pregunta, respuestas=procesar(screenshot)
    print("La pregunta es:\n" + pregunta)
    print("\nOpciones: ")
    for respuesta in respuestas: print(respuesta)
    return pregunta,respuestas

########################################BUSQUEDA####################################
def busqueda(pregunta,palabras_claves):
    resultados = search(palabras_claves, 1)
    query = ""
    for resultado in resultados:
        query+=resultado.name
        query+=resultado.description
    return query

##########################################COINCIDENCIAS##############################
def coincidencias(query,respuestas):
    query_min = query.lower()
    contarCoincidencias(query_min, respuestas)

#########################################BUSQUEDA A TRAVES DE IMAGENES#######################
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


#########################################FUNCIONES DEL MAIN#############################
def busquedaPregunta():
    pregunta,respuestas = procesamientoImagen()
    palabras_claves=palabraClave(pregunta)
    print("PALABRA CLAVE: "+palabras_claves)
    query = busqueda(pregunta,palabras_claves)
    coincidencias(query,respuestas)

def busquedaImagen():
    screenshot = pyautogui.screenshot(region=(860, 50, 325, 620))
    query=queryImages(screenshot)#falta implementar
    input("\npresione para hacer screenshot\n")
    pregunta,respuestas = procesamientoImagen()
    coincidencias(query,respuestas)

def busquedaManual():
    palabras_claves = input("\nEscriba la palabra clave\n")
    try:
        pregunta,respuestas = procesamientoImagen()
    except:
        pass
    query = busqueda(pregunta,palabras_claves)
    print(query)
    coincidencias(query,respuestas)
#COMENTARIO
while True:
    try:
        n = int(input("Bienvenido señor, espero órdenes\n1.Busqueda Automática\n2.Busqueda Imagen\n3.Busqueda Manual\n0.Salir\n"))
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
