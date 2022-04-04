# inputs
sal     = float(input("Informe o salário? "))
nFilhos = float(input("Informe o número de filhos? "))

# processamento
qtd_pessoas_pesq = 0
sum_sal = 0
qtd_filhos = 0
maior_sal = sal
qtd_pes_100 = 0

while sal > 0:
  qtd_pessoas_pesq += 1

  sum_sal += sal # somatório de salários
  qtd_filhos += nFilhos # somatório de filhos

  if maior_sal < sal:
    maior_sal = sal

  if sal < 100:
   qtd_pes_100 += 1
   
  sal     = float(input("Informe o salário? "))

  if sal > 0:
    nFilhos = float(input("Informe o número de filhos? "))
############# Fim do while

print()
if qtd_pessoas_pesq > 0:
   md_sal_pop = sum_sal / qtd_pessoas_pesq
   md_num_filhos = qtd_filhos / qtd_pessoas_pesq
   per_pes_sal_100 = qtd_pes_100 / qtd_pessoas_pesq

   print('\n Média de salário da pop: ', md_sal_pop)
   print('\n Média de número de filho: ', md_num_filhos)
   print('\n Maior salário da pop: ', maior_sal)
   print('Percentual de pessoas sal até $100: ', per_pes_sal_100)
else:
   print('\n Primeiro salário informado foi negativo')
    