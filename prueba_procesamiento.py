from procesamiento import procesar
import cv2
from search import search
from coincidencias import contarCoincidencias
from PIL import Image

def palabraClave(titulo_string):
    a = titulo_string.find('"')
    if a == -1: a = titulo_string.find('“')
    if a != -1:
        a2 = titulo_string[a+1:-1].find('"')
        if a2 == -1:
            a2 = titulo_string[a+1:-1].find('”')+a+1
        else:
            a2 +=a
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
    return palabra_clave

def busqueda(titulo_string,palabra_clave):
    resultados = search(palabra_clave, 1)
    definitivo = ""
    for resul in resultados:
        definitivo += resul.name
        definitivo = definitivo+resul.description
    return definitivo

def busquedaPregunta(titulo_string = None, lista_palabras = None):
    definitivo = busqueda(titulo_string,titulo_string)
    coincidencias(definitivo,lista_palabras)

def coincidencias(definitivo,lista_palabras):
    texto = definitivo.lower()
    contarCoincidencias(texto, lista_palabras)

nombre = '1585546578.8814008.jpg'
img = Image.open('./screens/' + nombre)
pregunta, opciones = procesar(img)

print("La pregunta es:\n" + pregunta)
print("\nOpciones: ")
for opcion in opciones: print(opcion)


#print("Respuestas:")
#busquedaPregunta(pregunta, opciones)
palabra_clave = palabraClave(pregunta)
print("PALABRA CLAVE: "+palabra_clave)
definitivo = busqueda(pregunta,palabra_clave)
contarCoincidencias(definitivo.lower(),opciones)
