matriz = []
matrizT = []

for l in range(3):
    lista = []
    for c in range(2):
        elem = int(input('Num: '))
        lista.append(elem)
    matriz.append(lista)

for l in range(2):
    lista = []
    for c in range(3):
        elem = matriz[c][l]
        lista.append(elem)
    matrizT.append(lista)
print (matriz)
print (matrizT)

#4 5
#2 3
#0 8

#4 2 0
#5 3 8

