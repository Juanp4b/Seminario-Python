# Dadas varias descripciones de streams en Twitch, cuente cuántas menciones hay de
# "entretenimiento", "música" y "charla".

def mencionesDeEn(keyword,list):
    total = 0
    for desc in list:
        for word in desc.split():
            if keyword == word.lower():
                total += 1
    return total