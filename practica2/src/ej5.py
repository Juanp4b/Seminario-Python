# Dado el tiempo de reacción de un jugador en milisegundos, clasifíquelo en las siguientes
# categorías:
# Menos de 200 ms: Rápido
# Entre 200 y 500 ms: Normal
# Más de 500 ms: Lento

def clasificarEntre(tiempo, min=200, max=500):
    if min < max:
        if tiempo < min:
            return 'Rápido'
        elif tiempo > max:
            return 'Lento'
        else:
            return 'Normal'
    else:
        return None