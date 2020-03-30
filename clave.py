def palabraClave(pregunta):
    a = pregunta.find('"')
    if a != -1:
        a2 = pregunta[a+1:-1].find('"')+a
        palabras_claves = pregunta[a+1:a2]
    elif not pregunta[2:-1].islower():
        aux = ""
        for i in range(len(pregunta[2:-1])):
            letra = pregunta[i+2]
            if letra.isupper():
                j = i
                i = pregunta.find(" ")
                aux = aux+pregunta[j:i]
        palabras_claves = aux
    elif "el" in pregunta.lower() and "es":
        a = pregunta.lower().find("el")
        b = pregunta.find("es")
        palabras_claves = pregunta[a+3:b-1]
    else:
        palabras_claves = pregunta
    return palabras_claves
