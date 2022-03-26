mat = []

print('matriz 2x3')
soma = 0
for lin in range(2):
  lista = []     
  for col in range(3):
      elemento = int(input(f'Informe os elementos da matriz[{lin},{col}]: '))
      lista.append(elemento)
      soma += elemento
      
  mat.append(lista)

print()      
for lin in range(2):
  print('[', end=' ')      
  for col in range(3):
      print(mat[lin][col], end=' ')
  print(']')

print()
print('Total', soma)
