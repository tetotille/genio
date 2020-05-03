def contarCoincidencias(google_str, respuestas):
    acu2 = 0
    ban_ban = False
    acu2_separado = 0
    for respuesta in respuestas:
        b = 0
        cont = -1
        respuesta = respuesta.lower()
        acu = 0
        bandera_ambas = False
        if respuesta == "ambas" or respuesta == "ambos": bandera_ambas = True
        if bandera_ambas: ban_ban = True
        while b !=-1:
            b = google_str[acu:len(google_str)].find(respuesta)
            cont+=1
            acu+=b+1
        if not bandera_ambas:print("\n\n", respuesta+" = "+str(cont))
        acu2 +=cont

        cont = -1
        for palabrita in respuesta.split():
            if len(palabrita) <= 2: continue
            b = 0
            acu = 0
            while b !=-1:
                b = google_str[acu:len(google_str)].find(palabrita)
                cont+=1
                acu+=b+1
        if not bandera_ambas:print(" PS =", cont)
        acu2_separado +=cont
    if ban_ban:
        print("\n\n", "AMBAS"+" = "+str(acu2))
        print(" PS =", acu2_separado)
