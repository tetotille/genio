def contarCoincidencias(texto, lista_palabras):
    for pal in lista_palabras:
        b = 0
        letras = len(pal)
        cont = -1
        acu = 0
        pal = pal.lower()
        while b !=-1:
            b = texto[acu:len(texto)].find(pal)
            cont+=1
            acu+=b+1
        print(pal+" = "+str(cont))
