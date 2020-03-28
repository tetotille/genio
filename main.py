from procesamiento import procesar
from time import time
from search import search
from coincidencias import contarCoincidencias

start = time()
########################################PROCESAMIENTO DE IMAGEN#########################
titulo_string, lista_palabras=procesar("imagen4.jpeg")

########################################PALABRA CLAVE##############################
#falta agregar una función que elija lo que haya que buscar
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
########################################BUSQUEDA####################################

titulo_string = titulo_string.lower()
resultados = search(palabra_clave, 1)
definitivo = ""
for resul in resultados:
    definitivo = definitivo+resul.description

##########################################COINCIDENCIAS##############################

texto = definitivo.lower()
contarCoincidencias(texto, lista_palabras)

#########################################FIN########################################
print("Tardó mucho nomás", time()-start)
