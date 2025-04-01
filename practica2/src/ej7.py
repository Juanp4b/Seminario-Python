# Genere un código de descuento aleatorio para un usuario en base a su nombre, la fecha
# actual y el resto deben ser números o letras aleatorias. El código debe tener una longitud de
# 30 caracteres, todas las letras deben ser mayúsculas.
# El usuario debe ingresarse por teclado y debe validar que no exeda los 15 caracteres.

import random, string
from datetime import date

def generarCodigo(name, fecha, max=30):
    code = name.upper()

    fecha = str(fecha)
    div = ''.join(fecha.split('-'))
    code += '-' + div + '-'
    
    extra = string.ascii_uppercase + string.digits
    for _ in range(max-len(code)):
        code += random.choice(extra)
    
    return(code)
