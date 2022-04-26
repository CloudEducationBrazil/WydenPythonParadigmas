# Análise
# input: número? Leitura (desconhecido)
# processamento(Lógica):
#     Dividores do número lido:? 
#     Somar os dividsores: acumulador (soma_divisores)
# ESBOÇO - Da Análise
#Ex.: 6 (é preciso enxergar o TODO)
# Divisores de 6: 1, 2, 3
# Descobrir quando o número é divisor? 
#    N / 1 até N - 1
#     6 / 1 = ok; Resto 0
#     6 / 2 = ok; Resto 0; N % x == 0 
#     6 / 3 = ok;
#     6 / 4 = não ok
#     6 / 5 = não ok
   
# Somar os Dividores: 1 + 2 + 3 = 6
# N Lido = SomaDiv (condicional)

# output: solução: Imprimir se o número é perfeito ou não?

soma_divisores = 0
divisores = []
 
def ehDivisor(num, divisor):
    return num % divisor == 0
 
def lerNumero():
    return int(input("Digite um número para verificar: "))
 
numero = lerNumero()
 
if numero > 0:

    for divisor in range(1, numero):

        if ehDivisor(numero, divisor):
            soma_divisores += divisor
            divisores.append(divisor)

    print("Os divisores são {}".format(divisores))
 
    if soma_divisores == numero:
        print("O número {} é perfeito".format(numero))
        exit()

print("O número {} não é perfeito".format(numero))