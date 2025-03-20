# Implementa un programa que solicite al usuario que ingrese una lista de
# números. Luego, imprime la lista pero detén la impresión si encuentras un
# número negativo. Nota: utilice la sentencia break cuando haga falta.

lista = []
cant = int(input('Cuantos numeros quiere ingresar?: '))
for i in range(cant):
    num = int(input('Ingrese un numero: '))
    lista.append(num)

print('Printing......')
for i in lista:
    if i < 0:
        break
    print(i)
