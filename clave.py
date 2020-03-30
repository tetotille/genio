def palabraClave(pregunta):
    a = pregunta.find('"')
    tamaño = len(pregunta)
    if a == -1:
        a = pregunta.find('“')
        if a == -1:
            a = pregunta.find('«')
    if a != -1:
        a2 = pregunta[a+1:tamaño].find('"')
        if a2 == -1:
            a2 = pregunta[a+1:tamaño].find('”')
            if a2 == -1:
                a2 = pregunta[a+1:tamaño].find('»')+a+1
            else:
                a2+=a+1
        else:
            a2 +=a+1
        palabras_claves = '"'+pregunta[a+1:a2]+'"'
        palabras_claves = palabras_claves.replace("\n"," ")
    elif not pregunta[2:-1].islower():
        aux = ""
        for i in range(3,len(pregunta)):
            letra = pregunta[i]
            if letra.isupper():
                j = i
                i = pregunta[j:-1].find(" ")
                if i != -1:
                    i = i + j
                else:
                    i = len(pregunta)
                aux = aux+' "'+pregunta[j:i]+'"'
        palabras_claves = aux
    elif "el" in pregunta.lower() and "es":
        a = pregunta.lower().find("el")
        b = pregunta.find("es")
        palabras_claves = pregunta[a+3:b-1]
    else:
        palabras_claves = pregunta
    if " NO " in pregunta:
        palabras_claves = palabras_claves.replace( ' "NO" "O"',' ')
    return palabras_claves
