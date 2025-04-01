# Dado un código de conducta para un servidor de Discord: []
# Solicite una palabra clave al usuario e imprima todas las reglas que la contengan.

def dividirReglas(rules):
    split = rules.split('.')
    for i in range(len(split)):
        split[i] = split[i].strip()
    return split

def obtenerReglas(rules,keyword):
    split = dividirReglas(rules)
    # out = []
    # for rule in split:
    #     if keyword in rule:
    #         out.append(rule)
    out = [rule for rule in split if keyword in rule]
    return out
    
    

# rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
# Evita el spam. No publiques enlaces sospechosos o repetitivos.
# No compartas información personal.
# Usa los canales adecuados para cada tema.
# Sigue las instrucciones de los moderadores."""

# obtenerReglas(rules)