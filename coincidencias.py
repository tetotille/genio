def contarCoincidencias(texto, respuestas):
    for respuesta in respuestas:
        b = 0
        letras = len(respuesta)
        contador = -1
        acumulador = 0

        while b !=-1:
            b = texto[acumulador:len(texto)].find(respuesta)
            contador+=1
            acumulador+=b+1
        print(respuesta+" = "+str(contador))
