import os
import time

# processamento - escopo GLOBAL
qtd_filhos = 0
maior_sal = 0
qtd_pes_100 = 0
        
qtd_pessoas_pesq = 0
sum_sal = 0

def menuAlteracao():
    #limpar a tela
    os.system("clear")
    
    print("Tipo de Alteração")
    print("1 - Índice")
    print("2 - por Nome")
    print("3 - Sair")

def menu():
    #limpar a tela
    os.system("clear")
    
    print("Pesquisa Populacional")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Pesquisar")
    print("5 - Sair")

def incuir():
        #limpar a tela
        os.system("clear")
        
        print("Módulo de Inclusão")
        
        # inputs
        nome    = str(input("Informe o nome? "))
        sal     = float(input("Informe o salário? "))
        
        if sal > 0:
           nFilhos = float(input("Informe o número de filhos? "))
        
        if sal >= 0:
          listaNome.append(nome)    
          listaSal.append(sal)
          listanFilhos.append(nFilhos)
        
        qtd_filhos = 0
        maior_sal = 0
        qtd_pes_100 = 0
        
        qtd_pessoas_pesq = 0
        sum_sal = 0
        while sal > 0:
          qtd_pessoas_pesq += 1
        
          sum_sal += sal # somatório de salários
          qtd_filhos += nFilhos # somatório de filhos
        
          if maior_sal < sal:
            maior_sal = sal
        
          if sal < 100:
           qtd_pes_100 += 1
           
          # NOVOS inputs
          print()
          nome    = str(input("Informe o nome? "))
          sal     = float(input("Informe o salário? "))
        
          if sal > 0:
            nFilhos = float(input("Informe o número de filhos? "))
        
            listaNome.append(nome)    
            listaSal.append(sal)
            listanFilhos.append(nFilhos)
        ############# Fim do while

def alterar():
    #limpar a tela
    os.system("clear")
        
    print("Módulo de Alteração")
    while True:
        menuAlteracao()
        
        try:
            opc = int(input("Selecione uma opção:"))
        except ValueError as e:
            print("Não eh permitido literal!!!")
    
        if opc == 1:
            indice = int(input("Informe a posição para alteração? "))
            
            if indice > len(listaNome):
                print('Não existe o índice na lista!!!')
                time.sleep(1)
            else:
              # DADOS NOVOS para alteração inputs
              nome    = str(input("Informe o NOVO nome? "))
              
              sal     = float(input("Informe o NOVO salário? "))
              while sal < 0:
                 print("Salário não pode ser negativo!!!")
                 sal  = float(input("Informe o NOVO salário? "))
            
              nFilhos = float(input("Informe o número de filhos? "))
            
              listaNome[indice] = nome    
              listaSal[indice] = sal
              listanFilhos[indice] = nFilhos
        elif opc == 2:
            print('Alteração por nome')
            nome    = str(input("Informe o nome? "))
            
            # Percorrendo a lista 
            for indice in range(len(listaNome)):
              if nome == listaNome[indice]:
                 # ALTERAR OS DADOS na lista - NOVOS para alteração inputs
                sal     = float(input("Informe o NOVO salário? "))
                while sal < 0:
                    print("Salário não pode ser negativo!!!")
                    sal  = float(input("Informe o NOVO salário? "))
            
                nFilhos = float(input("Informe o número de filhos? "))
            
                listaNome[indice] = nome    
                listaSal[indice] = sal
                listanFilhos[indice] = nFilhos
                break
              else:
                print("Nome não existe na lista")    

        elif opc == 3:
            break
        else:
            print('Opção inválida')

def exluir():
    print("Excluindo")
    
def consultar():
    print("Consultando")

# inicializamos a estrutura de dados = array do tipo lista
listaNome    = []
listaSal     = []
listanFilhos = []

opc = -1

while True:
    # Exibir o menu - finaliza com opção = 5
    menu()
    
    try:
        opc = int(input("Selecione uma opção:"))
    except ValueError as e:
        print("Não eh permitido literal!!!")
    
    if opc == 1:
        incuir()
    elif opc == 2:    
         alterar()
    elif opc == 3:    
        excluir()
    elif opc == 4:    
        consultar()
    elif opc == 5:    
        break
    else:
        print("Opção inválida do menu!!!")
    
    time.sleep(2)
    
# Quando finalizar a aplicação, imprime os resultados
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
   
# Para testar imprimimos a posição 1 do array
print(listaNome[1])   
print(listaSal[1])   
print(listanFilhos[1])   