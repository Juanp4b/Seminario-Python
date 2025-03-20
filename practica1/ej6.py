# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
# listas, una con los número pares y otras con los que son impares. Imprima
# las listas al terminar de procesarlas.

lista = []
for i in range(30): lista.append(i)
print(lista)

pares = []
impares = []
for i in lista:
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Pares: {pares}')
print(f'Impares: {impares}')
