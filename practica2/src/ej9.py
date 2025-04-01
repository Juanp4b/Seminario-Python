# Desarrollar un sistema que permita realizar las siguientes operaciones en los datos:
# Eliminar espacios extra en los nombres.
# Convertir todos los nombres a formato de título (primera letra en mayúscula y el
# resto en minúscula).
# Eliminar registros duplicados para evitar clientes repetidos.
# Eliminar valores vacíos o nulos, ya que no aportan información válida.
# Mostrar la lista limpia de clientes listos para usar en el sistema de facturación.

def rmEspacios(text):
    while text.startswith(' '):
        text = text[1:]
    while text.endswith(' '):
        text = text[:-1]
    return text
    

def limpiar(clients):
    out = set() # Eliminar registros duplicados para evitar clientes repetidos.
    for client in clients:
        if client != None:
            clean = str(client)
            # Eliminar espacios extra en los nombres
            clean = rmEspacios(clean)
            # Convertir todos los nombres a formato de título
            clean = clean.title()
            out.add(clean)
        
    # Eliminar valores vacíos o nulos, ya que no aportan información válida.
    out = out - {'',}
    
    return sorted(list(out))
