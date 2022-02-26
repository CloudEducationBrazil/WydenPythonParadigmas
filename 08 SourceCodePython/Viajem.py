print('-=-' *30)
print('Atenção, Para viajem com menos de 200km de distancia, o valor por km é de: R$0,50')
print('E Para viajens acima de 200km de distancia, o valor por km é de: R$0,45')
print('-=-'*30)
km = float(input('Quantos km você deseja viajar?'))
if km <= 200:
    print('Sua viajem não alcança o limite promocional!')
    valor1 = km * 0.50
    print('O Valor da sua viajem será: R${:.2f}!'.format(valor1))
    print('Tenha um boa viajem!')
else:
    print('Sua viajem foi aprovada, e receberá o valor promocional!')
    valor2 = km * 0.45
    print('O Valor da sua viajem será: R${:.2f}!'.format(valor2))
    print('Tenha um boa viajem!')    