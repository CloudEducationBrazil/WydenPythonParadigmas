#Frase de inicio.
print('==X'*35)
print('Faça um calculo de, Duplo, Triplo ou Raiz quadrada e ainda descubra se seu numero é impar ou par!')
print('==X'*35)
#Números a serem calculados
n = int(input ('insira um numero para fazer o calculo:'))
d = n * 2 
t = n * 3
r = n ** (1/2)
#Chaves para tipo de calculo
cau = input('Insira qual tipo de calculo você deseja fazer (Duplo, Triplo ou Raiz quadradra):')
if cau == 'Triplo':
    print('O Triplo de {} vale {}:'.format(n, t))
if cau == 'Raiz quadrada':
    print('A Raiz quadrade de {} Vale {}'.format(n, r)) 
if cau == 'Duplo':
    print('O Duplo de {} vale {}'.format(n, d))

