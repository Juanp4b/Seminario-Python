# Dado un listado de títulos de streams en Twitch: []
# Encuentre el título con más palabras y muéstrelo en pantalla.

def contarPalabras(text):
    return len(text.split())

def mayorTitulo(list):
    maxWords = 0
    maxTitle = ''
    for title in list:
        words = contarPalabras(title)
        if words > maxWords:
            maxTitle = title
            maxWords = contarPalabras(title)
    return maxTitle