lista = [];
soma = 0;

def inputLista():
    for i in range(3):
      n = int(input("Numero? "));
      lista.append(n);

def proccessLista():
    global soma;
    for i in range(3):
      soma += lista[i];

def outputLista():
    global soma;
    print(lista);
    print(soma);

inputLista();
proccessLista();
outputLista();
