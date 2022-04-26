# input(entrada de dados): Declaração => vetor = lista
numeros_entrada = []
numeros_saida = []

def lerNumero():
  return int(input("Digite um número: "))
  
# inputs: Entrada de Dados  
for numero in range(10):
  numeros_entrada.append(lerNumero())

# Processamento: Lógica; i = indice; numeros_entrada[i] = elemento  
soma_multiplos = 0
multiplo = 3
for i in range(len(numeros_entrada)):
  if numeros_entrada[i] % multiplo == 0:
    soma_multiplos += numeros_entrada[i]
    numeros_saida.append(i)

# Output; Saída de Dados  
print("A soma dos múltiplos de dado o conjunto é: ", 
       multiplo, numeros_entrada, soma_multiplos)
