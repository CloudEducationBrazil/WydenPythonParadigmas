#mat=[[3, 4],[7, 8],[0, 1]]
mat=[[0, 0],[0, 0 ],[0, 0]]

for lin in range(3):
    for col in range(2):
       num = int(input(f'Informe a matriz [{lin}][{col}]'))
       mat[lin][col] = num
       
for lin in range(3):
    print('[', end='')
    for col in range(2):
        print (f'{mat[lin][col]:^5}', end='')
    print(']')