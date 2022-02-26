# include a blioteca time
import time

# define a função busca_sequencial com dois parâmetros: vetor e elemento


def busca_sequencial(v, x):
    i = 0

    # percorrer o vetor
    while i < len(v):
        if v[i] == x:
            return i
        i += 1

    return -1


# defindo o vetor
vetor = list(range(0, 100))

# print (vetor)
chave = 98

# definindo o elemento 98 na posição 2
vetor[6] = chave

# grava o instante tempo inicial do processamento
antes = time.time()

# busca na função a posição aonde se encontra o elemento CHAVE
posicao = busca_sequencial(vetor, chave)

# grava o instante tempo final do processamento
depois = time.time()

# tempo total do processamento
total = (depois-antes) * 1000

# testa posicao do vetor
if posicao >= 0:
    print('elemento foi encontrado na posicao', chave, posicao)
else:
    print('elemento não encontrado.')

# imprime o tempo gasto de processamento
print('\nO tempo total gasto foi: ms', total)
