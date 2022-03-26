mat = []

print('matriz 3x2')
for lin in range(3):
  lista = []     
  for col in range(2):
      elemento = int(input(f'Informe os elementos da matriz[{lin},{col}]: '))
      lista.append(elemento)
  mat.append(lista)

print()      
for lin in range(3):
  print('[')    
  for col in range(2):
      print(mat[lin][col], end=' ')
  print(']')