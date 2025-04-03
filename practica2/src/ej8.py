# Determine si dos palabras ingresadas son anagramas (contienen las mismas letras en
# diferente orden)

def anagramas(w1,w2):
    return sorted(w1.lower()) == sorted(w2.lower())