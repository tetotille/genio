def contarCoincidencias(texto, lista_palabras):
    for pal in lista_palabras:
        b = 0
        cont = -1
        acu = 0

        while b !=-1:
            b = texto[acu:len(texto)].find(pal)
            cont+=1
            acu+=b+1
        print("\n\n", pal+" = "+str(cont))

        cont = -1
        for palabrita in pal.split():
            b = 0
            acu = 0
            while b !=-1:
                b = texto[acu:len(texto)].find(palabrita)
                cont+=1
                acu+=b+1
        print("Palabras por separado =", cont)
