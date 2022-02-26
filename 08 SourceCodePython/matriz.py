#mat = [[0,0,0], [0,0,0], [0,0,0]]
mat = [[], [], []]
lin = 3
col = 3
soma = 0

for i in range(0,3):
  for j in range(0,3):
    n = int(input(f'valor elemento: [{i},{j}]= '))
    mat[i].append(n)
    soma += n

print(mat)

# print(f'{mat[i][j]:^4}  ', end='')
for i in range(lin):
  for j in range(col):
    print(f'[{mat[i][j]}]  ', end='')
  print()
    
print()
print(soma)    