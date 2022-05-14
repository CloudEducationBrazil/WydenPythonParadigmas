with open("f://listaNiver.txt", "wt", encoding="utf-8") as f:
    f.write("Julia ,"+"17,"+chr(13))
    f.write("Maria ,"+"69,"+chr(13))
    f.write("josy ,"+"51,"+chr(13))

text_file = open("f://listaNiver.txt")
lista = text_file.read().split(",")
print(lista)


text_file = open("f://listaNiver.txt")
count = 0
for line in text_file:
    count = count + 1
print('line count:', count)

text_file = open('f://listaNiver.txt')
for line in text_file:
    if line.startswith("josy"):
        print("oiiii", line)

fname = input('Digite o nome do arquivo: ')
try:
    text_file = open(fname)

    conteudo = text_file.read()
    print('aqui', conteudo)

    print("***")
    print("***")
    print("***")
    for line in text_file:
        print(line)

except:
    print(f'Erro na abertura do arquivo {fname}')
    quit()
# linha2 = text_file.read()
# print('ooo', linha2)
