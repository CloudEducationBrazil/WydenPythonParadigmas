print('==X'*30)
print('Faça um calculo de, Triplo ou Raiz quadrada!')
print('==X'*30)
n = int(input ('insira um numero para fazer o calculo:'))
t = n * 3
r = n ** (1/2)
cau = input('Insira qual tipo de calculo você deseja fazer (Triplo ou Raiz quadradra):')
if cau == 'Triplo':
    print('O Triplo de {} vale {}:'.format(n, t))
else:
    cau == 'Raiz quadrada'
    print('A Raiz quadrade de {} Vale {}'.format(n, r)) 
       
