lista = []

for i in range(0,5):
    element = int (input('Digite um numero : '))
    lista.append(element)
    
print(lista)
print('\n')

remover = int(input('Digite um numero que desejar apagar:'))

if remover in lista:
   lista.remove(remover)
else:
   print('Elemento não encontrado na lista.')
      
print()     
print('Nova Lista', lista)