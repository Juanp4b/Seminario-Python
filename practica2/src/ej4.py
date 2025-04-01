# Valide un nombre de usuario con los siguientes criterios:
# Al menos 5 caracteres.
# Contiene al menos un número.
# Contiene al menos una letra mayúscula.
# Solo puede contener letras y números.

def validar(text):
    if len(text) >= 5:
        if any(char.isdigit() for char in text):
            if any(char.isupper() for char in text):
                if text.isalnum():
                    return True
    return False