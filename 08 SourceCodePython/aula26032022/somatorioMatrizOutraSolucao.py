mat = []

# entrando com os elementos da matriz
print('matriz 2x3')
for lin in range(2):
  lista = []     
  for col in range(3):
      elemento = int(input(f'Informe os elementos da matriz[{lin},{col}]: '))
      lista.append(elemento)
  mat.append(lista)

# Realizando a soma
soma = 0
for lin in range(2):
  for col in range(3):
    soma += mat[lin][col]

# imprimindo a matriz
print()      
for lin in range(2):
  print('[', end=' ')      
  for col in range(3):
      print(mat[lin][col], end=' ')
  print(']')

# imprimindo a soma
print()
print('Total', soma)
