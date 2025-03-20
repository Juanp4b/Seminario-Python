# Escribe un programa que tome una lista de números enteros como entrada
# del usuario. Luego, convierte cada número en la lista a string y únelos en
# una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier
# número que sea múltiplo de 3 de la cadena final.

lista = []
cant = int(input('Cuantos numeros quiere ingresar?: '))
for i in range(cant):
    num = int(input('Ingrese un numero: '))
    lista.append(num)

merge = ''
for i in lista:
    if i % 3 != 0:
        merge += str(i) + '-'

print(merge[:-1]) # se elimina el guion al final de la cadena.