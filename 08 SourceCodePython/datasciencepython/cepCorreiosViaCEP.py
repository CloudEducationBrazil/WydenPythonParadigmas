import requests
import os

# https://viacep.com.br/
# https://viacep.com.br/ws/41720075/json/
'''{
  "cep": "41720-075",
  "logradouro": "Rua Jayme Sapolnik",
  "complemento": "",
  "bairro": "Imbuí",
  "localidade": "Salvador",
  "uf": "BA",
  "ibge": "2927408",
  "gia": "",
  "ddd": "71",
  "siafi": "3849"
}'''

os.system("cls")
cep = input("Informe o CEP: ")

cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    #dic_requisicao = requisicao.json()
    #print('retorno ' , requisicao.status_code)

    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()

        print(dic_requisicao)

        uf = dic_requisicao["uf"]
        cidade = dic_requisicao['localidade']
        bairro = dic_requisicao['bairro']
        #print('uf', uf)
    else:
        print("CEP Inválido")    
else:
    print("CEP Inválido")