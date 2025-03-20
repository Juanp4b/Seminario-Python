lista = []
for i in range(30): lista.append(i)
print(lista)

for i in lista:
    if i==0 or i%2 == 1: continue
    print(i)
