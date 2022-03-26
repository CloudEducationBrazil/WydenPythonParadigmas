lista = []
print ('Tamanho da lista', len(lista) )
print ('Lista Atual', lista)
print()

#inseriu no final da lista
num = int(input('Informe o elemento a ser inserido? '))
lista.append(num)

lista.append(5)
lista.append(4)
lista.append(7)
print ('Tamanho da lista', len(lista) )
print ('Lista com inclusão de elemento', lista)
print()

#removeu o elemento da lista
lista.remove(5)
print ('Tamanho da lista', len(lista) )
print ('Lista com elemento removido', lista)
