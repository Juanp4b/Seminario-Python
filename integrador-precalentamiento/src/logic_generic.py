import csv

def load_file(path_file):
    global header
    with open(path_file, encoding='UTF-8') as archivo_csv:
        reader = csv.DictReader(archivo_csv, delimiter=';')
        data = list(reader)
    return data

def load_cols(columns):
    global columnas
    columnas = columns

def get(col,row):
    global columnas
    return row[columnas[col].upper()]
