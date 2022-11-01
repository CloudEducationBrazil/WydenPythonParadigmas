# input - entrada de dados
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1/n!
n = int(input("Informe n inteiros positivos da sequência E: "))

# processamento
somaE = 1
for denominador in range(1, n + 1):
    fat = denominador
    # calculo fatorial
    for x in range(denominador-1, 1, -1): # ajuste
        fat *= x
    # print (fat)
    somaE += 1 / fat
    
# output         
print ('Resultado da expressão: {:.3} '.format(somaE))