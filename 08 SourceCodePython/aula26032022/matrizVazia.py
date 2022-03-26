mat=[]

for lin in range(3):
    linha = []
    for col in range(2):
       num = int(input(f'Informe a matriz [{lin}][{col}]'))
       linha.append(num)
    mat.append(linha)
    
print(mat)