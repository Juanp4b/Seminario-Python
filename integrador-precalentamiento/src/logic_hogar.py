from logic_generic import *
columnas = { ##########
    'pondera': 'PONDERA',
    'aglomerado': 'AGLOMERADO',
    'baño': 'IV8', # 2 = no tiene
    'tenencia': 'II7', # 1 = propietario de vivienda y terreno
    'miembros': 'IX_TOT'
}

def read_file(path_file):
    global data,columnas
    data = load_file(path_file)
    load_cols(columnas)


def esPropietarioCompleto(row):
    return int(get('tenencia',row)) == 1

def tieneBañoConMasMiembros(row):
    return (int(get('baño',row)) == 2) and (int(get('miembros',row)) > 2)


def analyze():
    global data
    gotten = {
        'total': 0,
        'propietario': 0,
        '2_con_baño': {}
    }
    
    for row in data:
        pondera = int(get('pondera',row))
        gotten['total'] += pondera
        
        gotten['propietario'] += esPropietarioCompleto(row) * pondera
        
        aglomerado = get('aglomerado',row)
        if tieneBañoConMasMiembros(row):
            gotten['2_con_baño'][aglomerado] = gotten['2_con_baño'].get(aglomerado,0) + pondera
    
    return gotten
