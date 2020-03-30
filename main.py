from procesamiento import procesar
from time import time
from search import search
from coincidencias import contarCoincidencias
import pyautogui
import os





########################################PROCESAMIENTO DE IMAGEN#########################
def procesamientoImagen():
    screenshot = pyautogui.screenshot(region=(860, 50, 325, 620))
    screenshot.save("./Screens/"+str(time())+".jpg")
    titulo_string, lista_palabras=procesar(screenshot)
    return titulo_string,lista_palabras
########################################PALABRA CLAVE##############################
#falta agregar una función que elija lo que haya que buscar
def palabraClave(titulo_string):
    a = titulo_string.find('"')
    tamaño = len(titulo_string)
    if a == -1:
        a = titulo_string.find('“')
        if a == -1:
            a = titulo_string.find('«')
    if a != -1:
        a2 = titulo_string[a+1:tamaño].find('"')
        if a2 == -1:
            a2 = titulo_string[a+1:tamaño].find('”')
            if a2 == -1:
                a2 = titulo_string[a+1:tamaño].find('»')+a+1
            else:
                a2+=a+1
        else:
            a2 +=a+1
        palabra_clave = '"'+titulo_string[a+1:a2]+'"'
        palabra_clave = palabra_clave.replace("\n"," ")
    elif not titulo_string[2:-1].islower():
        aux = ""
        for i in range(3,len(titulo_string)):
            letra = titulo_string[i]
            if letra.isupper():
                j = i
                i = titulo_string[j:-1].find(" ")
                if i != -1:
                    i = i + j
                else:
                    i = len(titulo_string)
                aux = aux+' "'+titulo_string[j:i]+'"'
        palabra_clave = aux
    elif "el" in titulo_string.lower() and "es":
        a = titulo_string.lower().find("el")
        b = titulo_string.find("es")
        palabra_clave = titulo_string[a+3:b-1]
    else:
        palabra_clave = titulo_string
    if " NO " in titulo_string:
        palabra_clave = palabra_clave.replace( ' "NO" "O"',' ')
    return palabra_clave

########################################BUSQUEDA####################################
def busqueda(titulo_string,palabra_clave):
    resultados = search(palabra_clave, 1)
    definitivo = ""
    for resul in resultados:
        definitivo+=resul.name
        definitivo = definitivo+resul.description
    return definitivo

##########################################COINCIDENCIAS##############################
def coincidencias(definitivo,lista_palabras):
    texto = definitivo.lower()
    contarCoincidencias(texto, lista_palabras)

#########################################FIN########################################



def busquedaPregunta():
    titulo_string,lista_palabras = procesamientoImagen()
    #print(titulo_string)
    palabra_clave=palabraClave(titulo_string)
    definitivo = busqueda(titulo_string,palabra_clave)
    coincidencias(definitivo,lista_palabras)

def busquedaImagen():
    screenshot = pyautogui.screenshot(region=(1089, 210, 277, 440))
    definitivo=googleImages(screenshot)#falta implementar
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

#start = time()
#print("HOLA")
while True:
    try:
        n = int(input("Bienvenido señor, espero órdenes\n1.Busqueda Pregunta\n2.Busqueda Imagen\n3.Busqueda Shazam\n"))
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
