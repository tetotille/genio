def contarCoincidencias(texto, lista_palabras):
    acu2 = 0
    ban_ban = False
    acu2_separado = 0
    for pal in lista_palabras:
        b = 0
        cont = -1
        pal = pal.lower()
        acu = 0
        bandera_ambas = False
        if pal == "ambas" or pal == "ambos": bandera_ambas = True
        if bandera_ambas: ban_ban = True
        while b !=-1:
            b = texto[acu:len(texto)].find(pal)
            cont+=1
            acu+=b+1
        if not bandera_ambas:print("\n\n", pal+" = "+str(cont))
        acu2 +=cont

        cont = -1
        for palabrita in pal.split():
            b = 0
            acu = 0
            while b !=-1:
                b = texto[acu:len(texto)].find(palabrita)
                cont+=1
                acu+=b+1
        if not bandera_ambas:print(" PS =", cont)
        acu2_separado +=cont
    if ban_ban:
        print("\n\n", "AMBAS"+" = "+str(acu2))
        print(" PS =", acu2_separado)
