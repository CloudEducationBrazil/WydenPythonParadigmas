velocidade = float(input('Qual a velocidade atual do veiculo?'))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade, e será multado!')
    multa = (velocidade-80) * 7
    print('O Valor da multa é:R${:.2f}!'.format(multa))
    print('Tome mais cuidado, dirija com atenção, Bom dia!')
else:
    print('Prossiga sua viajem, dirija com segurança, Bom dia!')    