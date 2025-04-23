from logic_generic import *
columnas = {
    'pondera': 'PONDERA',
    'sexo': 'CH04', # 1 = varon, 2 = mujer
    'edad': 'CH06', # >= 18 mayor de edad
    'educacion': 'NIVEL_ED' # 4,5,6 secundario completo
}

def read_file(path_file):
    global data,columnas
    data = load_file(path_file)
    load_cols(columnas)


def esMayorConSecundario(row):
    return (int(get('edad',row)) >= 18) and (int(get('educacion',row)) in (4,5,6))


def analyze():
    global data
    gotten = {
        'total': 0,
        'sexo': {},
        'mayor_con_secundario': 0,
    }
    
    for row in data:
        pondera = int(get('pondera',row))
        gotten['total'] += pondera
        
        sexo = int(get('sexo',row))
        gotten['sexo'][sexo] = gotten['sexo'].get(sexo,0) + pondera
        
        gotten['mayor_con_secundario'] += esMayorConSecundario(row) * pondera
    
    return gotten
