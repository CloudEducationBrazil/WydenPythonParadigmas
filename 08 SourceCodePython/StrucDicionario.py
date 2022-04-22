lista = {}

umCliente = {'id':1, 'nome':'Heleno', 'cpf':'01234567890', 'limite':5000.0, 'compra':300.0}
lista[0] = umCliente

umCliente = {'id':2, 'nome':'Paulo', 'cpf':'45674567890', 'limite':3000.0, 'compra':200.0}
lista[1] = umCliente
#lista.pop(1)

for dic in lista.keys():
  print(lista[dic])
  
print(lista)
  