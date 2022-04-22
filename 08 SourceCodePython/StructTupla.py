from collections import namedtuple
lista = []
cliente = namedtuple('cliente', 'nome cpf limite compras')

umCliente = cliente('Heleno', '01234567890', 5000.0, 300.0)
lista.append(umCliente)

umCliente = cliente('Paulo', '01234567890', 5000.0, 700.0)
lista.append(umCliente)

print(umCliente.cpf)
print(lista)